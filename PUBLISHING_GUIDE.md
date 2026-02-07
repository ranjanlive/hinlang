# 📦 Publishing `hinlangpy` to PyPI - Complete Step-by-Step Guide

## 🎯 **What You'll Achieve**

After following this guide, anyone in the world can install your package with:
```bash
pip install hinlangpy
```

---

## 📋 **PART 1: Pre-Publishing Setup**

### **Step 1.1: Create PyPI Accounts**

#### A. Test PyPI (for practice)
1. Visit: https://test.pypi.org/account/register/
2. Create account with email/password
3. Verify email
4. **Enable 2FA** (Two-Factor Authentication) — REQUIRED
   - Go to Account Settings → Add 2FA
   - Use Google Authenticator or similar app

#### B. Real PyPI (for actual release)
1. Visit: https://pypi.org/account/register/
2. Create account with email/password
3. Verify email
4. **Enable 2FA** — REQUIRED for uploads
   - Same process as Test PyPI

### **Step 1.2: Generate API Tokens**

API tokens are safer than passwords for uploading.

#### For Test PyPI:
1. Login to https://test.pypi.org/
2. Go to: Account Settings → API tokens
3. Click **"Add API token"**
4. **Token name:** `hinlangpy-upload`
5. **Scope:** `Entire account` (for first upload) or `Project: hinlangpy` (after first upload)
6. Click **"Create token"**
7. **⚠️ COPY THE TOKEN NOW** — you can't see it again!
   - Format: `pypi-AgEIcHlwaS5vcmcC...` (starts with `pypi-`)
8. Save it securely (password manager recommended)

#### For Real PyPI:
1. Login to https://pypi.org/
2. Same process as above
3. Copy and save the token

---

## 📋 **PART 2: Build the Package**

### **Step 2.1: Navigate to Project**
```bash
cd D:\New_Projects\hinlang
```

### **Step 2.2: Clean Old Builds**
```bash
# Remove old build artifacts if any
rmdir /s /q dist build hinlangpy.egg-info 2>nul
```

### **Step 2.3: Build Distribution Files**
```bash
python -m build
```

This creates:
- `dist/hinlangpy-1.0.0-py3-none-any.whl` — Wheel (binary) distribution
- `dist/hinlangpy-1.0.0.tar.gz` — Source distribution

**Expected output:**
```
Successfully built hinlangpy-1.0.0.tar.gz and hinlangpy-1.0.0-py3-none-any.whl
```

### **Step 2.4: Verify Build**
```bash
dir dist
```

You should see 2 files:
- `hinlangpy-1.0.0-py3-none-any.whl`
- `hinlangpy-1.0.0.tar.gz`

---

## 📋 **PART 3: Test Upload (Test PyPI)**

**⚠️ ALWAYS test on Test PyPI first!**

### **Step 3.1: Upload to Test PyPI**
```bash
twine upload --repository testpypi dist/*
```

**You'll be prompted:**
```
Enter your username: __token__
Enter your password: [paste your Test PyPI token here]
```

**✅ Success looks like:**
```
Uploading distributions to https://test.pypi.org/legacy/
Uploading hinlangpy-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Uploading hinlangpy-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

View at:
https://test.pypi.org/project/hinlangpy/1.0.0/
```

### **Step 3.2: Test Install from Test PyPI**
```bash
# Create a test virtual environment
python -m venv test_env
test_env\Scripts\activate

# Install from Test PyPI
pip install -i https://test.pypi.org/simple/ hinlangpy

# Test it works
python -c "import hinlang; print(hinlang.to_hindi('Namaste Dosto'))"

# Should print: नमस्ते दोस्तो

# Deactivate and delete test env
deactivate
rmdir /s /q test_env
```

---

## 📋 **PART 4: Real Upload (PyPI)**

**⚠️ THIS IS PERMANENT! YOU CANNOT DELETE OR RE-UPLOAD THE SAME VERSION!**

### **Step 4.1: Final Checks**

✅ **Checklist before uploading:**
- [ ] Tests pass: `python -m pytest tests/ -v`
- [ ] README.md is complete and looks good
- [ ] Version number is correct in `setup.py` and `pyproject.toml`
- [ ] LICENSE file is included
- [ ] Test PyPI upload worked
- [ ] You've tested installing from Test PyPI

### **Step 4.2: Upload to Real PyPI**
```bash
twine upload dist/*
```

**You'll be prompted:**
```
Enter your username: __token__
Enter your password: [paste your REAL PyPI token here]
```

**✅ Success looks like:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading hinlangpy-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Uploading hinlangpy-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

View at:
https://pypi.org/project/hinlangpy/1.0.0/
```

### **Step 4.3: Verify on PyPI**

1. Visit: https://pypi.org/project/hinlangpy/
2. Check that:
   - Description renders correctly
   - Version shows `1.0.0`
   - All metadata is correct

### **Step 4.4: Test Install from Real PyPI**

**Wait 2-5 minutes** for PyPI to propagate, then:

```bash
# In a fresh terminal/environment
pip install hinlangpy

# Test it
python -c "import hinlang; print(hinlang.to_hindi('Hello Dosto'))"

