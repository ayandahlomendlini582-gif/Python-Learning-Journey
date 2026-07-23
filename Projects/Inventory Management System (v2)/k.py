import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

# Database setup
def create_db():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

# Functions for product operations
def add_product():
    if name_var.get() == "" or quantity_var.get() == "" or price_var.get() == "":
        messagebox.showwarning("Input Error", "Please fill in all fields")
    else:
        try:
            quantity = int(quantity_var.get())
            price = float(price_var.get())
            conn = sqlite3.connect("inventory.db")
            c = conn.cursor()
            c.execute("INSERT INTO products (name, description, quantity, price) VALUES (?, ?, ?, ?)",
                      (name_var.get(), description_var.get(), quantity, price))
            conn.commit()
            conn.close()
            display_products()
            clear_entries()
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity and price must be numbers")

def update_product():
    selected_id = get_selected_product_id()
    if selected_id is None:
        pass
    else:
        try:
            quantity = int(quantity_var.get())
            price = float(price_var.get())
            conn = sqlite3.connect("inventory.db")
            c = conn.cursor()
            c.execute("UPDATE products SET name=?, description=?, quantity=?, price=? WHERE id=?",
                      (name_var.get(), description_var.get(), quantity, price, selected_id))
            conn.commit()
            conn.close()
            display_products()
            clear_entries()
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity and price must be numbers")

def delete_product():
    selected_id = get_selected_product_id()
    if selected_id is None:
        pass
    else:
        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE id=?", (selected_id,))
        conn.commit()
        conn.close()
        display_products()

def get_selected_product_id():
    try:
        return int(product_text.get(product_text.curselection()).split()[1])
    except:
        messagebox.showwarning("Selection Error", "No product selected")
        return None

def display_products(sort_by=None, ascending=True):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    if ascending:
        order = "ASC"
    else:
        order = "DESC"
    query = f"SELECT * FROM products ORDER BY {sort_by if sort_by else 'id'} {order}"
    c.execute(query)
    products = c.fetchall()
    conn.close()

    product_text.delete(1.0, END)
    for product in products:
        product_text.insert(END, f"ID: {product[0]}\nName: {product[1]}\nDescription: {product[2]}\nQuantity: {product[3]}\nPrice: ${product[4]:.2f}\n{'-'*40}\n")
    status_label.config(text=f"Total products: {len(products)}")

def clear_entries():
    name_var.set("")
    description_var.set("")
    quantity_var.set("")
    price_var.set("")

def sort_products():
    sort_option = sort_combobox.get()
    if sort_option == "Name (A-Z)":
        display_products("name", ascending=True)
    elif sort_option == "Name (Z-A)":
        display_products("name", ascending=False)
    elif sort_option == "Price (Low-High)":
        display_products("price", ascending=True)
    elif sort_option == "Price (High-Low)":
        display_products("price", ascending=False)
    elif sort_option == "Quantity (Low-High)":
        display_products("quantity", ascending=True)
    else:
        display_products("quantity", ascending=False)

# GUI setup
app = Tk()
app.title("Inventory Management System")
app.geometry("500x450")

# Entry fields for product details
name_var = StringVar()
description_var = StringVar()
quantity_var = StringVar()
price_var = StringVar()

Label(app, text="Name:").grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")
Entry(app, textvariable=name_var, width=40).grid(row=0, column=1, padx=5, pady=5)

Label(app, text="Description:").grid(row=1, column=0, padx=(10, 5), pady=5, sticky="w")
Entry(app, textvariable=description_var, width=40).grid(row=1, column=1, padx=5, pady=5)

Label(app, text="Quantity:").grid(row=2, column=0, padx=(10, 5), pady=5, sticky="w")
Entry(app, textvariable=quantity_var, width=40).grid(row=2, column=1, padx=5, pady=5)

Label(app, text="Price:").grid(row=3, column=0, padx=(10, 5), pady=5, sticky="w")
Entry(app, textvariable=price_var, width=40).grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = Frame(app)
button_frame.grid(row=4, column=0, columnspan=2, pady=5)
Button(button_frame, text="Add Product", command=add_product).pack(side="left", padx=5)
Button(button_frame, text="Update Product", command=update_product).pack(side="left", padx=5)
Button(button_frame, text="Delete Product", command=delete_product).pack(side="left", padx=5)

# Text widget for displaying products with a scrollbar
product_text = Text(app, width=58, height=10, wrap="none")
product_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
scrollbar = Scrollbar(app, orient=VERTICAL, command=product_text.yview)
scrollbar.grid(row=5, column=2, sticky="ns")
product_text.config(yscrollcommand=scrollbar.set)

# Combobox for sorting options
Label(app, text="Sort by:").grid(row=6, column=0, padx=(10, 5), pady=10, sticky="w")
sort_combobox = ttk.Combobox(app, values=["Name (A-Z)", "Name (Z-A)", "Price (Low-High)", "Price (High-Low)", "Quantity (Low-High)", "Quantity (High-Low)"], width=20)
sort_combobox.grid(row=6, column=1, sticky="w")
sort_combobox.bind("<<ComboboxSelected>>", lambda event: sort_products())

# Status bar
status_label = Label(app, text="Total products: 0", anchor="w")
status_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Initialize database and display products
create_db()
display_products()
app.mainloop()
