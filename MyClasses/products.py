# Huvudklass för alla products 
class products:
    def __init__(self, category, maker, price, inventory, expiry_date, strenght, dosage):
        self.category = category
        self.maker = maker
        self.price = price
        self.inventory = inventory
        self.expiry_date = expiry_date
        self.stryka = strenght
        self.dosage = dosage

class prescription(products):
    def __init__(self, category, maker, price, inventory, expiry_date, strenght, dosage):
        super().__init__(category, maker, price, inventory, expiry_date, strenght, dosage)
        self.prescription = prescription