from cli import parse_args
from cli import run_command


def main():
    args = parse_args()
    run_command(args)


if __name__ == "__main__":
    main()
