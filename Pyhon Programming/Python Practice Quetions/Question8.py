# Write A program using if-elif-else statements to grade a student based on their marks. The grading criteria are as follows:
# Marks >= 90: Grade A
# Marks >= 80 and < 90: Grade B
# Marks >= 70 and < 80: Grade C
# Marks >= 60 and < 70: Grade D
# Marks < 60: Grade F

marks = float(input("Enter the marks obtained by the student: "))   

if marks >= 90:
    print("Grade A : Excellent work!")
elif marks >= 80:
    print("Grade B : Well done!")
elif marks >= 70:
    print("Grade C : Good job!")
elif marks >= 60:
    print("Grade D : You need to improve!")    
else:    
    print("Grade F : You need to work harder!")

