"""
hinlangpy — Hinglish ↔ Hindi (Devanagari) Transliterator
=========================================================

A pure-Python, zero-dependency library for converting between
Roman Hindi (Hinglish) and Devanagari script.

Quick Start::

    import hinlang

    # Roman → Devanagari
    hinlang.to_hindi("Namaste Dosto")
    # 'नमस्ते दोस्तो'

    # Devanagari → Roman
    hinlang.to_roman("नमस्ते दोस्तो")
    # 'namaste dosto'

    # Auto-detect and convert
    hinlang.convert("Kya haal hai")
    # 'क्या हाल है'

:copyright: (c) 2024 hinlangpy contributors.
:license: MIT — see LICENSE for details.
"""

__version__ = "1.0.0"
__author__ = "hinlangpy contributors"
__license__ = "MIT"

from hinlang.roman_to_hindi import RomanToHindi
from hinlang.hindi_to_roman import HindiToRoman
from hinlang.detector import detect_script

# ── Module-level singleton instances (lazy, created once) ──
_r2h = None
_h2r = None


def _get_r2h():
    global _r2h
    if _r2h is None:
        _r2h = RomanToHindi()
    return _r2h


def _get_h2r():
    global _h2r
    if _h2r is None:
        _h2r = HindiToRoman()
    return _h2r


# ────────────────────────────────────────────────
#  PUBLIC API — Convenience functions
# ────────────────────────────────────────────────

def to_hindi(text: str) -> str:
    """
    Convert Roman Hindi (Hinglish) text to Devanagari.

    Args:
        text: Roman/Hinglish text string.

    Returns:
        Devanagari (Hindi) text string.

    Example::

        >>> hinlang.to_hindi("Namaste Dosto")
        'नमस्ते दोस्तो'

        >>> hinlang.to_hindi("Main theek hoon")
        'मैं ठीक हूँ'
    """
    return _get_r2h().transliterate(text)


def to_roman(text: str) -> str:
    """
    Convert Devanagari (Hindi) text to Roman Hinglish.

    Args:
        text: Devanagari (Hindi) text string.

    Returns:
        Roman/Hinglish text string.

    Example::

        >>> hinlang.to_roman("नमस्ते दोस्तो")
        'namaste dosto'

        >>> hinlang.to_roman("मैं ठीक हूँ")
        'main theek hoon'
    """
    return _get_h2r().transliterate(text)


def convert(text: str) -> str:
    """
    Auto-detect input script and convert to the other.

    - If input is Roman → converts to Devanagari.
    - If input is Devanagari → converts to Roman.
    - If input is mixed → converts to Devanagari (default).

    Args:
        text: Input text in either script.

    Returns:
        Converted text in the opposite script.

    Example::

        >>> hinlang.convert("Kya haal hai")
        'क्या हाल है'

        >>> hinlang.convert("क्या हाल है")
        'kya haal hai'
    """
    script = detect_script(text)
    if script == "devanagari":
        return to_roman(text)
    else:
        return to_hindi(text)


def to_hindi_batch(texts: list) -> list:
    """
    Convert a list of Roman Hindi strings to Devanagari.

    Args:
        texts: List of Roman/Hinglish text strings.

    Returns:
        List of Devanagari (Hindi) text strings.

    Example::

        >>> hinlang.to_hindi_batch(["Namaste", "Kya haal hai"])
        ['नमस्ते', 'क्या हाल है']
    """
    engine = _get_r2h()
    return [engine.transliterate(t) for t in texts]


def to_roman_batch(texts: list) -> list:
    """
    Convert a list of Devanagari strings to Roman Hinglish.

    Args:
        texts: List of Devanagari (Hindi) text strings.

    Returns:
        List of Roman/Hinglish text strings.

    Example::

        >>> hinlang.to_roman_batch(["नमस्ते", "क्या हाल है"])
        ['namaste', 'kya haal hai']
    """
    engine = _get_h2r()
    return [engine.transliterate(t) for t in texts]


# ── Public API listing ──
__all__ = [
    "to_hindi",
    "to_roman",
    "convert",
    "to_hindi_batch",
    "to_roman_batch",
    "detect_script",
    "RomanToHindi",
    "HindiToRoman",
    "__version__",
]
