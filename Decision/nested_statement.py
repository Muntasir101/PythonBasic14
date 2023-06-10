"""
40 pass marks
40-49 = D
50-59 = C
60-69= B
70-79 = A-
80-89= A
90-100= A+
"""

pass_mark = 40

try:
    student_mark = int(input("Enter your Mark: "))

    if student_mark >= pass_mark:
        if 40 <= student_mark <= 49:
            print("Grade D")
        elif 50 <= student_mark <= 59:
            print("Grade C")
        elif 60 <= student_mark <= 69:
            print("Grade B")
        elif 70 <= student_mark <= 79:
            print("Grade A-")
        elif 80 <= student_mark <= 89:
            print("Grade A")
        elif 90 <= student_mark <= 100:
            print("Grade A+")
        else:
            print("Invalid Marks.")
    else:
        print("Fail")
except ValueError:
    print("Invalid input. Please enter a valid integer mark.")
