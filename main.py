import tkinter as tk
import number_system as ns

def calculate(btn1,btn2,input,output):
    From = btn1.get()
    To = btn2.get()
    if From == To:
        output.set(input)
        return
    if From == "HexaDecimal":
        if To == "Decimal":
            out = ns.hex_To_dec(input)
        elif To == "Binary":
            out = ns.hex_To_bin(input)
        elif To == "Octal":
            out = ns.hex_To_oct(input)
    if From == "Octal":
        if To == "Decimal":
            out = ns.oct_To_dec(input)
        elif To == "Binary":
            out = ns.oct_To_bin(input)
        elif To == "HexaDecimal":
            out = ns.oct_To_hex(input)
    if From == "Binary":
        if To == "Decimal":
            out = ns.bin_To_dec(input)
        elif To == "HexaDecimal":
            out = ns.bin_To_hex(input)
        elif To == "Octal":
            out = ns.bin_To_oct(input)
    if From == "Decimal":
        if To == "Octal":
            out = ns.dec_To_oct(input)
        elif To == "Binary":
            out = ns.dec_To_bin(input)
        elif To == "HexaDecimal":
            out = ns.dec_To_hex(input)
    output.set(out)
        
