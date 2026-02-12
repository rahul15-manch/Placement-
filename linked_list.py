class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, n):
        for i in range(n):
            val = int(input("Enter the value: "))
            new_node = Node(val)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    # Insert at index
    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete at index
    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(index - 1):
            if temp.next is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Index out of range")
            return

        temp.next = temp.next.next

    # Print Linked List
    def print_list(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- Main Program ---------------- #

ll = LinkedList()

n = int(input("Enter the length of linked list: "))
ll.create(n)

while True:
    print("\nLinked List Menu")
    print("1. Insert element at index")
    print("2. Delete element at index")
    print("3. Print Linked List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        index = int(input("Enter index: "))
        value = int(input("Enter value: "))
        ll.insert_at_index(index, value)

    elif choice == 2:
        index = int(input("Enter index to delete: "))
        ll.delete_at_index(index)

    elif choice == 3:
        ll.print_list()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


