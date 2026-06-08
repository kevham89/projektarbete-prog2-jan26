# Huvudklass för alla products 
class MyProducts:
    def __init__(self, name, category, maker, price, inventory, expiry_date, strenght, dosage):
        self.name = name
        self.category = category
        self.maker = maker
        self.price = price
        self.inventory = inventory
        self.expiry_date = expiry_date
        self.stryka = strenght
        self.dosage = dosage

class prescription(MyProducts):
    def __init__(self, name, category, maker, price, inventory, expiry_date, strenght, dosage):
        super().__init__(name, category, maker, price, inventory, expiry_date, strenght, dosage)
        self.prescription = prescription