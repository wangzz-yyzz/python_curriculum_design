import json
import os
from ..entity.student import *

path = "data"
file_name = "data.txt"


def readData() -> list:
    with open(path + os.sep + file_name, "r") as f:
        data = json.load(f, object_hook=encode)
    return data


def decode(obj: Student):
    return {
        "student_id": obj.student_id,
        "name": obj.name,
        "sex": obj.sex,
        "age": obj.age,
        "native_place": obj.native_place,
        "student_class": obj.student_class,
        "score": obj.score
    }


def encode(dic):
    student = Student()
    student.student_id = dic["student_id"]
    student.name = dic["name"]
    student.sex = dic["sex"]
    student.age = dic["age"]
    student.student_class = dic["student_class"]
    student.native_place = dic["native_place"]
    student.score = dic["score"]
    return student


def writeData(data: list):
    with open(path + os.sep + file_name, "w") as f:
        f.writelines(json.dumps(data, default=decode))


def initData():
    data: list[Student] = []
    student_id = ["1001", "1002", "1003"]
    name = ["zhangSan", "liSi", "wangWu"]
    sex = ["Male", "Female", "Male"]
    age = [18, 19, 20]
    native_place = ["ChongQing", "ShanDong", "Beijing"]
    student_class = ["zk_1", "zk_2", "rg_1"]
    score = [4.1, 4.2, 3.9]
    for i in range(len(student_id)):
        student = Student()
        student.student_id = student_id[i]
        student.name = name[i]
        student.sex = sex[i]
        student.age = age[i]
        student.native_place = native_place[i]
        student.student_class = student_class[i]
        student.score = score[i]
        data.append(student)
    writeData(data)