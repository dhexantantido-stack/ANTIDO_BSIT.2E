
# ASSESSMENT 3.2 - STACK (LIFO)
# Last Name: ANTIDO

def main():
    S = []

    letters = ["A", "N", "T", "I", "D", "O"]

    print("=== STACK OPERATIONS ===")
    print("Pushing letters...")

    for letter in letters:
        S.append(letter)
        print("Pushed:", letter)

    print("\nStack:", S)

    print("\nPopping letters (LIFO)...")

    while len(S) > 0:
        removed = S.pop()
        print("Popped:", removed)
        print("Remaining Stack:", S)

    print("\nStack is now empty:", S)


if __name__ == "__main__":
    main()
