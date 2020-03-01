groupmates=[
    {
        "name":"Виктор",
        "surname":"Скоморохов",
        "exams":["Информатика","Математика","Физика"],
        "marks":[4,4,4]
        },
     {
        "name":"Вероника",
        "surname":"Коровушкина",
        "exams":["Информатика","КТП","АиГ"],
        "marks":[5,5,5]
        },
     {
        "name":"Заза",
        "surname":"Харатишвили",
        "exams":["История","Философия","Физика"],
        "marks":[5,5,4]
        },
     {
        "name":"Егор",
        "surname":"Коловертных",
        "exams":["История","КТП","Филосифия"],
        "marks":[3,3,4]
        },
    {
        "name":"Александр",
        "surname":"Бережков",
        "exams":["АиГ","История","Филосифия"],
        "marks":[5,3,4]
        },
    ]
def print_students(students,mark):
    print ("name".ljust(15), "surname".ljust(10),"exams".ljust(30),"marks".ljust(20))
    for student in students:
        marks_list=student['marks']
        result=(sum(marks_list)/len(marks_list))
        if result>=need:
            print(student["name"].ljust(15),student["surname"].ljust(10),str(student["exams"]).ljust(30),str(student["marks"]).ljust(20))

need=int(input('Input:'))
                  
print_students(groupmates,need)
    
