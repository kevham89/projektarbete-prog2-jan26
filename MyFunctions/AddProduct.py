# Funktion för att lägga till en produkt (ropar på MyInventory.py)

# Behöver importera messagebox även här för att det ska fungera.
from tkinter import messagebox

def AddProduct(Inventory, DicHeader, Tree, RefreshTree): # "Inventory länkar mot objektet vi skapade i "MyProgram"
    Name = DicHeader["Namn"].get()
    Category = DicHeader["Kategori"].get()
    Brand = DicHeader["Tillverkare"].get()

    try: # säkerställer att vi får in ett tal
        Price = float(DicHeader["Pris"].get())
    except ValueError:
        messagebox.showerror("Fel", "Ogiltigt pris, ange ett tal.")
        return
    
    try: # säkerställer att vi får in ett tal
        Stock = int(DicHeader["Lagersaldo"].get())
    except ValueError:
        messagebox.showerror("Fel", "Ogiltigt antal, ange ett tal.")
        return
    
    ExpiryDate = DicHeader["Utgångsdatum"].get()
    Strength = DicHeader["Styrka"].get()
    Dosage = DicHeader["Dosering"].get()
    Prescription = DicHeader["Receptbelagd"].get().lower() == "ja"

    PrescriptionWarning = Inventory.AddProduct(Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage, Prescription)

    RefreshTree(Tree, Inventory)

    if PrescriptionWarning:
        messagebox.showwarning("Receptbelagd produkt", PrescriptionWarning)

