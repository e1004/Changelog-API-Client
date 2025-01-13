from argparse import ArgumentParser

from . import create_version, delete_version, read_versions, release_version


def main() -> None:
    parser = ArgumentParser(
        description="""CLI for Changelog API;
    before creating a changelog,
    create a project and its access key, execute 'cli_project -h'"""
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    create_version.add_parser(subparsers)
    delete_version.add_parser(subparsers)
    release_version.add_parser(subparsers)
    read_versions.add_parser(subparsers)

    args = parser.parse_args()
    if args.command in ["delete", "read"]:
        args.func()
    else:
        args.func(args)
