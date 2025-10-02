import argparse
from datetime import datetime

SYSTEM_PROMPT = (
    "You are a simple local rule-based assistant. You do not access the internet.\n"
    "Keep answers short and friendly."
)

HELP_TEXT = (
    "Commands:\n"
    "  :help   Show this help\n"
    "  :quit   Exit the chat\n"
)


def reply(message: str) -> str:
    m = message.strip().lower()
    if not m:
        return "Say something, please."
    if m in {":help", "help", "/help"}:
        return HELP_TEXT
    if any(g in m for g in ["hello", "hi", "hey"]):
        return "Hello! How can I help?"
    if "time" in m:
        return f"It's {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    if "name" in m:
        return "I'm your local chat-bot."
    if m in {":quit", ":exit", "quit", "exit"}:
        return "__EXIT__"
    return "Got it. (This is a simple starter—you can extend my skills in cli.py)"


def interactive_loop() -> None:
    print("chat-bot (type :help for help, :quit to exit)\n")
    while True:
        try:
            user = input("> ")
        except EOFError:
            break
        ans = reply(user)
        if ans == "__EXIT__":
            break
        print(ans)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Minimal chat-bot CLI")
    parser.add_argument("--once", action="store_true", help="Read one line from stdin and respond once")
    args = parser.parse_args(argv)

    if args.once:
        try:
            user = input()
        except EOFError:
            user = ""
        ans = reply(user)
        if ans != "__EXIT__":
            print(ans)
        return

    interactive_loop()
