from MyClasses import Products, PrescriptionProducts

class MyInventory():

    # Vi hämtar in classes "FileProcessor" som sköter inläsningen utav våran data.
    def __init__(self, FileProcessor):
        self.FileProcessor = FileProcessor
        self.Products = self.FileProcessor.ReadData()

    # Vi skapar metoden för att söka efter "namn" i produktlistan.
    def SearchProduct(self, Name):
        Results = []
        for Product in self.Products:
            if Product["Name"].lower() == Name.lower():
                Results.append(Product)
        return Results

    # Metod för att lägga till produkter till. Prescription=False betyder att om man inte anger något så antags produkter att inte vara receptbelagd.
    def AddProduct(self, Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage, Prescription=False):
        if Prescription:
            NewProduct = PrescriptionProducts(Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage)
        else:
            NewProduct = Products(Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage)
        ProductDictionary = {
            "Name": NewProduct.Name,
            "Category": NewProduct.Category,
            "Brand": NewProduct.Brand,
            "Price": NewProduct.Price,
            "Stock": NewProduct.Stock,
            "ExpiryDate": NewProduct.ExpiryDate,
            "Prescription": "Ja" if Prescription else "Nej",
            "Strength": NewProduct.Strength,
            "Dosage": NewProduct.Dosage
        }
        self.Products.append(ProductDictionary)
        self.FileProcessor.SaveData(self.Products)

        if Prescription: # Om produkten är receptbelagd så skickar vi en varning till användaren
            return NewProduct.PrescriptionWarning()
        return None

    # Metod för att uppdatera antal i lager
    def UpdateStock(self, Name, Amount):
        for Product in self.Products:
            if Product["Name"].lower() == Name.lower():
                StockCheck = int(Product["Stock"]) + Amount
                if StockCheck < 0:
                    return False # Skickar tillbaka "False" utifall lagret får negativa nummer.
                Product["Stock"] = StockCheck
                self.FileProcessor.SaveData(self.Products)
                return True # Skickar tillbaka "True" om vi hittar produkten
        return False # Annars skickar vi tillbaka "False"

    # Metod för att ta bort en produkt
    def RemoveProduct(self, Name):
        for Product in self.Products:
            if Product["Name"].lower() == Name.lower():
                self.Products.remove(Product)
                self.FileProcessor.SaveData(self.Products)
                return True
        return False