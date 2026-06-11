import os
from MyClasses import FileProcessor

FP = FileProcessor()

with open(FP.MyDataFile, "r", encoding="utf-8-sig") as f:
    Lines = f.readlines()
    print("Antal rader i filen:", len(Lines))
    print("Sista raden:", repr(Lines[-1]))