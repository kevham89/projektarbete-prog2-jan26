import tkinter as tk
from tkinter import ttk, messagebox
from MyClasses import FileProcessor, MyInventory
from MyFunctions import ShowMenu, AddProduct, SearchProduct, UpdateStock, RemoveProduct, RefreshTree

root = tk.Tk()
root.title("Apotek")
root.geometry("800x600")

FP = FileProcessor()
Inventory = MyInventory(FP)

# Header
Header = tk.Label(root, text="Apotek", font=("Arial", 14, "bold" ))
Header.pack(pady=10)

# Skapar 2 frames, vänster & höger, och ramar in dessa i "Main". 
MainFrame = tk.Frame(root)
MainFrame.pack(fill="x")
LeftFrame = tk.Frame(MainFrame)
LeftFrame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
RightFrame = tk.Frame(MainFrame)
RightFrame.grid(row=0, column=1, pady=10, padx=10, sticky="n")

MainFrame.columnconfigure(0, weight=1)
MainFrame.columnconfigure(1, weight=1)

# LeftFrame
UserInput = tk.Frame(LeftFrame)
UserInput.pack()

DicHeader = {}

ListHeader = [
    "Namn",
    "Kategori",
    "Tillverkare",
    "Pris",
    "Lagersaldo",
    "Utgångsdatum",
    "Styrka",
    "Dosering",
    "Receptbelagd",
]

for RowIndex, HeaderText in enumerate(ListHeader):
    tk.Label(UserInput, text=HeaderText, width=15, anchor="w").grid(row=RowIndex, column=0, pady=2)

    entry = tk.Entry(UserInput, width=25)
    entry.grid(row=RowIndex, column=1, pady=2)

    DicHeader[HeaderText] = entry

# RightFrame

button1 = tk.Button(RightFrame, text="Lägg Till Produkt", bg="green", fg="white", width=20, command=lambda: AddProduct(Inventory, DicHeader, Tree, RefreshTree))
button1.pack(pady=5) # Fill "x" betyder att vi sträcker ut knappen från höger till vänster.
button2 = tk.Button(RightFrame, text="Sök Efter Produkt", bg="orange", fg="white", width=20, command=lambda: SearchProduct(Inventory, DicHeader, Tree))
button2.pack(pady=5) 
button3 = tk.Button(RightFrame, text="Updatera Lagersaldo", bg="blue", fg="white", width=20, command=lambda: UpdateStock(Inventory, DicHeader, Tree, RefreshTree))
button3.pack(pady=5) 
button4 = tk.Button(RightFrame, text="Ta Bort Produkt", bg="red", fg="white", width=20, command=lambda: RemoveProduct(Inventory, DicHeader, Tree, RefreshTree))
button4.pack(pady=5) 
button5 = tk.Button(RightFrame, text="Avsluta Program", bg="black", fg="white", width=20, command=root.destroy)
button5.pack(pady=5) 


# Tree (Sträcker sig över båda frames).

TreeFrame = tk.Frame(root)
TreeFrame.pack(fill="both", expand=True, padx=10, pady=10)

Tree = ttk.Treeview(TreeFrame, columns=("Name","Category","Brand","Price","Stock","ExpiryDate","Prescription","Strength","Dosage"), show="headings")

for Col in Tree["columns"]:
    Tree.heading(Col, text=Col, anchor="w")
    Tree.column(Col, width=80)

Tree.pack(fill="both", expand=True)

RefreshTree(Tree, Inventory)

root.mainloop()