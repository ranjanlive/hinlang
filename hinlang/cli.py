"""
hinlang.cli
============

Command-line interface for hinlangpy transliterator.

Usage::

    hinlangpy "Namaste Dosto"
    hinlangpy "नमस्ते दोस्तो"
    hinlangpy --to-hindi "Kya haal hai"
    hinlangpy --to-roman "क्या हाल है"
    hinlangpy --interactive
    hinlangpy --file input.txt --output output.txt
    echo "Namaste" | hinlangpy
"""

import sys
import argparse

# Fix Windows console encoding for Devanagari output
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass


def main():
    """Entry point for the ``hinlangpy`` CLI command."""
    parser = argparse.ArgumentParser(
        prog="hinlangpy",
        description="Hinglish ↔ Hindi (Devanagari) Transliterator",
        epilog="Examples:\n"
               "  hinlangpy \"Namaste Dosto\"\n"
               "  hinlangpy \"नमस्ते दोस्तो\"\n"
               "  hinlangpy --to-hindi \"Kya haal hai\"\n"
               "  hinlangpy --to-roman \"क्या हाल है\"\n"
               "  hinlangpy --interactive\n"
               "  echo \"Namaste\" | hinlangpy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "text", nargs="*", default=None,
        help="Text to transliterate (auto-detects script)"
    )
    parser.add_argument(
        "--to-hindi", "-H", dest="force_hindi", action="store_true",
        help="Force Roman → Devanagari conversion"
    )
    parser.add_argument(
        "--to-roman", "-R", dest="force_roman", action="store_true",
        help="Force Devanagari → Roman conversion"
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true",
        help="Interactive mode (type and translate line by line)"
    )
    parser.add_argument(
        "--file", "-f", dest="input_file", default=None,
        help="Input file to translate"
    )
    parser.add_argument(
        "--output", "-o", dest="output_file", default=None,
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--version", "-v", action="store_true",
        help="Show version"
    )

    args = parser.parse_args()

    # Lazy import to keep CLI fast
    import hinlang

    # Version
    if args.version:
        print(f"hinlangpy v{hinlang.__version__}")
        return

    # Interactive mode
    if args.interactive:
        _interactive_mode(hinlang)
        return

    # File mode
    if args.input_file:
        _file_mode(hinlang, args)
        return

    # Get text from args or stdin
    if args.text:
        text = ' '.join(args.text)
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        parser.print_help()
        return

    # Convert
    if args.force_hindi:
        result = hinlang.to_hindi(text)
    elif args.force_roman:
        result = hinlang.to_roman(text)
    else:
        result = hinlang.convert(text)

    # Output
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(result + '\n')
        print(f"Output written to: {args.output_file}")
    else:
        print(result)


def _interactive_mode(hinlang):
    """Interactive REPL mode."""
    print("=" * 55)
    print("  hinlangpy — Interactive Transliterator")
    print("  Type text and press Enter to translate.")
    print("  Commands: /hindi  /roman  /auto  /quit")
    print("=" * 55)
    print()

    mode = "auto"

    while True:
        try:
            prompt = f"[{mode}] > "
            text = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye! 👋")
            break

        if not text:
            continue

        # Commands
        if text.lower() == "/quit" or text.lower() == "/exit":
            print("Bye! 👋")
            break
        elif text.lower() == "/hindi":
            mode = "hindi"
            print("  Mode: Roman → Hindi (Devanagari)")
            continue
        elif text.lower() == "/roman":
            mode = "roman"
            print("  Mode: Hindi → Roman (Hinglish)")
            continue
        elif text.lower() == "/auto":
            mode = "auto"
            print("  Mode: Auto-detect")
            continue
        elif text.lower() == "/help":
            print("  /hindi  — Force Roman → Devanagari")
            print("  /roman  — Force Devanagari → Roman")
            print("  /auto   — Auto-detect input script")
            print("  /quit   — Exit")
            continue

        # Translate
        if mode == "hindi":
            result = hinlang.to_hindi(text)
        elif mode == "roman":
            result = hinlang.to_roman(text)
        else:
            result = hinlang.convert(text)

        print(f"  → {result}")
        print()


def _file_mode(hinlang, args):
    """File translation mode."""
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert
    if args.force_hindi:
        result = hinlang.to_hindi(content)
    elif args.force_roman:
        result = hinlang.to_roman(content)
    else:
        result = hinlang.convert(content)

    # Output
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Translated: {args.input_file} → {args.output_file}")
    else:
        print(result)


if __name__ == "__main__":
    main()
