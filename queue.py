
# ASSESSMENT 3.2 - QUEUE (FIFO)
# Last Name: ANTIDO

from collections import deque

def main():
    Q = deque()

    letters = list(input("Enter letters (press Enter for ANTIDO): ").strip().upper() or "ANTIDO")

    print("=== QUEUE OPERATIONS ===")
    print("Enqueuing letters...")

    for letter in letters:
        Q.append(letter)
        print("Enqueued:", letter)

    print("\nQueue:", list(Q))

    print("\nDequeuing letters (FIFO)...")

    while len(Q) > 0:
        removed = Q.popleft()
        print("Dequeued:", removed)
        print("Remaining Queue:", list(Q))

    print("\nQueue is now empty:", list(Q))


if __name__ == "__main__":
    main()
