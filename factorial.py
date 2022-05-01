def factorial():
    number = input("Please enter the number : ")
    b = 1
    if number == 0:
        return 1
    else:
        for i in range(1, int(number)+1):
            b = b * i
    print(b)

factorial()