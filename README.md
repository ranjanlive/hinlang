# hinlangpy

> **Hinglish ↔ Hindi Transliterator for Python**

Convert between Roman Hindi (Hinglish) and Devanagari script effortlessly.

```
pip install hinlangpy
```

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## ✨ Features

- 🔤 **Roman → Devanagari** — `"Namaste Dosto"` → `"नमस्ते दोस्तो"`
- 🔡 **Devanagari → Roman** — `"नमस्ते दोस्तो"` → `"namaste dosto"`
- 📖 **500+ word dictionary** for accurate common word translation
- ⚡ **Character-level transliteration** for unknown/new words
- 🔁 **Round-trip accurate** — convert back and forth reliably
- 🧩 **Auto-detection** — automatically detects input script
- 📦 **Zero dependencies** — pure Python, no external packages
- 🐍 **Python 3.7+** compatible
- 💻 **CLI tool included** — use directly from terminal

---

## 📦 Installation

```bash
pip install hinlangpy
```

Or install from source:

```bash
git clone https://github.com/ranjanlive/hinlang.git
cd hinlang
pip install -e .
```

---

## 🚀 Quick Start

### Basic Usage

```python
import hinlang

# Roman to Devanagari
hindi = hinlang.to_hindi("Namaste Dosto")
print(hindi)  # नमस्ते दोस्तो

# Devanagari to Roman
roman = hinlang.to_roman("नमस्ते दोस्तो")
print(roman)  # namaste dosto

# Auto-detect and convert
result = hinlang.convert("Kya haal hai")
print(result)  # क्या हाल है

result = hinlang.convert("क्या हाल है")
print(result)  # kya haal hai
```

### Using Classes Directly

```python
from hinlang import RomanToHindi, HindiToRoman

# Roman → Hindi
r2h = RomanToHindi()
print(r2h.transliterate("Mera naam Ranjan hai"))
# मेरा नाम रंजन है

# Hindi → Roman
h2r = HindiToRoman()
print(h2r.transliterate("मेरा नाम रंजन है"))
# mera naam ranjan hai
```

### Batch Translation

```python
import hinlang

sentences = [
    "Aap kaise ho",
    "Main theek hoon",
    "Bahut accha kaam kiya",
    "Shukriya dost",
]

# Convert all at once
results = hinlang.to_hindi_batch(sentences)
for original, converted in zip(sentences, results):
    print(f"{original}  →  {converted}")
```

Output:
```
Aap kaise ho  →  आप कैसे हो
Main theek hoon  →  मैं ठीक हूँ
Bahut accha kaam kiya  →  बहुत अच्छा काम किया
Shukriya dost  →  शुक्रिया दोस्त
```

### Script Detection

```python
import hinlang

print(hinlang.detect_script("Hello Dosto"))     # "roman"
print(hinlang.detect_script("नमस्ते दोस्तो"))     # "devanagari"
print(hinlang.detect_script("Hello दोस्तो"))     # "mixed"
```

### Custom Dictionary

```python
from hinlang import RomanToHindi

converter = RomanToHindi()

# Add your own word mappings
converter.add_word("bruh", "ब्रह")
converter.add_word("vibe", "वाइब")
converter.add_words({
    "cringe": "क्रिंज",
    "lowkey": "लोकी",
    "sigma":  "सिग्मा",
})

print(converter.transliterate("Bruh kya vibe hai"))
# ब्रह क्या वाइब है
```

---

## 💻 CLI Usage

```bash
# Roman to Hindi
hinlangpy "Namaste Dosto"
# Output: नमस्ते दोस्तो

# Hindi to Roman
hinlangpy "नमस्ते दोस्तो"
# Output: namaste dosto

# Specify direction explicitly
hinlangpy --to-hindi "Kya haal hai"
hinlangpy --to-roman "क्या हाल है"

# Interactive mode
hinlangpy --interactive

# Translate a file
hinlangpy --file input.txt --output output.txt

# Pipe support
echo "Namaste Dosto" | hinlangpy
```

---

## 📚 API Reference

### Module-Level Functions

