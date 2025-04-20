from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school = School('Abc', 'Dhaka')

# adding classroom
eight = Classroom('Eight')
nine = Classroom('Nine')
ten = Classroom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)



# Adding Student
rahim = Student("Rahim",eight)
sakil = Student("Sakil",nine)
sabbir = Student("Sabbir",ten)
rafi = Student("Rafi",ten)

school.student_admission(rahim)
school.student_admission(sakil)
school.student_admission(sabbir)
school.student_admission(rafi)

# adding teachers

Abul = Teacher('Abul Khan')
Babul = Teacher('Babul Khan')
Kabul = Teacher('Kabul Khan')

# Adding subjects

bangla = Subject("bangla",Abul)
physics = Subject("Physics",Babul)
chemistry = Subject("Chemistry",Kabul)
biology = Subject("Biology",Kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)

nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)

ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)

