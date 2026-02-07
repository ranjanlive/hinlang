"""
Basic Usage Example — hinlang
==============================

Demonstrates the simplest way to use hinlang for
Hinglish ↔ Hindi transliteration.
"""

import hinlang

print("=" * 60)
print("  hinlang — Basic Usage Example")
print("=" * 60)
print()

# ── Roman to Hindi ──
print("▶ Roman → Devanagari:")
print()

texts = [
    "Namaste Dosto",
    "Kya haal hai",
    "Mera naam Ranjan hai",
    "Main theek hoon",
    "Bahut accha kaam kiya",
    "Aap kaise ho",
    "Shukriya dost",
]

for text in texts:
    hindi = hinlang.to_hindi(text)
    print(f"  {text:35s}  →  {hindi}")

print()

# ── Hindi to Roman ──
print("▶ Devanagari → Roman:")
print()

hindi_texts = [
    "नमस्ते दोस्तो",
    "क्या हाल है",
    "मेरा नाम रंजन है",
    "मैं ठीक हूँ",
    "बहुत अच्छा काम किया",
    "आप कैसे हो",
    "शुक्रिया दोस्त",
]

for text in hindi_texts:
    roman = hinlang.to_roman(text)
    print(f"  {text:35s}  →  {roman}")

print()

# ── Auto-detect ──
print("▶ Auto-detect (convert):")
print()

mixed = [
    "Hello Dosto",
    "नमस्ते दोस्तो",
    "Kya haal hai",
    "क्या हाल है",
]

for text in mixed:
    result = hinlang.convert(text)
    script = hinlang.detect_script(text)
    print(f"  [{script:11s}] {text:25s}  →  {result}")

print()
print("Done! ✨")
