"""
hinlang.detector
=================

Utility to detect whether text is Roman, Devanagari, or mixed script.
"""


def _is_devanagari_char(ch: str) -> bool:
    """Check if a single character is in the Devanagari Unicode block."""
    cp = ord(ch)
    return 0x0900 <= cp <= 0x097F


def detect_script(text: str) -> str:
    """
    Detect the script of the given text.

    Returns:
        - ``"roman"``      — text is primarily Roman/Latin characters
        - ``"devanagari"``  — text is primarily Devanagari characters
        - ``"mixed"``       — text contains significant amounts of both
        - ``"empty"``       — text is empty or whitespace only

    Args:
        text: Input text string.

    Example::

        >>> detect_script("Hello Dosto")
        'roman'
        >>> detect_script("नमस्ते दोस्तो")
        'devanagari'
        >>> detect_script("Hello दोस्तो")
        'mixed'
        >>> detect_script("")
        'empty'
    """
    if not text or not text.strip():
        return "empty"

    roman_count = 0
    devanagari_count = 0

    for ch in text:
        if ch.isspace() or not ch.isalpha():
            continue
        if _is_devanagari_char(ch):
            devanagari_count += 1
        elif ch.isascii() and ch.isalpha():
            roman_count += 1

    total = roman_count + devanagari_count

    if total == 0:
        return "empty"

    roman_ratio = roman_count / total
    dev_ratio = devanagari_count / total

    if dev_ratio >= 0.7:
        return "devanagari"
    elif roman_ratio >= 0.7:
        return "roman"
    else:
        return "mixed"
