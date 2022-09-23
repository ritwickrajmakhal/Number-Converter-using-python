import tkinter as tk
import main

def evaluate():
    main.calculate(clicked1,clicked2,input.get(),output)
root = tk.Tk()
root.title("Number Converter")
root.resizable(False,False)
padding = {'padx': 5, 'pady': 5}

# Adjust size
root.geometry( "772x250" )
  
# Dropdown menu options
options = [
    "Decimal",
    "Binary",
    "Octal",
    "HexaDecimal"
]
  
# datatype of menu text
clicked1 = tk.StringVar()
clicked2 = tk.StringVar()

# initial menu text
clicked1.set( "Decimal" )
clicked2.set( "Decimal" )

# Create labels
label1 = tk.Label(root,text="From:",font=("Arial", 12),**padding)
label2 = tk.Label(root,text="To:",font=("Arial", 12),**padding)

# Create Dropdown menu
drop1 = tk.OptionMenu( root , clicked1 , *options )
drop2 = tk.OptionMenu( root , clicked2 , *options )
# Create Text Box for inputs
input = tk.StringVar()
output = tk.StringVar()
e1 = tk.Entry(root,textvariable=input,font=("Arial",12))
e2 = tk.Entry(root,state=tk.DISABLED,textvariable=output,font=("Arial",12))
# Create 'Calculate' Button
btn = tk.Button(root,text="Calculate",background="green",font=("Arial", 10),command=evaluate,**padding)

label1.pack(side=tk.LEFT)
drop1.pack(side=tk.LEFT)
e1.pack(side=tk.LEFT)
e2.pack(side=tk.RIGHT)
drop2.pack(side=tk.RIGHT)
label2.pack(side=tk.RIGHT)
btn.pack(side=tk.BOTTOM)

root.mainloop()