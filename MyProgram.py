from MyClasses import FileProcessor, MyInventory
from MyFunctions import ShowMenu, AddProduct, SearchProduct, UpdateStock, RemoveProduct

def Start():
    FP = FileProcessor()
    Inventory = MyInventory(FP)

    while True:
        ShowMenu()
        UserInput = input("Välj ett alternativ.")

        if UserInput == "1":
            AddProduct(Inventory)
        elif UserInput == "2":
            SearchProduct(Inventory)
        elif UserInput == "3":
            UpdateStock(Inventory)
        elif UserInput == "4":
            RemoveProduct(Inventory)
        elif UserInput == "5":
            print("Avslutar programmet, Tack för att du använder vårat program!")
            break
        else:
            print("Ogiltigt Val.")
Start()

