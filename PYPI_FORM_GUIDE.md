# 📋 PyPI Trusted Publisher - Form Fill Guide

## 🎯 What to Enter on PyPI

When you go to: **https://pypi.org/manage/account/publishing/**

And click **"Add a new pending publisher"** → **GitHub** tab:

---

## ✍️ **Form Fields (Copy These Exactly)**

```
┌─────────────────────────────────────────────────────────┐
│  Add a new pending publisher - GitHub                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  PyPI Project Name: (required)                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │ hinlangpy                                         │ │
│  └───────────────────────────────────────────────────┘ │
│  The project that will be created on PyPI             │
│                                                         │
│  Owner: (required)                                     │
│  ┌───────────────────────────────────────────────────┐ │
│  │ ranjanlive                                        │ │
│  └───────────────────────────────────────────────────┘ │
│  Your GitHub username or organization                 │
│                                                         │
│  Repository name: (required)                           │
│  ┌───────────────────────────────────────────────────┐ │
│  │ hinlang                                           │ │
│  └───────────────────────────────────────────────────┘ │
│  The name of your GitHub repository                   │
│                                                         │
│  Workflow name: (required)                             │
│  ┌───────────────────────────────────────────────────┐ │
│  │ publish.yml                                       │ │
│  └───────────────────────────────────────────────────┘ │
│  Filename in .github/workflows/ directory             │
│                                                         │
│  Environment name: (optional)                          │
│  ┌───────────────────────────────────────────────────┐ │
│  │ pypi                                              │ │
│  └───────────────────────────────────────────────────┘ │
│  GitHub Actions environment for publishing            │
│                                                         │
│           [ Add ]                                      │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 **Field-by-Field Explanation**

### 1. **PyPI Project Name**
```
hinlangpy
```
- This is the name people will use: `pip install hinlangpy`
- Must match `name="hinlangpy"` in your `setup.py`
- **⚠️ Case-sensitive!**

### 2. **Owner**
```
ranjanlive
```
- Your GitHub username (or organization)
- Found at: `https://github.com/ranjanlive`
- **⚠️ Must be exact!**

### 3. **Repository name**
```
hinlang
```
- The GitHub repo name
- Found at: `https://github.com/ranjanlive/hinlang`
- **⚠️ Case-sensitive!**

### 4. **Workflow name**
```
publish.yml
```
- The filename (not full path!)
- ✅ Already created at: `D:\New_Projects\hinlang\.github\workflows\publish.yml`
- PyPI looks for: `.github/workflows/publish.yml` in your repo
- **⚠️ Must match filename exactly!**

### 5. **Environment name** (OPTIONAL)
```
pypi
```
- The GitHub environment name
- Leave **blank** if not using environments
- Use `pypi` for better security
- Must match `environment: name: pypi` in your workflow

---

## 🔍 **How PyPI Verifies It**

When you create a GitHub release and the workflow runs:

1. ✅ GitHub Actions requests PyPI access via OIDC
2. ✅ PyPI checks:
   - Is this from `github.com/ranjanlive/hinlang`?
   - Is it using workflow `publish.yml`?
   - Is it from environment `pypi` (if specified)?
3. ✅ If all match → **AUTHORIZED** → Package published!

**No API tokens needed!** 🎉

---

## 📂 **Your Current File Structure**

```
D:\New_Projects\hinlang\
├── .github\
│   └── workflows\
│       └── publish.yml         ← PyPI looks for this!
├── hinlang\
│   ├── __init__.py
│   ├── cli.py
│   ├── detector.py
│   ├── dictionary.py
│   ├── hindi_to_roman.py
│   └── roman_to_hindi.py
├── tests\
│   └── ...
├── dist\
│   ├── hinlangpy-1.0.0-py3-none-any.whl
│   └── hinlangpy-1.0.0.tar.gz
├── setup.py
├── pyproject.toml
└── README.md
```

✅ **Everything is ready!**

---

## 🎬 **Step-by-Step Actions (Visual)**

### **STEP 1: Create GitHub Repo**

