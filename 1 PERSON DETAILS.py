# 1. Create a Python class named "Person" with attributes name and age. Add a method to display the details.

   **Input:** 
   Name: Alice  
   Age: 25  

   **Output:**  
   Person Name: Alice  
   Age: 25  



    class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_1(self):
        print(f"Person Name:{self.name}")
        print(f"Age:{self.age}")
person=(person("Alice", 25))
person.person_1()
