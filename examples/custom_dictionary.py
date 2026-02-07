"""
Custom Dictionary Example — hinlang
======================================

Demonstrates adding custom words to the transliterator.
"""

from hinlang import RomanToHindi, HindiToRoman

print("=" * 60)
print("  hinlang — Custom Dictionary Example")
print("=" * 60)
print()

# ── Add custom slang / internet words ──
r2h = RomanToHindi()

# Add single word
r2h.add_word("bruh", "ब्रह")
r2h.add_word("vibe", "वाइब")

# Add multiple at once
r2h.add_words({
    "cringe":   "क्रिंज",
    "lowkey":   "लोकी",
    "sigma":    "सिग्मा",
    "noob":     "नूब",
    "pro":      "प्रो",
    "gg":       "जीजी",
    "lol":      "लोल",
    "bestie":   "बेस्टी",
    "slay":     "स्ले",
    "rizz":     "रिज़",
})

print("▶ Custom words (Roman → Hindi):")
print()

sentences = [
    "Bruh kya vibe hai",
    "Sigma grindset hai bhai",
    "Bestie tu slay kar rahi hai",
    "Noob player hai wo",
    "Pro move tha yeh",
    "Lol bohot cringe tha",
]

for s in sentences:
    print(f"  {s}")
    print(f"  → {r2h.transliterate(s)}")
    print()

# ── Reverse: add custom Hindi words ──
h2r = HindiToRoman()

h2r.add_words({
    "ब्रह":   "bruh",
    "वाइब":   "vibe",
    "क्रिंज":  "cringe",
    "सिग्मा":  "sigma",
    "नूब":    "noob",
    "प्रो":    "pro",
    "लोल":    "lol",
    "बेस्टी":  "bestie",
})

print("▶ Custom words (Hindi → Roman):")
print()

hindi_sentences = [
    "ब्रह क्या वाइब है",
    "सिग्मा है भाई",
    "लोल बहुत क्रिंज था",
]

for s in hindi_sentences:
    print(f"  {s}")
    print(f"  → {h2r.transliterate(s)}")
    print()

print("Done! ✨")
