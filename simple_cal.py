def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def main():
    x = int(input("What's X ?"))
    y = int(input("What's y?"))
    print("The sum of X and Y is : ", + add(x + y))
    print("The difference of X and Y is :", + sub(x - y))

if __name__ == '__main__':
    main()