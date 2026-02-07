"""
hinlangpy — Hinglish ↔ Hindi (Devanagari) Transliterator
"""

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

# Read README for long description
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hinlangpy",
    version="1.0.0",
    author="Ranjan",
    author_email="ranjan@example.com",
    description="A pure-Python Hinglish ↔ Hindi (Devanagari) transliterator. Convert Roman Hindi to Devanagari and vice versa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ranjanlive/hinlang",
    project_urls={
        "Bug Tracker": "https://github.com/ranjanlive/hinlang/issues",
        "Documentation": "https://github.com/ranjanlive/hinlang#readme",
        "Source Code": "https://github.com/ranjanlive/hinlang",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "docs"]),
    python_requires=">=3.7",
    install_requires=[],  # Zero dependencies!
    entry_points={
        "console_scripts": [
            "hinlangpy=hinlang.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Internationalization",
        "Natural Language :: Hindi",
    ],
    keywords="hindi hinglish devanagari transliteration roman unicode india",
    zip_safe=True,
)
