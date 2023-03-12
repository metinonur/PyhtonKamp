students = ["Metin Onur"," Alperen Doğu","mert onur"]

#listeye yeni öğrenci eklemek için 
def addStudent():
    newStudent= input("Lütfen eklemek istediğiniz öğrencinin isim soyismini giriniz : ")
    students.append(newStudent)
    print(f"{newStudent} Öğrenci başarıyla eklenmiştir.")
    return students


#listeden öğrenci silmek için
def removeStudent():
    removeStudent = input("Lütfen silmek istediğiniz öğrencinin isim soyismini giriniz : ")
    students.remove(removeStudent)
    print(f"{students}  Öğrenci başarıyla silinmiştir.")
    return students

#listeye birden fazla öğrenci eklemek 
def addMultipleStudents():
    student1 = input("Lütfen eklemek istediğiniz öğrencinin isim soyismini giriniz : ")
    student2  = input("Lütfen eklemek istediğiniz öğrencinin isim soyismini giriniz : ")
    students.extend([student1,student2])
    print(f"{student1} {student2} Öğrenciler başarıyla eklenmiştir.")
    return students


#listeyi listelemek için 
def listStudents():
    for student in students:
        print(students)
        return students

#index numaralarını öğrenci numarası olarak kabul edip öğrenci adlarını ve numaralarını aynı anda aldık.
def studentNumber():
    i =0
    while i < len(students):
        print(f"{students[i]},{students.index(students[i])}")
        i += 1
        return students


# listStudents()
studentNumber()