# Funktion för att uppdatera lagret på en produkt (ropar på MyInventory.py)
from tkinter import messagebox

def UpdateStock(Inventory, DicHeader, Tree, RefreshTree):
    Name = DicHeader["Namn"].get()
    Results = Inventory.SearchProduct(Name)

    if not Results:
        messagebox.showinfo("Hittades inte", "Hittade inga produkter med namnet {Name}.")
        return

    # Vi skapar en lista med dictionaries från Metoden "SearchProduct" från classen "MyInventory"
    Product = Results[0]
    
    # Testar att värdet för input är ett tal
    try:
        Amount = int(DicHeader["Lagersaldo"].get())
    except ValueError:
        messagebox.showerror("Fel", "Ogiltigt värde, ange ett heltal.")
        return
    if Inventory.UpdateStock(Name, Amount):
        RefreshTree(Tree, Inventory)
    else:
        messagebox.showerror("Fel", f"Kunde ej uppdatera lagersaldo för {Product['Namn']}")