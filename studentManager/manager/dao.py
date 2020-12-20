from ..manager.data import *


def selectByName(name: str) -> list:
    res: list[Student] = []
    for i in readData():
        if i.name == name:
            res.append(i)
    return res


def selectById(student_id: str) -> list:
    res: list[Student] = []
    for i in readData():
        if i.student_id == student_id:
            res.append(i)
    return res


def selectByNative(native: str) -> list:
    res: list[Student] = []
    for i in readData():
        if i.native_place == native:
            res.append(i)
    return res


def selectBySex(sex: str) -> list:
    res: list[Student] = []
    for i in readData():
        if i.sex == sex:
            res.append(i)
    return res


def selectByClass(student_class: str) -> list:
    res: list[Student] = []
    for i in readData():
        if i.student_class == student_class:
            res.append(i)
    return res


def add(student: Student):
    data = readData()
    data.append(student)
    writeData(data)


def removeById(student_id: str) -> int:
    """成功删除返回0，失败返回1"""
    data = readData()
    flag = False
    for i in data:
        if i.student_id == student_id:
            data.remove(i)
            flag = True
    if not flag:
        return 1
    else:
        writeData(data)
        return 0


def removeByName(name: str) -> int:
    """成功删除返回0，失败返回1"""
    data = readData()
    flag = False
    for i in data:
        if i.name == name:
            data.remove(i)
            flag = True
    if not flag:
        return 1
    else:
        writeData(data)
        return 0