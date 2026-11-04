
# ASSESSMENT 3.2 - ARRAY
# Last Name: ANTIDO

def main():
    A = []

    print("=== ARRAY OPERATIONS ===")
    print("Adding letters...")

    letters = ["A", "N", "T", "I", "D", "O"]

    for letter in letters:
        A.append(letter)
        print("Added:", letter)

    print("\nArray:", A)

    print("\nRemoving letters from the end...")

    while len(A) > 0:
        removed = A.pop()
        print("Removed:", removed)
        print("Remaining Array:", A)

    print("\nArray is now empty:", A)


if __name__ == "__main__":
    main()
