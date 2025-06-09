import math
  
class MultiFunctionInClass:
    def subfieldsinAI():
        subFields = ["Machine Learning", "Deep Learning", "NLP", "Timeseriesanaysis"]
        print("Sub fields in ai are")
        for field in subFields:
            print(field)
    def OddEven():
        number = int(input("Enter a Number"))
        if number%2 == 0:
            message = "Even"
        else:
            message = "Odd"
        return message

    def eligiblityForMarriage(gender, age):
        if gender=="Male" and age >=21:
            status = "Eligible"
        elif gender =="Female" and age >=18 :
            status ="Eligible" 
        else:
            status ="Not Eligible"
        return status

    def findPercent(s1,s2,s3,s4,s5):
        total = s1+s2+s3+s4+s5
        percentage = (total / 500) * 100
        return percentage

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))