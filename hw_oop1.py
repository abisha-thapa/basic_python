"""
We have class defined for vehicles. Create two vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
and car2 to be a blue van need Jump worth $10,000.00
define the Vehicle class
"""

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f"%(self.name,self.color,self.kind,self.value)
        return desc_str

    def __init__(self,name,kind,color,value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

car1 = Vehicle("Fer","convertible","red",60000)
print (car1.description())
car2 = Vehicle("Jump","van","blue",10000)
print (car2.description())