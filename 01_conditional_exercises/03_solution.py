student_score = 200

if student_score >= 101:
    print("Please verify your grade again")
    exit()

if student_score >= 90 :
    grade = "A"
elif student_score >= 80 :
    grade = "B"
elif student_score >= 70 :
    grade = "C"
elif student_score >= 60 :
    grade = "D"
else: 
    grade = "F"

print("Grade : ",grade)