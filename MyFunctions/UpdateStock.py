# Funktion för att uppdatera lagret på en produkt (ropar på MyInventory.py)

def UpdateStock(Inventory):
    Name = input("Sök på produkt: ")
    Results = Inventory.SearchProduct(Name)

    if not Results:
        print(f"Hittade inga produkter med namnet {Name}.")
        return

    # Vi skapar en lista med dictionaries från Metoden "SearchProduct" från classen "MyInventory"
    Product = Results[0]

    # Hämtar värdet för "Name" & "Stock" i våran lista vi just skapade och printar ut det.
    print(f"Namn: {Product['Name']}")
    print(f"Nuvarande lagersaldo: {Product['Stock']}")
    
    # Testar att värdet för input är ett tal
    try:
        Amount = int(input("Ange Mängd som du vill lägga till (använd negativa tal för att ta bort): "))
    except ValueError:
        print("Ogiltigt värde, ange ett heltal.")
        return
    
    # Verifiering att användaren verkligen vill uppdatera lagret.
    Confirm = input(f"Ska vi uppdatera {Product['Name']} med {Amount}? (Ja/Nej): ").lower()
    if Confirm != "ja":
        print("Uppdatering avbruten.")
        return
    if Inventory.UpdateStock(Name, Amount):
        print(f"Lagersaldo för {Product['Name']} har uppdaterats.")
    else: # Metoden "UpdateStock" för class "MyInventory" retunerar "False" utifall inventariet skulle bli negativt.
        print(f"Kunde ej uppdatera lagersaldo, kontrollera tillgängligt inventarie.")