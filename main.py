input_ = int(input("number of records you need to enter: "))
highest_grade = 0
number_of_scores = ""
name_of_wanted_student = ""

file2 = open("youssef2.txt", "w")

for grade in range(input_):
    name = input("Please, enter your name: ")
    grade = int(input("Please, enter your grade: "))

    if highest_grade < int(grade):
        highest_grade = grade
        name_of_wanted_student = name

    name = str(name), "\n"
    grade = str(grade), "\n"

    file2.writelines(name)
    file2.writelines(grade)

file2.close()

highest_grade = "Highest score: {}".format(highest_grade)
name_of_wanted_student = "Held by: {}".format(name_of_wanted_student)
number_of_scores = "Number of scores: {}".format(str(input_))


print(highest_grade)
print(name_of_wanted_student)
print(number_of_scores)
