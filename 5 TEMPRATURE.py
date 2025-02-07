# 5. Create a class "Temperature" with a method to convert Celsius to Fahrenheit and another method to convert Fahrenheit to Celsius.

   **Input:**  
   Celsius: 100  

   **Output:**  
   Fahrenheit: 212°F  

   **Input:**  
   Fahrenheit: 32  

   **Output:**  
   Celsius: 0°C


    

   class temp:
    def cels(self, celsius):
        fahrenheit=(celsius * 9/5) + 32
        return fahrenheit
    def fahr(self, fahrenheit):
        celsius=(fahrenheit - 32) * 5/9
        return celsius
temp1=temp()
celsius1=100
fahrenheit1=temp1.cels(celsius1)
print(f"Fahrenheit:{fahrenheit1}°F")  
fahrenheit2=32
celsius2=temp1.fahr(fahrenheit2)
print(f"Celsius:{celsius2}°C")  



