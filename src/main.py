import argparse
from pathlib import Path

from unlockdoc.unlockdoc import generate_doc

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UnLock Documentation")
    parser.add_argument("input", help="path to the main input file")
    parser.add_argument("output", help="path to the output file")
    args = parser.parse_args()
    generate_doc(args.input, args.output)
