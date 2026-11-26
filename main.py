import sys
from pathlib import Path


def load_word(path=None):
    entry_path = Path(__file__).with_name("entry.txt") if path is None else Path(path)
    text = entry_path.read_text(encoding="utf-8").strip()
    return text


def validate_word(word):
    if not word:
        raise SystemExit("entry is empty")
    if len(word) > 30:
        raise SystemExit("entry exceeds 30 characters")
    if len(word.split()) != 1:
        raise SystemExit("entry must be a single word")
    return word


def main():
    word = validate_word(load_word())
    sys.stdout.write(word + "\n")


if __name__ == "__main__":
    main()