| Function | Description |
|----------|-------------|
| `hinlang.to_hindi(text)` | Convert Roman text to Devanagari |
| `hinlang.to_roman(text)` | Convert Devanagari text to Roman |
| `hinlang.convert(text)` | Auto-detect script and convert to the other |
| `hinlang.to_hindi_batch(list)` | Convert a list of Roman strings to Hindi |
| `hinlang.to_roman_batch(list)` | Convert a list of Hindi strings to Roman |
| `hinlang.detect_script(text)` | Detect script: `"roman"`, `"devanagari"`, or `"mixed"` |

> **Note:** Install with `pip install hinlangpy`, import as `import hinlang`.

### Classes

#### `RomanToHindi`

```python
from hinlang import RomanToHindi

converter = RomanToHindi()
result = converter.transliterate("Namaste Dosto")

# Custom words
converter.add_word("key", "value")
converter.add_words({"key1": "val1", "key2": "val2"})
```

#### `HindiToRoman`

```python
from hinlang import HindiToRoman

converter = HindiToRoman()
result = converter.transliterate("नमस्ते दोस्तो")

# Custom words
converter.add_word("key", "value")
converter.add_words({"key1": "val1", "key2": "val2"})
```

---

## 🗺️ Transliteration Guide

| Roman | Devanagari | Example |
|-------|-----------|---------|
| a | अ | `amar` → `अमर` |
| aa | आ | `aap` → `आप` |
| i | इ | `is` → `इस` |
| ee | ई | `eel` → `ईल` |
| u | उ | `upar` → `उपर` |
| oo | ऊ | `ooncha` → `ऊंचा` |
| e | ए | `ek` → `एक` |
| ai | ऐ | `aisa` → `ऐसा` |
| o | ओ | `om` → `ॐ` |
| au | औ | `aur` → `और` |
| k | क | `kal` → `कल` |
| kh | ख | `khat` → `खत` |
| g | ग | `ghar` → `घर` |
| gh | घ | `ghee` → `घी` |
| ch | च | `chai` → `चाय` |
| chh | छ | `chhota` → `छोटा` |
| j | ज | `jab` → `जब` |
| jh | झ | `jhooth` → `झूठ` |
| t | त | `tab` → `तब` |
| th | थ | `theek` → `ठीक` |
| d | द | `din` → `दिन` |
| dh | ध | `dhan` → `धन` |
| n | न | `naam` → `नाम` |
| p | प | `paani` → `पानी` |
| ph | फ | `phir` → `फिर` |
| b | ब | `bas` → `बस` |
| bh | भ | `bhai` → `भाई` |
| m | म | `maa` → `माँ` |
| y | य | `yahan` → `यहाँ` |
| r | र | `raat` → `रात` |
| l | ल | `log` → `लोग` |
| v/w | व | `woh` → `वो` |
| sh | श | `shaam` → `शाम` |
| s | स | `sab` → `सब` |
| h | ह | `hai` → `है` |
| z | ज़ | `zindagi` → `ज़िंदगी` |

---

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run with verbose
python -m pytest tests/ -v

# Quick test (package is 'hinlangpy' on PyPI, import as 'hinlang')
python -c "import hinlang; print(hinlang.to_hindi('Namaste Dosto'))"
```

---

## 📁 Project Structure

```
hinlang/
├── hinlang/
│   ├── __init__.py          # Public API & convenience functions
│   ├── roman_to_hindi.py    # Roman → Devanagari engine
│   ├── hindi_to_roman.py    # Devanagari → Roman engine
│   ├── detector.py          # Script detection utility
│   ├── dictionary.py        # Word dictionaries (500+ words)
│   └── cli.py               # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_roman_to_hindi.py
│   ├── test_hindi_to_roman.py
│   ├── test_roundtrip.py
│   └── test_detector.py
├── examples/
│   ├── basic_usage.py
│   ├── batch_convert.py
│   └── custom_dictionary.py
├── docs/
│   └── TRANSLITERATION_GUIDE.md
├── setup.py
├── setup.cfg
├── pyproject.toml
├── MANIFEST.in
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Add your changes and tests
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Adding New Words

The easiest way to contribute is by adding words to the dictionary:

```python
# In hinlang/dictionary.py, add to ROMAN_TO_HINDI dict:
'yourword': 'देवनागरी',
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Credits

- Built with ❤️ for the Hindi-speaking developer community
- Inspired by the need for a simple, offline, dependency-free Hindi transliterator

---

**Made with ❤️ in India 🇮🇳**
