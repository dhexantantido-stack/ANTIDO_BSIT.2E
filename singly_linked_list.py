
# ASSESSMENT 3.2 - SINGLY LINKED LIST
# Last Name: ANTIDO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("NULL")


def main():
    head = None
    tail = None

    letters = ["A", "N", "T", "I", "D", "O"]

    print("=== SINGLY LINKED LIST ===")
    print("Adding letters...")

    for letter in letters:
        new_node = Node(letter)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        print("Added:", letter)

    print("\nLinked List:")
    display(head)

    print("\nRemoving nodes from the head...")

    while head is not None:
        removed = head.data
        head = head.next

        print("Removed:", removed)
        print("Remaining List:")
        display(head)

    print("\nLinked List is now empty.")


if __name__ == "__main__":
    main()
