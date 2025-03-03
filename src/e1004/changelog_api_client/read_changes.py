import argparse

from .cli_client import create_client


def run(args: argparse.Namespace) -> None:
    version_number = args.version_number

    print(create_client().read_changes(version_number))


def add_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser("read-changes", help="Read changes.")
    parser.add_argument("version_number", help="'major.minor.patch'")

    parser.set_defaults(func=run)
