Student_name = input("Enter student name: ")
Math=int(input("Enter math marks:"))
Physics=int(input("Enter physics marks:"))
Chemistry=int(input("Enter chemistry marks:"))

Total_marks=Math+Physics+Chemistry

Avarage=Total_marks / 3
if(Avarage>=80):
    grade ="A+"
    
elif(Avarage>=70):
    grade ="A"
elif(Avarage>=60):
    grade ="B"  
elif (Avarage>= 50):
    grade ="C"
else :"F"  

print(f"Student_name: {Student_name}")
print(f"Total-marks: {Total_marks}")

print(f"Avarage: {Avarage}")
print(f"grade {grade}")
