#!/usr/bin/env python3
"""L-ZIP CLI-only entry (no GUI imports)."""

import sys
from cli import LZIPCLI


def main() -> None:
    cli = LZIPCLI()

    if len(sys.argv) > 1:
        cmd = " ".join(sys.argv[1:])
        cli.run_single_command(cmd)
    elif not sys.stdin.isatty():
        try:
            piped_input = sys.stdin.read().strip()
            if piped_input:
                cli.run_single_command(piped_input)
            else:
                cli.run_interactive()
        except Exception as exc:
            print(f"Error reading piped input: {exc}")
            cli.run_interactive()
    else:
        cli.run_interactive()


if __name__ == "__main__":
    main()
