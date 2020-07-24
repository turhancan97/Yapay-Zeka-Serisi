# calculator project
# class -> init -> method/attribute -> funct vs method

class Calc(object):
    "calculator"
    # init metodu
    def __init__(self, a, b):
        "initialize values"
        
        # attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
         
    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
           
print("Choose add(1), multiply(2), div(3)")
selection = input("Select 1 or 2 or 3 \n")

v1 = int(input("First Value = "))
v2 = int(input("Second Value = "))

c1 = Calc(v1,v2)
if selection == "1":
    add_result = c1.add()
    print("\nAddition Result : {}".format(add_result))
elif selection == "2": # else if = elif
    multiply_result = c1.multiply()
    print("\nMultiplication Result : {}".format( multiply_result))
elif selection == "3":
    div_result = c1.division()
    print("\nDivision Result : {}".format(div_result))
else: 
    print("\nError there is no proper selection")