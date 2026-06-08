def AddProduct(Inventory): # "Inventory länkar mot objektet vi skapade i "MyProgram"
    Name = input("Produktnamn: ")
    Category = input("Kategori: ")
    Brand = input("Tillverkare: ")

    try: # säkerställer att vi får in ett tal
        Price = float(input("Pris: "))
    except ValueError:
        print("Ogiltigt pris, ange ett tal.")
        return
    
    try: # säkerställer att vi får in ett tal
        Stock = int(input("Antal i lager: "))
    except ValueError:
        print("Ogiltigt antal, ange ett tal.")
        return
    
    ExpiryDate = input("Utgångsdatum (ÅÅÅÅ-MM-DD): ")
    Strength = input("Styrka: ")
    Dosage = input("Dosering: ")
    Prescription = input("Receptbelgad (Ja/Nej): ").lower() == "ja"

    Inventory.AddProduct(Name, Category, Brand, Price, Stock, ExpiryDate, Strength, Dosage, Prescription)
    print(f"{Name} har lagts till!")
