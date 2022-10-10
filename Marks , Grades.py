'''marks       #grades
100-90         A
90-80          B
80-70          C
70-0           D'''

marks = int(input("enter your marks:"))

if marks > 90 and marks <=100:
    print("Your grade is A")

elif marks > 80 and marks <=90:
    print("Your grade is B")

elif marks > 70 and marks <=80:
    print("Your grade is C")

elif marks > 0 and marks <=70:
    print("Your grade is D")
else:
    print("invalid")
        