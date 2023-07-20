def my_list():
    divisible = []
    remining = []
    while True:
        number = int(input("enter non negative integer, any negative to stop "))
        if number < 0:
            break
        elif (number % 3) == 0 and (number % 2) == 0:
            divisible.append(number)
        else:
            remining.append(number)

    print("the elements that are multiple if 3 and 2: ", divisible)
    print("the remaining elements: ", remining)


my_list()
