# 🔐 Trusted Publishers Setup - Complete Guide

## 🎯 What is Trusted Publishers?

**Trusted Publishers** lets you publish to PyPI from GitHub Actions **WITHOUT needing API tokens**. It uses OpenID Connect (OIDC) for secure, automatic authentication.

**Benefits:**
- ✅ No API tokens to manage
- ✅ More secure (no secrets to leak)
- ✅ Automatic publishing on GitHub releases
- ✅ No manual uploads needed

---

## 📋 **Complete Setup Process**

### **STEP 1: Create GitHub Repository**

```bash
cd D:\New_Projects\hinlang

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - hinlang v1.0.0"

# Create repo on GitHub:
# Go to: https://github.com/new
# Name: hinlang
# Description: Hinglish ↔ Hindi (Devanagari) Transliterator
# Public/Private: Your choice
# Don't initialize with README (you already have one)

# Add remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/hinlang.git

# Push
git branch -M main
git push -u origin main
```

---

### **STEP 2: Create GitHub Environment**

This is **optional but STRONGLY RECOMMENDED** for security.

1. Go to your repo: `https://github.com/YOUR-USERNAME/hinlang`
2. Click **Settings** → **Environments**
3. Click **New environment**
4. Name: `pypi` (exactly this name!)
5. Click **Configure environment**
6. **Protection rules** (recommended):
   - ✅ **Required reviewers:** Add yourself
   - ✅ **Wait timer:** 0 minutes
   - ✅ **Prevent self-review:** Unchecked (you're solo)
7. Click **Save protection rules**

**Why?** This ensures only authorized releases trigger PyPI uploads.

---

### **STEP 3: Configure PyPI Trusted Publisher**

#### **Option A: For EXISTING Project (if you already uploaded manually)**

1. Go to: https://pypi.org/manage/project/hinlangpy/settings/publishing/
2. Scroll to **"Add a new publisher"**
3. Select **GitHub** tab
4. Fill in:
   ```
   Owner: YOUR-GITHUB-USERNAME (e.g., ranjanlive)
   Repository name: hinlang
   Workflow name: publish.yml
   Environment name: pypi (optional but recommended)
   ```
5. Click **Add**

#### **Option B: For NEW Project (if you haven't uploaded yet) — PENDING PUBLISHER**

1. Go to: https://pypi.org/manage/account/publishing/
2. Scroll to **"Add a new pending publisher"**
3. Select **GitHub** tab
4. Fill in:
   ```
   PyPI Project Name: hinlangpy
   Owner: YOUR-GITHUB-USERNAME (e.g., ranjanlive)
   Repository name: hinlang
   Workflow name: publish.yml
   Environment name: pypi (optional but recommended)
   ```
5. Click **Add**

**⚠️ IMPORTANT:** This does NOT reserve the name! Anyone can still create `hinlangpy` on PyPI. The "pending publisher" will only activate when YOUR workflow creates the project for the first time.

---

### **STEP 4: Verify Workflow File Exists**

Check that you have: `D:\New_Projects\hinlang\.github\workflows\publish.yml`

This file should look like:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write  # Required for trusted publishing
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Build
        run: |
          pip install build
          python -m build
      - name: Publish
        uses: pypa/gh-action-pypi-publish@release/v1
```

✅ **Already created for you at:** `D:\New_Projects\hinlang\.github\workflows\publish.yml`

---

### **STEP 5: Push Workflow to GitHub**

```bash
cd D:\New_Projects\hinlang

# Add the workflow file
git add .github/

# Commit
git commit -m "Add GitHub Actions publishing workflow"

# Push
git push origin main
```

---

### **STEP 6: Create a GitHub Release (This Triggers Publishing)**

#### **Via GitHub Web UI:**

1. Go to: `https://github.com/YOUR-USERNAME/hinlang`
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. **Choose a tag:** `v1.0.0` (create new tag)
5. **Target:** `main`
6. **Release title:** `hinlangpy v1.0.0 - Initial Release`
7. **Description:**
   ```markdown
   ## 🎉 hinlangpy v1.0.0 - Initial Release
   
   A pure-Python Hinglish ↔ Hindi (Devanagari) transliterator.
   
   ### Installation
   ```bash
   pip install hinlangpy
   ```
   
   ### Features
   - ✅ Roman → Devanagari conversion
   - ✅ Devanagari → Roman conversion
   - ✅ 500+ word dictionary
   - ✅ Auto-detection
   - ✅ CLI included
   - ✅ Zero dependencies
   
   ### Quick Start
   ```python
   import hinlang
   hinlang.to_hindi("Namaste Dosto")  # नमस्ते दोस्तो
   ```
   ```
8. **Attach binaries** (optional):
   - Upload `dist/hinlangpy-1.0.0-py3-none-any.whl`
   - Upload `dist/hinlangpy-1.0.0.tar.gz`
9. ✅ Check **"Set as the latest release"**
10. Click **Publish release**

#### **Via Git Command Line:**

```bash
cd D:\New_Projects\hinlang

# Create tag
git tag -a v1.0.0 -m "Release v1.0.0"

# Push tag
git push origin v1.0.0

# Then create release on GitHub web UI using this tag
```

---

### **STEP 7: Watch the Magic Happen!**

1. Go to: `https://github.com/YOUR-USERNAME/hinlang/actions`
2. You'll see **"Publish to PyPI"** workflow running
3. Click on it to watch progress
4. Steps:
   - ✅ Checkout code
   - ✅ Setup Python
   - ✅ Install dependencies
   - ✅ Run tests
   - ✅ Build package
   - ✅ **Publish to PyPI** (no token needed!)

5. After 2-5 minutes, check: https://pypi.org/project/hinlangpy/

**🎉 YOUR PACKAGE IS NOW LIVE!**

```bash
pip install hinlang
```

---

## 🔄 **Publishing Future Versions**

### **For version 1.0.1, 1.1.0, etc:**

```bash
cd D:\New_Projects\hinlang

# 1. Update version in 3 places:
# - setup.py → version="1.0.1"
# - pyproject.toml → version = "1.0.1"  
# - hinlang/__init__.py → __version__ = "1.0.1"

# 2. Commit changes
git add .
git commit -m "Bump version to 1.0.1"
git push

# 3. Create new release on GitHub
# Go to: https://github.com/YOUR-USERNAME/hinlang/releases/new
# Tag: v1.0.1
# Title: hinlangpy v1.0.1
# Click "Publish release"

# 4. GitHub Actions automatically publishes to PyPI!
```

**That's it!** No manual building or uploading needed.

---

## 📊 **Workflow File Breakdown**

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]    # Triggers when you publish a GitHub release
  workflow_dispatch:       # Allows manual trigger from Actions tab

