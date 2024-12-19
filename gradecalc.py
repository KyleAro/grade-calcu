q1=int(input("Enter Your Quiz 1 Grade:"))
q1I=int(input("How many items is this quiz:"))

q2=int(input("\nEnter Your Quiz 2 Grade:"))
q2I=int(input("How many items is this quiz:"))

q3=int(input("\nEnter Your Quiz 3 Grade:"))
q3I=int(input("How many items is this quiz:"))

q4=int(input("\nEnter Your Quiz 4 Grade:"))
q4I=int(input("How many items is this quiz: "))


#Detailed Computation

q1D= (q1/q1I)*100

q2D= (q2/q2I)*100

q3D= (q3/q3I)*100

q4D= (q4/q4I)*100

QA= (q1D+q2D+q3D+q4D)/4

print("\nQuiz Average")
print(round(QA,2))


#Lab ACT SCORES

l1=int(input("\nEnter Your Laboratory Activity 1 Grade:"))

l2=int(input("\nEnter Your Laboratory Activity 2 Grade:"))

l3=int(input("\nEnter Your Laboratory Activity 3 Grade:"))

l4=int(input("\nEnter Your Laboratory Activity 4 Grade:"))



LA= (l1+l2+l3+l4)/4

print("\nLaboratory Activity Average")
print(round(LA,2))

#Project Scores

PA=int(input("\nEnter Your Project Grade:"))
print("\nProject Average")
print(round(PA,2))

#Major Exam Score

m1=int(input("\nEnter Your Major Exam Grade:"))
m1I=int(input("How many items is this Exam:"))

MA= (m1/m1I)*100
print("\nMajor Exam Average")
print(round(MA,2))

#Attendance Grade

a1=int(input("\nHow many days did you attend the class:"))
a1I=int(input("How many meetings do you have:"))

AA= (a1/a1I)*100
print("\nAttendance Average")
print(round(AA,2))

#PERCENTAGE CALCULATION

print( "       **QUIZ = 15% of your overall grade   **")
print( "     \n**Lab Acts = 25% of your overall grade**")
print( "     \n**Major Examination = 30% of your overall grade**")
print( "     \n**Project = 25% of your overall grade**")
print( "     \n**Attendance = 5% of your overall grade**")

QFA= QA * 0.15
LFA= LA * 0.25
MFA= MA * 0.30
PFA= PA * 0.25
AFA= AA * 0.05

# PERCENTAGE CALCULATIONS BREAKDOWN
print("\nQUIZ FULL GRADE PERCENTAGE             ")
print(round(QFA,2))
print("\nLABORATORY FULL GRADE PERCENTAGE       ")
print(round(LFA,2))
print("\nMAJOR EXAMINATION FULL GRADE PERCENTAGE")
print(round(MFA,2))
print("\nPROJECT FULL GRADE PERCENTAGE          ")
print(round(PFA,2))
print("\nATTENDANCE FULL GRADE PERCENTAGE       ")
print(round(AFA,2))

TA= QFA+LFA+MFA+PFA+AFA
print("\nTOTAL AVERAGE ")
print(round(TA,2))
if TA>=95:
    print("Congratulations on Passing this Semester\n")
    print("Your letter average is A which means Excellent")
if 90 <= TA <= 94 :
    print("Congratulations on Passing this Semester\n")
    print("Your letter average is B which means Very Good")
if 83 <= TA <= 89 :
    print("Congratulations on Passing this Semester\n")
    print("Your letter average is C which means Good")
if 74 <= TA <= 82 :
    print("Congratulations on Merely Passing this Semester\n")
    print("Your letter average is d which means Need Improvement")
if TA <= 73:
    print("Better Luck Next Semester\n")
    print("Your letter average is F which means Failed")

    

