all = []
for _ in range(int(input("number of records you need to enter: "))):
    all.append(input("Enter the name "))
    all.append(input("Enter the grade "))


file1 = open("youssef.txt", "w")
file1.writelines("\n".join(all))
file1.close()
