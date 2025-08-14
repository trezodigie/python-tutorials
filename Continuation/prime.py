def is_prime():
    if num <= 1:
        print(False)
        return

    for i in range(2, num):
        if (num % i == 0):
            print(False)
            return

    print(True)

num = int(input("Please select the number you want to check: "))    
is_prime()
