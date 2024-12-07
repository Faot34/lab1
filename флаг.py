YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
END = '\u001b[0m'

def lithuanian_flag():
    for _ in range(3):
        print(f"{YELLOW}{'  ' * 10}{END}")
    for _ in range(3):
        print(f"{GREEN}{'  ' * 10}{END}")
    for _ in range(3):
        print(f"{RED}{'  ' * 10}{END}")

lithuanian_flag()
