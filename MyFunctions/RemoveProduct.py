# Funktion för att ta bort en produkt (ropar på MyInventory.py)
from tkinter import messagebox

def RemoveProduct(Inventory, DicHeader, Tree, RefreshTree): # funktionen tar emot "Inventory"
    Name = DicHeader["Namn"].get()
    Results = Inventory.SearchProduct(Name) # Vi söker på användarens input i "Inventory" som vi tog emot i tidigare steget.

    if not Results: # om vi inte får något träff på input så skriver vi ut det här meddelandet.
        messagebox.showinfo("Hittades inte", f"Hittade inget på {Name}")
        return
    
    Product = Results[0] # Skapar en variabel som kopierar första träffen på våran sökning och visar informationen.

    Confirm = messagebox.askyesno("Bekräfta borttagning", f"Vill du ta bort {Product['Name']}?")
    if not Confirm:
        return
    if Inventory.RemoveProduct(Name):
        RefreshTree(Tree, Inventory)

    else:
        messagebox.showerror("Fel", f"Kunde ej ta bort {Product['Name']}")