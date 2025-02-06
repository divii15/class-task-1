# 4. Write a class "Student" with attributes name and marks. Add a method to check if the student has passed (pass mark: 40).

   **Input:**  
   Name: John  
   Marks: 35  

   **Output:**  
   John has failed.  

   **Input:**  
   Name: Emma  
   Marks: 45  

   **Output:**  
   Emma has passed.



   class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def mark(self):
        if self.marks>=40:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")
stu1=Student("John",39)
stu1.mark()
stu2=Student("Emma",58)
stu2.mark()