```
GitHub → New Repository
┌────────────────────────────────────┐
│ Repository name: hinlang           │
│ Description: Hinglish ↔ Hindi      │
│ Public ✓ or Private                │
│ [ Create repository ]              │
└────────────────────────────────────┘
```

### **STEP 2: Push Your Code**

```bash
cd D:\New_Projects\hinlang
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ranjanlive/hinlang.git
git push -u origin main
```

### **STEP 3: Create Environment (Optional)**

```
GitHub Repo → Settings → Environments → New environment
┌────────────────────────────────────┐
│ Name: pypi                         │
│ [ Configure environment ]          │
│                                    │
│ Protection rules:                  │
│ ☑ Required reviewers               │
│ [ Save protection rules ]          │
└────────────────────────────────────┘
```

### **STEP 4: Configure PyPI Trusted Publisher**

```
PyPI.org → Account Settings → Publishing
┌────────────────────────────────────┐
│ Add a new pending publisher        │
│ [GitHub] [GitLab] [Google] [...   ]│
│                                    │
│ PyPI Project Name: hinlangpy       │
│ Owner: ranjanlive                  │
│ Repository: hinlang                │
│ Workflow: publish.yml              │
│ Environment: pypi                  │
│                                    │
│ [ Add ]                            │
└────────────────────────────────────┘
```

### **STEP 5: Create Release**

```
GitHub Repo → Releases → Create a new release
┌────────────────────────────────────┐
│ Tag: v1.0.0 (create new tag)      │
│ Target: main ▼                     │
│ Title: hinlangpy v1.0.0              │
│ Description: [your description]    │
│                                    │
│ ☑ Set as latest release            │
│ [ Publish release ]                │
└────────────────────────────────────┘
```

### **STEP 6: Watch It Publish!**

```
GitHub Repo → Actions → Publish to PyPI
┌────────────────────────────────────┐
│ ✓ Checkout code                    │
│ ✓ Setup Python                     │
│ ✓ Install dependencies             │
│ ✓ Run tests                        │
│ ✓ Build package                    │
│ ✓ Publish to PyPI                  │
└────────────────────────────────────┘

After 2-5 minutes:
https://pypi.org/project/hinlangpy/ ✅ LIVE!
```

---

## 🎯 **Quick Reference Card**

**Save this for when you fill the PyPI form:**

```
┌──────────────────────────────────────┐
│  PYPI TRUSTED PUBLISHER CONFIG       │
├──────────────────────────────────────┤
│  Project Name:    hinlangpy          │
│  Owner:           ranjanlive         │
│  Repository:      hinlang            │
│  Workflow:        publish.yml        │
│  Environment:     pypi               │
└──────────────────────────────────────┘
```

---

## ✅ **Verification Checklist**

Before submitting the form, verify:

- [ ] GitHub username is correct: `ranjanlive`
- [ ] Repository exists: `https://github.com/ranjanlive/hinlang`
- [ ] Workflow file exists: `.github/workflows/publish.yml` in repo
- [ ] Workflow file has `environment: name: pypi` (if you specified environment)
- [ ] Workflow file has `permissions: id-token: write`
- [ ] All fields are spelled EXACTLY as shown (case-sensitive!)

---

## 🆘 **Common Mistakes**

❌ **Wrong:**
```
Owner: ranjanlive.github.io     ← No!
Owner: github.com/ranjanlive    ← No!
Workflow: .github/workflows/publish.yml  ← No! (just filename)
Workflow: publish                ← No! (needs .yml)
```

✅ **Correct:**
```
Owner: ranjanlive
Workflow: publish.yml
```

---

## 🎊 **You're Ready!**

1. ✅ Workflow file created: `.github/workflows/publish.yml`
2. ✅ Form fields documented above
3. ✅ Package built: `dist/` folder
4. ✅ Tests passing: 56/56

**Next action:** Push to GitHub and configure PyPI!

```bash
cd D:\New_Projects\hinlang
git add .
git commit -m "Add GitHub Actions workflow"
git push origin main
```

Then go to: **https://pypi.org/manage/account/publishing/**

**Good luck! 🚀**
