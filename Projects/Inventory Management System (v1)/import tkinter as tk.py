0import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

# Ensure the table is created by calling the database function
def database():
    conn = sqlite3.connect("item_inventory.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Initialize the database (creates the table if it doesn't exist)
database()

def add_btn():
    if name.get() == "" or price.get() == "" or quantity.get() == "":
        messagebox.showwarning("Warning", "Please fill in the fields.")
    else:
        try:
            quantitys = int(quantity.get())
            prices = float(price.get())
            conn = sqlite3.connect("item_inventory.db")
            c = conn.cursor()
            c.execute("INSERT INTO items (name, description, quantity, price) VALUES (?, ?, ?, ?)",
                      (name.get(), description.get(), quantitys, prices))
            conn.commit()
            conn.close()
           
        except ValueError:
            messagebox.showwarning("Warning", "Please enter valid entries.")

# Remaining code is unchanged
# ...

root = tk.Tk()
root.geometry("700x480")
root.title("Inventory Management System")

name = tk.StringVar()
description = tk.StringVar()
quantity = tk.StringVar()
price = tk.StringVar()

# Define the UI components
frame1 = tk.Frame(root).grid(row=0, column=0, padx=5, pady=5)

name_label = tk.Label(frame1, text="Name:").grid(row=0, column=0, padx=10, pady=4, sticky="w")
description_label = tk.Label(frame1, text="Description:").grid(row=1, column=0, padx=10, pady=4, sticky="w")
quantity_label = tk.Label(frame1, text="Quantity:").grid(row=2, column=0, padx=10, pady=4, sticky="w")
price_label = tk.Label(frame1, text="Price:").grid(row=3, column=0, padx=10, pady=4, sticky="w")

name_entry = tk.Entry(frame1, width=30, textvariable=name).grid(row=0, column=1)
description_entry = tk.Entry(frame1, width=30, textvariable=description).grid(row=1, column=1)
quantity_entry = tk.Entry(frame1, width=30, textvariable=quantity).grid(row=2, column=1)
price_entry = tk.Entry(frame1, width=30, textvariable=price).grid(row=3, column=1)

adding_btn = tk.Button(frame1, text="Add Product", bg="lightgrey", command=add_btn).grid(row=5, column=0, padx=15, pady=5)
updating_btn = tk.Button(frame1, text="Update Product", bg="lightgrey", ).grid(row=5, column=1, padx=5, sticky="w")
deleting_btn = tk.Button(frame1, text="Delete Product", bg="lightgrey", ).grid(row=5, column=2, padx=5, sticky="w")

frame2 = tk.Frame(root).grid(row=1, column=0, pady=10, sticky="w")
show_product = tk.Text(frame2, wrap="word", width=60, height=15)
show_product.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=show_product.yview)
scrollbar.grid(row=6, column=3, sticky="ns", pady=11)
show_product.config(yscrollcommand=scrollbar.set)

frame3 = tk.Frame(root).grid(row=2, column=0, padx=5, pady=5, sticky="w")
sort_label = tk.Label(frame3, text="Sort by:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
n = tk.StringVar()
sort_menu = ttk.Combobox(frame3, textvariable=n, width=30)
sort_menu['values'] = ('Name', 'Price(High)', 'Price(Low)', 'Quantity')
sort_menu.grid(row=7, column=1, pady=5, sticky="w")

frame4 = tk.Frame(root).grid(row=3, column=0)
results_label = tk.Label(frame4, text="Total products:").grid(row=8, column=0, ipadx=1, pady=5, sticky="w")

root.mainloop()
