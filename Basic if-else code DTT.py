Name=input("Enter Your Full Nmae:")
Theory_marks=int(input("Enter Your Theory Marks out of 50(MCQ):"))
Hazard_marks=int(input("Enter Your Hazard Marks out of 75(Video clips):"))
if Theory_marks <= 42 and Hazard_marks <= 43:
    print(f"{Name}\nTheory Marks out of 50(MCQ) is {Theory_marks}\nHazard Marks out of 75(Video clips) is {Hazard_marks}\nSorry, you haven't passed the Driving Theory Test.\nBetter Luck Next Time!!!!")
else:
    print(f"{Name}\nTheory Marks out of 50(MCQ) is {Theory_marks}\nHazard Marks out of 75(Video clips) is {Hazard_marks}\nCongraulation!!, you have passed the Driving Theory Test.\nGood Luck!!!!")
