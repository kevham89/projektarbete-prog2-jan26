# Funktion för att söka på en produkt, Uppdaterad för GUI.

def SearchProduct(Inventory, DicHeader, Tree): # funktionen tar emot "Inventory"
    Name = DicHeader["Namn"].get()

    # Vi börjar med att rensa hela Tree listan.
    for Row in Tree.get_children():
        Tree.delete(Row)

    if not Name: # Om fältet är tomt, visa alla produkter.
        Results = Inventory.Products
    else:
        Results = Inventory.SearchProduct(Name)

    for Product in Results:
        Tree.insert("", "end", values=(
            Product["Name"],
            Product["Category"],
            Product["Brand"],
            Product["Price"],
            Product["Stock"],
            Product["ExpiryDate"],
            Product["Prescription"],
            Product["Strength"],
            Product["Dosage"],

        ))