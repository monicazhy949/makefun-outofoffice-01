"""One-line AI out-of-office reply, for the make.fun bounty."""
import os

OUTPUT_PATH = "/output/entry.txt"

REPLY = (
    "I'm out of office until Monday, recharging my batteries. My "
    "auto-reply is now auto-replying to your auto-reply, so neither of "
    "us is getting anything done."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
