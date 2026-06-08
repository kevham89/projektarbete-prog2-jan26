from MyClasses import Products, PrescriptionProducts

class MyInventory():

    # Vi hämtar in classes "FileProcessor" som sköter inläsningen utav våran data.
    def __init__(self, FileProcessor):
        self.FileProcessor = FileProcessor
        self.Products = self.FileProcessor.ReadData()

    def SearchProduct(self):
        pass

    # Metod för att lägga till produkter till. Prescription=False betyder att om man inte anger något så antags produkter att inte vara receptbelagd.
    def AddProduct(self, Name, Category, Brand, Price, Inventory, ExpiryDate, Strength, Dosage, Prescription=False):
        if Prescription:
            NewProduct = PrescriptionProducts(Name, Category, Brand, Price, Inventory, ExpiryDate, Strength, Dosage)
        else:
            NewProduct = Products(Name, Category, Brand, Price, Inventory, ExpiryDate, Strength, Dosage)
        ProductDictionary = {
            "Name": NewProduct.Name,
            "Category": NewProduct.Category,
            "Brand": NewProduct.Brand,
            "Price": NewProduct.Price,
            "Inventory": NewProduct.Inventory,
            "ExpiryDate": NewProduct.ExpiryDate,
            "Prescription": "Ja" if Prescription else "Nej",
            "Strength": NewProduct.Strength,
            "Dosage": NewProduct.Dosage
        }
        self.Products.append(ProductDictionary)
        self.FileProcessor.SaveData(self.Products)





    def UpdateStock(self):
        pass
    def RemoveProduct(self):
        pass