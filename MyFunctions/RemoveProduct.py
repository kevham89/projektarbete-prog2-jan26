# Funktion för att ta bort en produkt (ropar på MyInventory.py)

def RemoveProduct(Inventory): # funktionen tar emot "Inventory"
    Name = input("Sök på produkt: ")
    Results = Inventory.SearchProduct(Name) # Vi söker på användarens input i "Inventory" som vi tog emot i tidigare steget.

    if not Results: # om vi inte får något träff på input så skriver vi ut det här meddelandet.
        print(f"Hittade inget på {Name}")
        return
    
    Product = Results[0] # Skapar en variabel som kopierar första träffen på våran sökning och visar informationen.
    print(f"Namn: {Product['Name']} ")
    print(f"Kategori: {Product['Category']}")
    print(f"Lagersaldo: {Product['Stock']}")

    Confirm = input(f"Vill du ta bort {Product['Name']}? (Ja/Nej)").lower() # Användaren bekräftar att detta är rätt innan vi plockar bort det.
    if Confirm != "ja":
        print("Avbryter bortagningen.")
        return
    
    if Inventory.RemoveProduct(Name): # vi ropar på metoden "RemoveProduct" i classen MyInventory
        print(f"{Product['Name']} borttagen.")
    else:
        print(f"Kunde ej ta bort {Product['Name']}")

