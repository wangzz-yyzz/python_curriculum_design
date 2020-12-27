from ..manager.data import *
from ..util.util import *
from ..util.sort import *
import studentManager.manager.dao as dao
import sys


def run():
    print("Welcome to Student Manager System!")
    while True:
        # 主循环
        printMenu()
        try:
            c = int(input("Enter the service: "))
        except ValueError:
            c = -1
        if c == 1:
            display(readData())
        elif c == 2:
            retrieve()
        elif c == 3:
            create()
        elif c == 4:
            delete()
        elif c == 5:
            update()
        elif c == 6:
            sortData()
        elif c == 7:
            showTenth()
        elif c == 8:
            getAverage()
        elif c == 9:
            print("Bye")
            sys.exit(0)
        elif c == 10:
            initData()
        else:
            print("Please Enter The Right Number!")


def retrieve():
    """打印数据"""
    data = []
    print("1. All")
    print("2. select by name")
    print("3. select by id")
    print("4. select by native")
    print("5. select by sex")
    print("6. select by class")
    c = int(input("Enter the number of choice: "))
    if c == 1:
        data = readData()
    elif c == 2:
        name = input("Enter the name: ")
        data = dao.selectByName(name)
    elif c == 3:
        student_id = input("Enter the id: ")
        data = dao.selectById(student_id)
    elif c == 4:
        native = input("Enter the native place: ")
        data = dao.selectByNative(native)
    elif c == 5:
        sex = input("Enter the sex: ")
        data = dao.selectBySex(sex)
    elif c == 6:
        student_class = input("Enter the class: ")
        data = dao.selectByClass(student_class)
    if len(data) == 0:
        print("Can not find any student: ")
    else:
        display(data)


def create():
    """创建新的学生数据"""
    student = Student()
    student.student_id = input("ID: ")
    student.name = input("Name: ")
    student.sex = input("Sex: ")
    student.age = input("Age: ")
    student.native_place = input("Native: ")
    student.student_class = input("Class: ")
    student.score = input("Score: ")
    dao.add(student)
    print("Done")


def delete():
    """根据ID或姓名删除学生数据"""
    print("1. remove by Id")
    print("2. remove by Name")
    c = int(input("Enter the choice: "))
    if c == 1:
        student_id = input("Enter the Id")
        if dao.removeById(student_id) == 0:
            print("Done")
        else:
            print("Failed")
    elif c == 2:
        name = input("Enter the name: ")
        if dao.removeByName(name) == 0:
            print("Done")
        else:
            print("Failed")
    else:
        print("Please Enter the right number")


def update():
    """查找并更新学生信息"""
    student_id = input("Enter the Id of student you want to update: ")
    data = dao.selectById(student_id)
    if not data:
        print("Can not find such student")
    else:
        display(data)
        dao.removeById(student_id)
    print("Enter the newer inf")
    create()


def sortData():
    """对数据按从大到小的顺序排序"""
    data = readData()
    quick_sort(data, 0, len(data) - 1)
    # data.sort(reverse=True, key=Student.get_score)
    writeData(data)
    print("Done")
    display(readData())


def showTenth():
    """展示分数前前10的学生信息"""
    sortData()
    data = readData()
    if len(data) > 10:
        data = dao[:10]
    display(data)


def getAverage():
    """获取某一类学生总分的平均值"""
    print("1. Class")
    print("2. Sex")
    c = int(input("Average in ?: "))
    total = 0
    if c == 1:
        student_class = input("Enter the class: ")
        data = dao.selectByClass(student_class)
        if len(data) == 0:
            print("Can not find any student")
        else:
            for i in data:
                total += float(i.score)
            print("Average: " + str(total / len(data)))
    elif c == 2:
        sex = input("Enter the sex: ")
        data = dao.selectBySex(sex)
        if len(data) == 0:
            print("Can not find any student")
        else:
            for i in data:
                total += float(i.score)
            print("Average: " + str(total / len(data)))
    else:
        print("Please Enter the right number!")