# Test CLI
hinlangpy "Namaste Dosto"
```

---

## 📋 **PART 5: Post-Publishing**

### **Step 5.1: Create a Git Tag**
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### **Step 5.2: Create GitHub Release**
1. Go to your GitHub repo
2. Click **"Releases"** → **"Create a new release"**
3. Tag: `v1.0.0`
4. Title: `hinlangpy v1.0.0 - Initial Release`
5. Description:
   ```markdown
   # 🎉 hinlangpy v1.0.0 — Initial Release

   A pure-Python Hinglish ↔ Hindi (Devanagari) transliterator.

   ## Installation
   ```bash
   pip install hinlangpy
   ```

   ## Features
   - ✅ Roman → Devanagari conversion
   - ✅ Devanagari → Roman conversion
   - ✅ 500+ word dictionary
   - ✅ Auto-detection
   - ✅ CLI included
   - ✅ Zero dependencies

   ## Quick Start
   ```python
   import hinlang
   hinlang.to_hindi("Namaste Dosto")  # नमस्ते दोस्तो
   ```

   See [README](https://github.com/your-username/hinlang#readme) for full documentation.
   ```

6. Attach the dist files:
   - `hinlangpy-1.0.0-py3-none-any.whl`
   - `hinlangpy-1.0.0.tar.gz`

### **Step 5.3: Share Your Package!**

Post on:
- Reddit: r/Python, r/learnpython
- Twitter/X with #Python #Hindi #OpenSource
- LinkedIn
- Dev.to blog post

---

## 📋 **PART 6: Updating Your Package (Future Versions)**

### **For version 1.0.1, 1.1.0, 2.0.0, etc:**

1. **Update version numbers** in:
   - `setup.py` → `version="1.0.1"`
   - `pyproject.toml` → `version = "1.0.1"`
   - `hinlang/__init__.py` → `__version__ = "1.0.1"`

2. **Update CHANGELOG** (create one if needed):
   ```markdown
   # Changelog

   ## [1.0.1] - 2024-XX-XX
   ### Fixed
   - Bug fix description

   ### Added
   - New feature description

   ## [1.0.0] - 2024-XX-XX
   - Initial release
   ```

3. **Rebuild and upload:**
   ```bash
   # Clean old build
   rmdir /s /q dist build hinlangpy.egg-info

   # Build new version
   python -m build

   # Upload to Test PyPI first (always!)
   twine upload --repository testpypi dist/*

   # Test install & verify

   # Upload to Real PyPI
   twine upload dist/*
   ```

4. **Tag the release:**
   ```bash
   git tag -a v1.0.1 -m "Release version 1.0.1"
   git push origin v1.0.1
   ```

---

## 🔐 **PART 7: Security Best Practices**

### **Storing Tokens Securely**

**Option 1: Use `.pypirc` file** (recommended)

Create: `C:\Users\RANJAN\.pypirc`
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-REAL-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

**⚠️ Set file permissions to private!**

Now you can upload without typing password:
```bash
twine upload --repository testpypi dist/*   # uses testpypi token
twine upload dist/*                          # uses pypi token
```

**Option 2: Use environment variables**
```bash
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=pypi-YOUR-TOKEN-HERE
twine upload dist/*
```

**Option 3: Use keyring** (most secure)
```bash
pip install keyring
keyring set https://upload.pypi.org/legacy/ __token__
# Enter your token when prompted

# Now twine will use keyring automatically
twine upload dist/*
```

---

## ❓ **PART 8: Troubleshooting**

### **Problem: "The user '__token__' isn't allowed to upload"**
- **Solution:** Enable 2FA on your PyPI account first

### **Problem: "File already exists"**
- **Solution:** You can't re-upload the same version. Bump version to 1.0.1

### **Problem: "Invalid or non-existent authentication"**
- **Solution:** Double-check your API token. Make sure username is `__token__` (literal)

### **Problem: "Repository not found"**
- **Solution:** For Test PyPI, use: `twine upload --repository testpypi dist/*`

### **Problem: README not rendering on PyPI**
- **Solution:** Check `long_description_content_type="text/markdown"` in setup.py

### **Problem: Package installs but import fails**
- **Solution:** Check that `packages=find_packages()` in setup.py finds your package

---

## 📊 **PART 9: Package Statistics**

After publishing, you can track:
- **Downloads:** https://pypistats.org/packages/hinlangpy
- **GitHub Stats:** Stars, forks, issues
- **PyPI page:** https://pypi.org/project/hinlangpy/

---

## ✅ **Quick Reference - Full Workflow**

```bash
# 1. One-time setup
# - Create PyPI accounts (test + real)
# - Enable 2FA
# - Generate API tokens
# - Save tokens in .pypirc

# 2. Every release:
cd D:\New_Projects\hinlang

# Clean
rmdir /s /q dist build hinlangpy.egg-info

# Run tests
python -m pytest tests/ -v

# Build
python -m build

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Test install
pip install -i https://test.pypi.org/simple/ hinlangpy

# Upload to Real PyPI
twine upload dist/*

# Tag release
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Done! 🎉
```

---

## 🎓 **Resources**

- **PyPI:** https://pypi.org/
- **Test PyPI:** https://test.pypi.org/
- **Packaging Guide:** https://packaging.python.org/
- **Twine Docs:** https://twine.readthedocs.io/
- **Semantic Versioning:** https://semver.org/

---

## 🎉 **You're Ready!**

Your package `hinlangpy` is now ready to be shared with the world!

**Next command:**
```bash
cd D:\New_Projects\hinlang
python -m build
twine upload --repository testpypi dist/*
```

**Good luck! 🚀**
