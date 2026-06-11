# Huvudklass för alla products 
class Products:
    def __init__(self, Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage):
        self.Name = Name
        self.Category = Category
        self.Brand = Brand
        self.Price = Price
        self.Stock = Stock
        self.ExpiryDate = ExpiryDate
        self.Strength = Strength
        self.Dosage = Dosage

# Sub-Class för att separera receptbelagda produkter, ärver från "Products" och varnar användaren att recept behövs. 
class PrescriptionProducts(Products):
    def __init__(self, Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage):
        super().__init__(Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage)
        self.RequiresPrescription = True # Vi använder True här för att det alltid gäller när vi skapar ett "PrecriptionsProducts"-objekt.

    def PrescriptionWarning(self):
        return f"Observera att {self.Name} är receptbelagt och kräver giltigt recept vid utlämning." # Skickar en varning om produkten är receptbelagd.