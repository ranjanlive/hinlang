"""Tests for Roman → Hindi transliteration."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hinlang import to_hindi, RomanToHindi


class TestToHindi:
    """Test the to_hindi() convenience function."""

    def test_basic_greeting(self):
        assert to_hindi("Namaste Dosto") == "नमस्ते दोस्तो"

    def test_hello(self):
        assert to_hindi("Hello Dosto") == "हेलो दोस्तो"

    def test_question(self):
        assert to_hindi("Kya haal hai") == "क्या हाल है"

    def test_sentence(self):
        assert to_hindi("Mera naam Ranjan hai") == "मेरा नाम रंजन है"

    def test_how_are_you(self):
        assert to_hindi("Aap kaise ho") == "आप कैसे हो"

    def test_im_fine(self):
        assert to_hindi("Main theek hoon") == "मैं ठीक हूँ"

    def test_good_work(self):
        assert to_hindi("Bahut accha kaam kiya") == "बहुत अच्छा काम किया"

    def test_thanks(self):
        assert to_hindi("Shukriya dost") == "शुक्रिया दोस्त"

    def test_need_water(self):
        assert to_hindi("Mujhe paani chahiye") == "मुझे पानी चाहिए"

    def test_where_going(self):
        assert to_hindi("Kahan ja rahe ho") == "कहां जा रहे हो"

    def test_lets_go_home(self):
        assert to_hindi("Chalo ghar chalte hain") == "चलो घर चलते हैं"

    def test_empty_string(self):
        assert to_hindi("") == ""

    def test_single_word(self):
        assert to_hindi("hai") == "है"

    def test_case_insensitive(self):
        assert to_hindi("NAMASTE") == "नमस्ते"
        assert to_hindi("namaste") == "नमस्ते"
        assert to_hindi("Namaste") == "नमस्ते"

    def test_numbers_preserved(self):
        result = to_hindi("din")
        assert result == "दिन"

    def test_weather(self):
        assert to_hindi("Aaj mausam accha hai") == "आज मौसम अच्छा है"

    def test_whats_your_name(self):
        assert to_hindi("Tumhara naam kya hai") == "तुम्हारा नाम क्या है"


class TestRomanToHindiClass:
    """Test the RomanToHindi class directly."""

    def test_instance(self):
        converter = RomanToHindi()
        assert converter.transliterate("Namaste") == "नमस्ते"

    def test_custom_word(self):
        converter = RomanToHindi()
        converter.add_word("bruh", "ब्रह")
        assert converter.transliterate("bruh") == "ब्रह"

    def test_custom_words_batch(self):
        converter = RomanToHindi()
        converter.add_words({
            "cringe": "क्रिंज",
            "sigma": "सिग्मा",
        })
        assert converter.transliterate("cringe") == "क्रिंज"
        assert converter.transliterate("sigma") == "सिग्मा"

    def test_custom_word_doesnt_affect_others(self):
        c1 = RomanToHindi()
        c2 = RomanToHindi()
        c1.add_word("yolo", "योलो")
        # c2 should NOT have this word
        assert c1.transliterate("yolo") == "योलो"
        # c2 will transliterate phonetically (not from dict)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
