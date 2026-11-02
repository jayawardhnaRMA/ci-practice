"""Small command line program for the ci-practice project."""

import argparse

from cleaner import average, clean_name, remove_duplicates
from version import __version__


def run_demo():
    names = ["  alice ", "BOB", "alice", "  carol   ann  "]
    cleaned = [clean_name(n) for n in names]
    print("Names:            ", names)
    print("Cleaned names:    ", cleaned)
    print("Without duplicates:", remove_duplicates(cleaned))

    scores = [80, 90, 100]
    print("Scores:           ", scores)
    print("Average score:    ", average(scores))


def main():
    parser = argparse.ArgumentParser(description="ci-practice demo program")
    parser.add_argument(
        "--version",
        action="version",
        version=f"ci-practice version {__version__}",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="show a short demo of the cleaner functions",
    )
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
