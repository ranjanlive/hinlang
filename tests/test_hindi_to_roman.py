"""Tests for Hindi → Roman transliteration."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hinlang import to_roman, HindiToRoman


class TestToRoman:
    """Test the to_roman() convenience function."""

    def test_greeting(self):
        assert to_roman("नमस्ते दोस्तो") == "namaste dosto"

    def test_hello(self):
        assert to_roman("हेलो दोस्तो") == "hello dosto"

    def test_question(self):
        assert to_roman("क्या हाल है") == "kya haal hai"

    def test_name_sentence(self):
        assert to_roman("मेरा नाम रंजन है") == "mera naam ranjan hai"

    def test_how_are_you(self):
        assert to_roman("आप कैसे हो") == "aap kaise ho"

    def test_im_fine(self):
        assert to_roman("मैं ठीक हूँ") == "main theek hoon"

    def test_good_work(self):
        assert to_roman("बहुत अच्छा काम किया") == "bahut accha kaam kiya"

    def test_need_water(self):
        assert to_roman("मुझे पानी चाहिए") == "mujhe paani chahiye"

    def test_where_going(self):
        assert to_roman("कहां जा रहे हो") == "kahaan ja rahe ho"

    def test_lets_go_home(self):
        assert to_roman("चलो घर चलते हैं") == "chalo ghar chalte hain"

    def test_beautiful_life(self):
        assert to_roman("ज़िंदगी बहुत खूबसूरत है") == "zindagi bahut khubsoorat hai"

    def test_your_name(self):
        assert to_roman("तुम्हारा नाम क्या है") == "tumhara naam kya hai"

    def test_weather(self):
        assert to_roman("आज मौसम अच्छा है") == "aaj mausam accha hai"

    def test_heartfelt_thanks(self):
        assert to_roman("दिल से शुक्रिया") == "dil se shukriya"

    def test_morning(self):
        assert to_roman("सुबह हो गयी") == "subah ho gayi"

    def test_meet_tonight(self):
        assert to_roman("रात को मिलते हैं") == "raat ko milte hain"

    def test_empty(self):
        assert to_roman("") == ""

    def test_single_word(self):
        assert to_roman("है") == "hai"


class TestHindiToRomanClass:
    """Test the HindiToRoman class directly."""

    def test_instance(self):
        converter = HindiToRoman()
        assert converter.transliterate("नमस्ते") == "namaste"

    def test_custom_word(self):
        converter = HindiToRoman()
        converter.add_word("ब्रह", "bruh")
        assert converter.transliterate("ब्रह") == "bruh"

    def test_custom_words_batch(self):
        converter = HindiToRoman()
        converter.add_words({
            "क्रिंज": "cringe",
            "सिग्मा": "sigma",
        })
        assert converter.transliterate("क्रिंज") == "cringe"
        assert converter.transliterate("सिग्मा") == "sigma"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
