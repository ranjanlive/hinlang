"""Tests for script detection."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hinlang import detect_script


class TestDetectScript:
    """Test the detect_script() function."""

    def test_roman(self):
        assert detect_script("Hello Dosto") == "roman"

    def test_devanagari(self):
        assert detect_script("नमस्ते दोस्तो") == "devanagari"

    def test_mixed(self):
        assert detect_script("Hello दोस्तो") == "mixed"

    def test_empty(self):
        assert detect_script("") == "empty"

    def test_whitespace(self):
        assert detect_script("   ") == "empty"

    def test_numbers_only(self):
        assert detect_script("12345") == "empty"

    def test_mostly_roman(self):
        assert detect_script("Hello World Namaste") == "roman"

    def test_mostly_devanagari(self):
        assert detect_script("नमस्ते दोस्तो कैसे हो") == "devanagari"

    def test_single_roman_word(self):
        assert detect_script("Hello") == "roman"

    def test_single_hindi_word(self):
        assert detect_script("नमस्ते") == "devanagari"


class TestConvertAutoDetect:
    """Test the convert() auto-detection function."""

    def test_roman_to_hindi(self):
        from hinlang import convert
        result = convert("Namaste Dosto")
        assert result == "नमस्ते दोस्तो"

    def test_hindi_to_roman(self):
        from hinlang import convert
        result = convert("नमस्ते दोस्तो")
        assert result == "namaste dosto"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
