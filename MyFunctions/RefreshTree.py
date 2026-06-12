# Funktion för att fylla Tree med Data från våran CSV
def RefreshTree(Tree, Inventory):
    for Row in Tree.get_children():
        Tree.delete(Row)


    for Product in Inventory.Products:
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