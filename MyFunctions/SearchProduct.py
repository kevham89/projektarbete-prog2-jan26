# Funktion för att söka på en produkt (ropar på MyInventory.py)

def SearchProduct(Inventory): # funktionen tar emot "Inventory"
    Name = input("Sök på produkt: ") 
    Results = Inventory.SearchProduct(Name) # Vi söker på användarens input i "Inventory" som vi tog emot i tidigare steget.

    if not Results: # om vi inte får något träff på input så skriver vi ut det här meddelandet.
        print(f"Hittade inget på {Name}")
        return
    else: 
        print(f"Vi hittade {len(Results)} produkter.") # Använder "len" för att räkna hur många produkter som vi hittade.
        for Product in Results: # för varje träff så skriver vi ut all
            print("----------------------------------------") # Ramar in varje enskild produkt.
            print(f"Namn: {Product['Name']}")
            print(f"Kategori {Product['Category']}")
            print(f"Tillverkare: {Product['Tillverkare']}")
            print(f"Pris: {Product['Price']}")
            print(f"Lager: {Product['Stock']}")
            print(f"Utgångsdatum: {Product['ExpiryDate']}")
            print(f"Receptbelagd: {Product['Prescription']}")
            print(f"Styrka: {Product['Strength']}")
            print(f"Dosering: {Product['Dosage']}")
