class Student:
    def __init__(self):  # initialize constructor
        self.name = ""
        self.rollNo = 0

    def takeStudentData(self):  # take input from user
        self.name = input("\nEnter the name of student : ")
        print("\nEnter the roll number of", self.name, ": ", end="")
        self.rollNo = input()

    def StudentData(self):  # print the student data
        print("\nStudent name is", self.name)
        print("\nRoll number of", self.name, "is", self.rollNo)


class Exam(Student):  # multilevel inheritance
    def __init__(self):  # initialize constructor
        Student.__init__(self)
        self.arr = []

    def takeInput(self):  # take input from user
        for i in range(0, 6):
            print("\nEnter the marks of subject", i + 1, ":", end=" ")
            n = int(input())
            self.arr.append(n)

    def printData(self):  # print the marks
        print(self.name, "\nYour marks is ", end="")
        print(self.arr)


class Result(Exam):  # multilevel inheritance
    def __init__(self):  # initialize constructor
        Exam.__init__(self)
        self.total_marks = 0

    def calculateAvg(self):  # print the average of marks
        self.check = True
        for i in range(0, 6):
            if (self.arr[i] < 33):  # if marks is < 33 no need to print average of marks
                print(self.name, "\nyou are fail in subject:", i + 1)
                self.check = False
                break
            self.total_marks = self.total_marks + self.arr[i]

        if (self.check):
            print("\nTotal marks is", self.total_marks)
            print(self.name, "You get", self.total_marks / 6, "%")


st = Student()
exam = Exam()
result = Result()

result.takeStudentData()
result.takeInput()

result.StudentData()
result.printData()
result.calculateAvg()


print("\nNAME AND ID :: DHRUV PUVAR AND 20CE117\n")