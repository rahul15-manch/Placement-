class Stack:
    def __init__(self, n):
        self.stack = [0] * n
        self.top = -1
        self.n = n

    def is_overflow(self):
        if self.top == self.n - 1:
            return True
        else: 
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, val):
        if self.is_overflow():
            print("No more numbers can be pushed")
        else:
            self.top += 1
            self.stack[self.top] = val
            print(val, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("No elements to pop")
        else:
            print(self.stack[self.top], "popped from stack")
            self.top -= 1

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])



n = int(input("Enter Length of Stack: "))
s = Stack(n)

while True:
    print("STACK MENU ")
    print("1. Push")
    print("2. Pop")
    print("3. Print Stack")
    print("4. Underflow Check")
    print("5. Overflow Check")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.print_stack()

    elif choice == 4:
        print(s.is_empty())

    elif choice == 5:
        print(s.is_overflow())

    elif choice == 6:
        print("Exit")
        break

    else:
        print("Invalid Operation")

