mathMarks = float(input("Enter marks obtained in Maths : "))
phyMarks = float(input("Enter marks obtained in Physics : "))
chemMarks = float(input("Enter marks obtained in Chemistry : "))

if mathMarks < 35 and phyMarks < 35 and chemMarks < 35:
    print("You have failed the exam")
else:
    totalMarks = mathMarks+phyMarks+chemMarks
    average = totalMarks/3
    if average <= 59:
        print("C Grade\nAverage : %.2f" % (average))
    elif average <= 69:
        print("B Grade\nAverage : %.2f" % (average))
    else:
        print("A Grade\nAverage : %.2f" % (average))
