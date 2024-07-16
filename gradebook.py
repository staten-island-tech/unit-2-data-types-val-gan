student = {"Name": str, "Class" : str, "Grades" : []}

def findAverage(grades):
    total = 0
    for i in grades:
        total += i
    average = total/len(grades)
    return(average)

#findAverage((99, 100))


def gradeList():
    grades = (input("Input student grades separated by a space\n")).split()
    for i in range (len(grades)):
        grades[i] = int(grades[i])
    return grades


def newStudents():
    studentList = []
    continue_adding_students = "Y"
    while continue_adding_students == "Y":
        student = {"Name": " ", "Class" : " ", "Grades" : [], "Average" : " "}
        student["Name"] = input("Input student name\n")
        student["Class"] = input("Input student class\n")
        student["Grades"] = gradeList()
        student["Average"] = findAverage(student["Grades"])
        studentList.append(student)
        continue_adding_students = input("Continue adding students? Y (yes) or N (no)\n").capitalize()
    return(studentList)

#newStudents()


def classAverage ():
    studentList = newStudents()
    avgsTotal = 0
    classAvg = 0
    for student in studentList:
        avgsTotal += student["Average"]
    classAvg = avgsTotal/len(studentList)
    print(classAvg)

classAverage()