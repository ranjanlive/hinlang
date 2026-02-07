"""
Batch Conversion Example — hinlang
====================================

Demonstrates converting multiple strings at once.
"""

import hinlang

print("=" * 60)
print("  hinlang — Batch Conversion")
print("=" * 60)
print()

# ── Batch: Roman → Hindi ──
roman_sentences = [
    "Namaste Dosto",
    "Aap kaise ho",
    "Main theek hoon",
    "Bahut accha kaam kiya",
    "Shukriya dost",
    "Kahan ja rahe ho",
    "Chalo ghar chalte hain",
    "Subah ho gayi",
    "Aaj mausam accha hai",
    "Zindagi bahut khubsoorat hai",
]

print(f"▶ Converting {len(roman_sentences)} sentences to Hindi...")
print()

hindi_results = hinlang.to_hindi_batch(roman_sentences)

for roman, hindi in zip(roman_sentences, hindi_results):
    print(f"  {roman}")
    print(f"  → {hindi}")
    print()

# ── Batch: Hindi → Roman ──
print("▶ Converting back to Roman...")
print()

roman_back = hinlang.to_roman_batch(hindi_results)

for hindi, roman in zip(hindi_results, roman_back):
    print(f"  {hindi}")
    print(f"  → {roman}")
    print()

print("Done! ✨")
