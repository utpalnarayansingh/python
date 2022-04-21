# def totalStudents(students):
#     c = 0
#     for key, value in students.items():
#         c += len(value)

#     return c

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
# name = list(students.keys())

subdetail = list(students.values())
print(subdetail)
agearr = []
for i in list(students.values()):
    # templist = list(i.values())
    agearr.append(list(i.values())[0])

print(agearr)

# for i in agearr:
#     print(i[1])