permissions:
  contents: read

jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    
    environment:
      name: pypi            # Uses the "pypi" environment you created
      url: https://pypi.org/p/hinlangpy
    
    permissions:
      id-token: write       # 🔐 KEY: Enables OIDC authentication
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install build twine pytest
      
      - name: Run tests
        run: |
          pip install -e .
          pytest tests/ -v
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        # 🔐 No token needed! OIDC handles authentication
```

---

## 🆚 **Trusted Publishers vs API Tokens**

| Feature | Trusted Publishers | API Tokens |
|---------|-------------------|------------|
| **Setup** | One-time config on PyPI | Generate token, store as secret |
| **Security** | Very secure (no secrets) | Secure if stored properly |
| **Rotation** | Automatic | Manual |
| **Revocation** | Easy (remove publisher) | Manual (regenerate token) |
| **Audit** | GitHub Actions logs | Limited |
| **Best for** | Automated CI/CD | Manual uploads, testing |

**Recommendation:** Use **Trusted Publishers** for production, **API tokens** for testing.

---

## 🔍 **Troubleshooting**

### **Problem: "Trusted publisher not configured"**

**Solution:**
1. Check you configured the publisher on PyPI correctly
2. Verify the `environment: name: pypi` in your workflow matches what you configured
3. Make sure `permissions: id-token: write` is present

### **Problem: "Environment protection rules failed"**

**Solution:**
- Go to repo Settings → Environments → pypi
- Check/adjust protection rules
- Make sure you're an authorized reviewer

### **Problem: "Workflow doesn't trigger"**

**Solution:**
1. Make sure workflow file is pushed to GitHub
2. Check it's in `.github/workflows/publish.yml`
3. Trigger manually: Actions tab → "Publish to PyPI" → "Run workflow"

### **Problem: "Tests fail in workflow"**

**Solution:**
- Run tests locally first: `pytest tests/ -v`
- Check workflow logs for specific error
- Fix tests, commit, and re-release

---

## ✅ **Quick Checklist**

- [ ] GitHub repository created
- [ ] `.github/workflows/publish.yml` file exists
- [ ] Workflow file pushed to GitHub
- [ ] PyPI trusted publisher configured (or pending)
- [ ] GitHub environment `pypi` created (optional)
- [ ] Ready to create first release

---

## 🎯 **Your Current Setup**

Based on your PyPI form:

```yaml
PyPI Project Name: hinlangpy
Owner: ranjanlive
Repository name: hinlang  
Workflow name: publish.yml  
Environment name: pypi
```

**Your workflow file location:**
```
D:\New_Projects\hinlang\.github\workflows\publish.yml
```

✅ **File created!** Now:

1. **Push to GitHub:**
   ```bash
   cd D:\New_Projects\hinlang
   git add .github/
   git commit -m "Add publishing workflow"
   git push
   ```

2. **Configure on PyPI:**
   - Go to: https://pypi.org/manage/account/publishing/
   - Add pending publisher with your details

3. **Create release:**
   - GitHub → Releases → New release
   - Tag: `v1.0.0`
   - Publish

4. **Watch it publish automatically!**

---

## 📚 **Resources**

- **PyPI Trusted Publishers:** https://docs.pypi.org/trusted-publishers/
- **GitHub OIDC:** https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- **PyPI Publishing Action:** https://github.com/marketplace/actions/pypi-publish

---

## 🎉 **You're All Set!**

Your workflow file is ready at:
```
D:\New_Projects\hinlang\.github\workflows\publish.yml
```

**Next steps:**
1. Push to GitHub
2. Configure PyPI trusted publisher
3. Create release
4. Done! 🚀

**No more manual uploads ever again!** 🎊
