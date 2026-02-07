"""
hinlang.hindi_to_roman
=======================

Engine for transliterating Devanagari (Hindi) script to Roman Hinglish.

Usage::

    from hinlang import HindiToRoman

    converter = HindiToRoman()
    print(converter.transliterate("नमस्ते दोस्तो"))
    # namaste dosto
"""

from hinlang.dictionary import HINDI_TO_ROMAN


class HindiToRoman:
    """
    Transliterates Devanagari (Hindi) text into Roman Hinglish.

    Uses a combination of:
      1. Dictionary lookup (500+ common words)
      2. Character-level Devanagari decomposition (for unknown words)

    Example::

        converter = HindiToRoman()
        converter.transliterate("नमस्ते दोस्तो")   # 'namaste dosto'
        converter.transliterate("क्या हाल है")      # 'kya haal hai'
    """

    def __init__(self):
        # ── Character maps ──
        self._vowel_map = {
            'अ': 'a',   'आ': 'aa',  'इ': 'i',   'ई': 'ee',
            'उ': 'u',   'ऊ': 'oo',  'ए': 'e',   'ऐ': 'ai',
            'ओ': 'o',   'औ': 'au',  'ऋ': 'ri',  'ॠ': 'ri',
            'ऑ': 'o',
        }

        self._matra_map = {
            'ा': 'aa',  'ि': 'i',   'ी': 'ee',  'ु': 'u',
            'ू': 'oo',  'े': 'e',   'ै': 'ai',  'ो': 'o',
            'ौ': 'au',  'ृ': 'ri',  'ॉ': 'o',
        }

        self._consonant_map = {
            'क': 'k',   'ख': 'kh',  'ग': 'g',   'घ': 'gh',  'ङ': 'ng',
            'च': 'ch',  'छ': 'chh', 'ज': 'j',   'झ': 'jh',  'ञ': 'ny',
            'ट': 't',   'ठ': 'th',  'ड': 'd',   'ढ': 'dh',  'ण': 'n',
            'त': 't',   'थ': 'th',  'द': 'd',   'ध': 'dh',  'न': 'n',
            'प': 'p',   'फ': 'ph',  'ब': 'b',   'भ': 'bh',  'म': 'm',
            'य': 'y',   'र': 'r',   'ल': 'l',   'व': 'v',
            'श': 'sh',  'ष': 'sh',  'स': 's',   'ह': 'h',
            'क्ष': 'ksh', 'त्र': 'tr', 'ज्ञ': 'gya', 'श्र': 'shr',
        }

        self._nukta_map = {
            'क़': 'q',   'ख़': 'kh',  'ग़': 'gh',  'ज़': 'z',
            'ड़': 'd',   'ढ़': 'dh',  'फ़': 'f',   'य़': 'y',
        }

        self._special_map = {
            'ं': 'n',    'ँ': 'n',    'ः': 'h',
            '्': '',     'ॐ': 'om',
        }

        self._digit_map = {
            '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
            '५': '5', '६': '6', '७': '7', '८': '8', '९': '9',
        }

        self._punct_map = {
            '।': '.', '॥': '||',
        }

        # Word dictionary
        self._dictionary = dict(HINDI_TO_ROMAN)

    # ── Public API ──

    def add_word(self, hindi: str, roman: str):
        """
        Add a custom word mapping.

        Args:
            hindi: Devanagari word.
            roman: Roman/Hinglish word.

        Example::

            converter.add_word("ब्रह", "bruh")
        """
        self._dictionary[hindi.strip()] = roman.lower().strip()

    def add_words(self, mapping: dict):
        """
        Add multiple custom word mappings.

        Args:
            mapping: Dict of {hindi: roman} pairs.

        Example::

            converter.add_words({"ब्रह": "bruh", "वाइब": "vibe"})
        """
        for hindi, roman in mapping.items():
            self._dictionary[hindi.strip()] = roman.lower().strip()

    def transliterate(self, text: str) -> str:
        """
        Transliterate Devanagari (Hindi) text to Roman Hinglish.

        Args:
            text: Input Devanagari (Hindi) text.

        Returns:
            Roman/Hinglish text.

        Example::

            >>> converter.transliterate("नमस्ते दोस्तो")
            'namaste dosto'
        """
        if not text:
            return ""

        words = text.split()
        result = []

        for word in words:
            prefix, core, suffix = self._strip_punctuation(word)
            converted_suffix = ''.join(
                self._punct_map.get(ch, ch) for ch in suffix
            )
            if core:
                roman_word = self._convert_word(core)
            else:
                roman_word = ''
            result.append(prefix + roman_word + converted_suffix)

        return ' '.join(result)

    # ── Internal ──

    def _is_devanagari(self, ch):
        cp = ord(ch)
        return 0x0900 <= cp <= 0x097F

    def _strip_punctuation(self, word):
        prefix = ''
        suffix = ''
        while word and not (self._is_devanagari(word[0]) or word[0].isalnum()):
            prefix += word[0]
            word = word[1:]
        while word and not (self._is_devanagari(word[-1]) or word[-1].isalnum()):
            suffix = word[-1] + suffix
            word = word[:-1]
        return prefix, word, suffix

    def _convert_word(self, word):
        if not word:
            return word

        # Dictionary lookup
        if word in self._dictionary:
            return self._dictionary[word]

        # Character-level romanization
        result = []
        i = 0
        length = len(word)

        while i < length:
            ch = word[i]

            # Digit
            if ch in self._digit_map:
                result.append(self._digit_map[ch])
                i += 1
                continue

            # Punctuation
            if ch in self._punct_map:
                result.append(self._punct_map[ch])
                i += 1
                continue

            # Special chars (anusvara, chandrabindu, visarga)
            if ch in self._special_map and ch != '्':
                result.append(self._special_map[ch])
                i += 1
                continue

            # 2-char conjunct consonants
            if i + 1 < length:
                two_char = word[i:i + 2]
                if two_char in self._consonant_map:
                    roman = self._consonant_map[two_char]
                    i += 2
                    if i < length and word[i] == '्':
                        i += 1
                    elif i < length and word[i] in self._matra_map:
                        roman += self._matra_map[word[i]]
                        i += 1
                    else:
                        if i < length and self._is_devanagari(word[i]):
                            roman += 'a'
                    result.append(roman)
                    continue

            # Nukta consonant
            if ch in self._nukta_map:
                roman = self._nukta_map[ch]
                i += 1
                if i < length and word[i] == '्':
                    i += 1
                elif i < length and word[i] in self._matra_map:
                    roman += self._matra_map[word[i]]
                    i += 1
                else:
                    if i < length and self._is_devanagari(word[i]):
                        roman += 'a'
                result.append(roman)
                continue

            # Regular consonant
            if ch in self._consonant_map:
                roman = self._consonant_map[ch]
                i += 1
                if i < length and word[i] == '्':
                    i += 1
                elif i < length and word[i] in self._matra_map:
                    roman += self._matra_map[word[i]]
                    i += 1
                else:
                    if i < length and self._is_devanagari(word[i]):
                        roman += 'a'
                result.append(roman)
                continue

            # Independent vowel
            if ch in self._vowel_map:
                result.append(self._vowel_map[ch])
                i += 1
                continue

            # Fallback
            result.append(ch)
            i += 1

        return ''.join(result)
