import prettytable as pt


def display(data: list):
    tb = pt.PrettyTable()
    tb.field_names = ["ID", "Name", "Sex", "Age", "Native Place", "Class", "Score"]
    for i in data:
        tb.add_row([i.student_id, i.name, i.sex, i.age, i.native_place, i.student_class, i.score])
    print(tb)


def printMenu():
    tb = pt.PrettyTable()
    tb.field_names = ["Student Manager System"]

    tb.add_row(["1. show the inf of all students"])
    tb.add_row(["2. retrieve"])
    tb.add_row(["3. create new inf"])
    tb.add_row(["4. delete student"])
    tb.add_row(["5. update student"])
    tb.add_row(["6. sort by score"])
    tb.add_row(["7. the 10th students"])
    tb.add_row(["8. average"])
    tb.add_row(["9. exit"])
    tb.add_row(["10. Init Data"])

    tb.align["Student Manager System"] = "l"
    print(tb)
