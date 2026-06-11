# Class för att läsa in och spara data.

# Importerar OS för att kunna hantera sökvägar och CSV för att kunna hantera lagring i CSV filer.
import os, csv 

class FileProcessor:
    def __init__(self):
        # Fördefinerar attributer för att kunna skapa sökvägen till fil och mapp.
        self.MyFolder = os.path.dirname(os.path.abspath(__file__)) # Hittar vart huvudmappen finns
        self.MyDataFolder = os.path.join(self.MyFolder, "MyData") # Lägger till fillmappen till sökvägen
        self.MyDataFile = os.path.join(self.MyDataFolder, "inventory.csv") # lägger till filnamnet till sökvägen.

        # Fördefinerar en header för våran CSV-fil
        self.MyHeader = ["Name", "Category", "Brand", "Price", "Stock", "ExpiryDate", "Prescription", "Strength", "Dosage"]

    # Module för att kontrollera om filen finns och skapa den utifall den saknas. 
    def CheckPath(self):
        os.makedirs(self.MyDataFolder, exist_ok=True) # Kollar om mappen finns.
        if not os.path.exists(self.MyDataFile):
            with open(self.MyDataFile, "w", newline="", encoding="utf-8") as content:
                writer = csv.writer(content)
                writer.writerow(self.MyHeader)
    
    # Module för att läsa in data från CSV till dictionary.
    def ReadData(self):
        self.CheckPath()

        with open(self.MyDataFile, "r", encoding="utf-8-sig") as content:
            reader = csv.DictReader(content)
            return list(reader)

    # Module för att spara data till CSV.
    def SaveData(self, MyProducts):
        with open(self.MyDataFile, "w", newline="", encoding="utf-8") as content:
            writer = csv.DictWriter(content, fieldnames=self.MyHeader)
            writer.writeheader()
            writer.writerows(MyProducts)