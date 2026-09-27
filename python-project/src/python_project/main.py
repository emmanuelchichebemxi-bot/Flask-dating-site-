"""Command-line entry point for the Python project."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="A small, well-structured Python project."
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="Name to greet (default: World).",
    )
    return parser


def greeting(name: str) -> str:
    """Return a friendly greeting for *name*."""
    cleaned_name = name.strip() or "World"
    return f"Hello, {cleaned_name}!"


def main() -> None:
    """Run the command-line application."""
    args = build_parser().parse_args()
    print(greeting(args.name))


if __name__ == "__main__":
    main()