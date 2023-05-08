class calc:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


c = calc()
x = 20
y = 10
while True:
    ch = input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")
    if ch == '5':
        break

    if ch == '1':
        result = c.add(x, y)
        print("Addition:", result)
    elif ch == '2':
        result = c.sub(x, y)
        print("Subtraction:", result)
    elif ch == '3':
        result = c.sub(x, y)
        print("Subtraction:", result)
    elif ch == '4':
        result = c.sub(x, y)
        print("Subtraction:", result)
    else:
        print("invalid choice")