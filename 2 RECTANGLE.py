# 2. Write a class "Rectangle" with attributes length and width. Add a method to calculate and return the area.

   **Input:**  
   Length: 5  
   Width: 3  

   **Output:**  
   Area: 15  



   class rect:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def rect1(self):
        print(f"Area:{self.length*self.width}")
rect=rect(5,3)
area=rect.rect1()
