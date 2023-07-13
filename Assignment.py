class Manufacturer:
   
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.brands = []
       
    def add_brand(self, brand):
        self.brands.append(brand)
       
    def get_brands(self):
        return self.brands
   
class Car:
   
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
       
    def get_details(self):
        print(f"Brand name : `{self.brand}`, Model Name : `{self.model}`, Year Of Manufacturing : `{self.year}`")
 
# Create two manufacturers
manufacturer1 = Manufacturer("Mahindra", "India")
manufacturer2 = Manufacturer("Hyundai", "Japan")
 
# Add brands to the manufacturers
manufacturer1.add_brand("Thar")
manufacturer1.add_brand("Scorpio")
manufacturer2.add_brand("Santro")
manufacturer2.add_brand("Verna")
 
# Create cars for each manufacturer
car1 = Car("Mahindra", "Thar", 2023)
car2 = Car("Mahindra", "Scorpio", 2022)
car3 = Car("Hyundai", "Santro", 2023)
car4 = Car("Hyundai", "Verna", 2022)
# Print the details of the cars
car1.get_details()
print()
car2.get_details()
print()
car3.get_details()
print()
car4.get_details()
