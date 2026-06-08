# Huvudklass för alla products 
class Products:
    def __init__(self, Name, Category, Brand, Price, Inventory, ExpiryDate, Strength, Dosage):
        self.Name = Name
        self.Category = Category
        self.Brand = Brand
        self.Price = Price
        self.Inventory = Inventory
        self.ExpiryDate = ExpiryDate
        self.Strength = Strength
        self.Dosage = Dosage

class PrescriptionProducts(Products):
    def __init__(self, Name, Category, Brand, Price, Inventory, ExpiryDate, RequiresPrescription, Strength, Dosage):
        super().__init__(Name, Category, Brand, Price, Inventory, ExpiryDate, Strength, Dosage)
        self.RequiresPrescription = RequiresPrescription