"""Tests for round-trip transliteration (Roman → Hindi → Roman)."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hinlang import to_hindi, to_roman


class TestRoundTrip:
    """Verify that converting Roman → Hindi → Roman gives consistent results."""

    SENTENCES = [
        "Hello Dosto",
        "Namaste Dosto",
        "Mera naam Ranjan hai",
        "Bahut accha kaam kiya",
        "Aap kaise ho",
        "Main theek hoon",
        "Kya haal hai",
        "Shukriya dost",
        "Mujhe paani chahiye",
        "Chalo ghar chalte hain",
        "Subah ho gayi",
        "Raat ko milte hain",
        "Dil se shukriya",
        "Aaj mausam accha hai",
        "Tumhara naam kya hai",
    ]

    def test_roundtrip_consistency(self):
        """Roman → Hindi → Roman should be case-insensitively equal."""
        for sentence in self.SENTENCES:
            hindi = to_hindi(sentence)
            back = to_roman(hindi)
            assert back.lower() == sentence.lower(), (
                f"Round-trip failed:\n"
                f"  Original: {sentence}\n"
                f"  Hindi:    {hindi}\n"
                f"  Back:     {back}"
            )

    def test_hindi_roundtrip(self):
        """Hindi → Roman → Hindi should give same Hindi output."""
        hindi_sentences = [
            "नमस्ते दोस्तो",
            "क्या हाल है",
            "मेरा नाम रंजन है",
            "बहुत अच्छा काम किया",
            "मुझे पानी चाहिए",
        ]
        for hindi in hindi_sentences:
            roman = to_roman(hindi)
            back = to_hindi(roman)
            assert back == hindi, (
                f"Hindi round-trip failed:\n"
                f"  Original: {hindi}\n"
                f"  Roman:    {roman}\n"
                f"  Back:     {back}"
            )


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
