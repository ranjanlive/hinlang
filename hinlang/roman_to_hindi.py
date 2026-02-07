"""
hinlang.roman_to_hindi
=======================

Engine for transliterating Roman Hindi (Hinglish) to Devanagari script.

Usage::

    from hinlang import RomanToHindi

    converter = RomanToHindi()
    print(converter.transliterate("Namaste Dosto"))
    # नमस्ते दोस्तो
"""

from hinlang.dictionary import ROMAN_TO_HINDI, SPECIALS


class RomanToHindi:
    """
    Transliterates Roman Hindi (Hinglish) text into Devanagari script.

    Uses a combination of:
      1. Dictionary lookup (500+ common words)
      2. Character-level phonetic transliteration (for unknown words)

    Example::

        converter = RomanToHindi()
        converter.transliterate("Namaste Dosto")  # 'नमस्ते दोस्तो'
        converter.transliterate("Kya haal hai")    # 'क्या हाल है'
    """

    def __init__(self):
        # ── Phonetic maps ──
        self._vowels = {
            'aa': 'आ', 'ai': 'ऐ', 'au': 'औ',
            'ee': 'ई', 'oo': 'ऊ', 'ou': 'औ',
            'a':  'अ', 'e':  'ए', 'i':  'इ',
            'o':  'ओ', 'u':  'उ',
        }

        self._matras = {
            'aa': 'ा',  'ai': 'ै',  'au': 'ौ',
            'ee': 'ी',  'oo': 'ू',  'ou': 'ौ',
            'a':  '',    'e':  'े',  'i':  'ि',
            'o':  'ो',  'u':  'ु',
        }

        self._consonants = {
            'shree': 'श्री',
            'ksha': 'क्ष', 'gnya': 'ज्ञ', 'dnya': 'ज्ञ',
            'shra': 'श्र', 'thra': 'थ्र', 'ttra': 'त्र',
            'bha': 'भ',  'cha': 'च',  'chh': 'छ',
            'dha': 'ध',  'gha': 'घ',  'jha': 'झ',
            'kha': 'ख',  'nka': 'ंक', 'pha': 'फ',
            'sha': 'श',  'shh': 'ष',  'tha': 'थ',
            'tra': 'त्र', 'nga': 'ंग',
            'nha': 'न्ह', 'lha': 'ल्ह',
            'bh': 'भ',  'ch': 'च',  'dh': 'ध',
            'gh': 'घ',  'jh': 'झ',  'kh': 'ख',
            'ph': 'फ',  'sh': 'श',  'th': 'थ',
            'tr': 'त्र', 'ng': 'ंग', 'nn': 'ण',
            'ny': 'ञ',  'rh': 'ढ',
            'b': 'ब',  'c': 'क',  'd': 'द',  'f': 'फ',
            'g': 'ग',  'h': 'ह',  'j': 'ज',  'k': 'क',
            'l': 'ल',  'm': 'म',  'n': 'न',  'p': 'प',
            'q': 'क़', 'r': 'र',  's': 'स',  't': 'त',
            'v': 'व',  'w': 'व',  'x': 'क्स', 'y': 'य',
            'z': 'ज़',
        }

        self._digits = {
            '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
            '5': '५', '6': '६', '7': '७', '8': '८', '9': '९',
        }

        self._punctuation = {
            '.': '।', '|': '।', '||': '॥',
        }

        # Word dictionary
        self._dictionary = dict(ROMAN_TO_HINDI)
        self._specials = dict(SPECIALS)

    # ── Public API ──

    def add_word(self, roman: str, hindi: str):
        """
        Add a custom word mapping.

        Args:
            roman: Roman/Hinglish word (will be lowercased).
            hindi: Devanagari word.

        Example::

            converter.add_word("bruh", "ब्रह")
        """
        self._dictionary[roman.lower().strip()] = hindi

    def add_words(self, mapping: dict):
        """
        Add multiple custom word mappings.

        Args:
            mapping: Dict of {roman: hindi} pairs.

        Example::

            converter.add_words({"bruh": "ब्रह", "vibe": "वाइब"})
        """
        for roman, hindi in mapping.items():
            self._dictionary[roman.lower().strip()] = hindi

    def transliterate(self, text: str) -> str:
        """
        Transliterate Roman Hindi text to Devanagari.

        Args:
            text: Input Roman/Hinglish text.

        Returns:
            Devanagari (Hindi) text.

        Example::

            >>> converter.transliterate("Namaste Dosto")
            'नमस्ते दोस्तो'
        """
        if not text:
            return ""

        words = text.split()
        result = []

        for word in words:
            prefix, core, suffix = self._strip_punctuation(word)
            converted_suffix = ''.join(
                self._punctuation.get(ch, ch) for ch in suffix
            )
            if core:
                dev_word = self._convert_word(core)
            else:
                dev_word = ''
            result.append(prefix + dev_word + converted_suffix)

        return ' '.join(result)

    # ── Internal ──

    def _strip_punctuation(self, word):
        prefix = ''
        suffix = ''
        while word and not word[0].isalnum():
            prefix += word[0]
            word = word[1:]
        while word and not word[-1].isalnum():
            suffix = word[-1] + suffix
            word = word[:-1]
        return prefix, word, suffix

    def _match_consonant(self, text, pos):
        for length in (5, 4, 3, 2, 1):
            chunk = text[pos:pos + length]
            if chunk in self._consonants:
                return chunk, self._consonants[chunk]
        return None, None

    def _match_matra(self, text, pos):
        for length in (2, 1):
            chunk = text[pos:pos + length]
            if chunk in self._matras:
                return chunk, self._matras[chunk]
        return None, None

    def _match_vowel(self, text, pos):
        for length in (2, 1):
            chunk = text[pos:pos + length]
            if chunk in self._vowels:
                return chunk, self._vowels[chunk]
        return None, None

    def _convert_word(self, word):
        lower = word.lower().strip()
        if not lower:
            return word

        # Dictionary lookup
        if lower in self._dictionary:
            return self._dictionary[lower]
        if lower in self._specials:
            return self._specials[lower]

        # Character-level transliteration
        result = []
        i = 0
        length = len(lower)
        last_was_consonant = False

        while i < length:
            ch = lower[i]

            # Digit
            if ch.isdigit():
                result.append(self._digits.get(ch, ch))
                last_was_consonant = False
                i += 1
                continue

            # Non-alpha
            if not ch.isalpha():
                result.append(ch)
                last_was_consonant = False
                i += 1
                continue

            # Anusvara before certain consonants
            if ch == 'n' and i + 1 < length and lower[i + 1] not in 'aeiou' and lower[i + 1].isalpha():
                if lower[i + 1] in 'gkcdjtpb':
                    result.append('ं')
                    last_was_consonant = False
                    i += 1
                    continue

            # Consonant
            cons_match, cons_dev = self._match_consonant(lower, i)
            if cons_match:
                if last_was_consonant:
                    result.append('्')
                result.append(cons_dev)
                i += len(cons_match)

                if i < length:
                    matra_match, matra_dev = self._match_matra(lower, i)
                    if matra_match:
                        result.append(matra_dev)
                        i += len(matra_match)
                        last_was_consonant = False
                        continue

                last_was_consonant = True
                continue

            # Vowel
            vowel_match, vowel_dev = self._match_vowel(lower, i)
            if vowel_match:
                if last_was_consonant:
                    matra_match, matra_dev = self._match_matra(lower, i)
                    if matra_match:
                        result.append(matra_dev)
                        i += len(matra_match)
                        last_was_consonant = False
                        continue
                result.append(vowel_dev)
                i += len(vowel_match)
                last_was_consonant = False
                continue

            # Fallback
            result.append(ch)
            last_was_consonant = False
            i += 1

        return ''.join(result)
