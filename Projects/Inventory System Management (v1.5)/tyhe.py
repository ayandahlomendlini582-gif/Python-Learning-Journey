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

# Function to add product
def add_product():
    if name_var.get() == "" or quantity_var.get() == "" or price_var.get() == "":
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return
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

# Function to update product
def update_product():
    selected_id = get_selected_product_id()
    if not selected_id:
        return
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

# Function to delete product
def delete_product():
    selected_id = get_selected_product_id()
    if not selected_id:
        return
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id=?", (selected_id,))
    conn.commit()
    conn.close()
    display_products()

# Get selected product ID from text widget
def get_selected_product_id():
    try:
        return int(product_text.get(product_text.curselection()).split()[0])
    except:
        messagebox.showwarning("Selection Error", "No product selected")
        return None

# Function to display products in the Text widget
def display_products(sort_by=None, ascending=True):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    order = "ASC" if ascending else "DESC"
    query = f"SELECT * FROM products ORDER BY {sort_by if sort_by else 'id'} {order}"
    c.execute(query)
    products = c.fetchall()
    conn.close()

    product_text.delete(1.0, END)  # Clear Text widget contents
    for product in products:
        product_text.insert(END, f"{product[0]} - {product[1]}, {product[2]}, Qty: {product[3]}, Price: ${product[4]}\n")
    status_label.config(text=f"Total Products: {len(products)}")

# Function to clear entry fields
def clear_entries():
    name_var.set("")
    description_var.set("")
    quantity_var.set("")
    price_var.set("")

# Function to sort products
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
    elif sort_option == "Quantity (High-Low)":
        display_products("quantity", ascending=False)

# Initialize main application window
app = Tk()
app.title("Inventory Management System")
app.geometry("600x400")

# Entry fields for product details
name_var = StringVar()
description_var = StringVar()
quantity_var = StringVar()
price_var = StringVar()

Label(app, text="Name:").grid(row=0, column=0, padx=10, pady=5)
Entry(app, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

Label(app, text="Description:").grid(row=1, column=0, padx=10, pady=5)
Entry(app, textvariable=description_var).grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
Entry(app, textvariable=quantity_var).grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Price:").grid(row=3, column=0, padx=10, pady=5)
Entry(app, textvariable=price_var).grid(row=3, column=1, padx=10, pady=5)

# Buttons for add, update, delete
Button(app, text="Add Product", command=add_product).grid(row=4, column=0, padx=10, pady=5)
Button(app, text="Update Product", command=update_product).grid(row=4, column=1, padx=10, pady=5)
Button(app, text="Delete Product", command=delete_product).grid(row=4, column=2, padx=10, pady=5)

# Text widget and scrollbar for displaying products
product_text = Text(app, width=50, height=10, wrap=NONE)
product_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
scrollbar = Scrollbar(app, orient=VERTICAL, command=product_text.yview)
scrollbar.grid(row=5, column=3, sticky="ns")
product_text.config(yscrollcommand=scrollbar.set)

# Combobox for sorting options
sort_combobox = ttk.Combobox(app, values=["Name (A-Z)", "Name (Z-A)", "Price (Low-High)", "Price (High-Low)", "Quantity (Low-High)", "Quantity (High-Low)"])
sort_combobox.grid(row=6, column=0, padx=10, pady=10)
sort_combobox.bind("<<ComboboxSelected>>", lambda event: sort_products())

# Label for status bar
status_label = Label(app, text="Total Products: 0")
status_label.grid(row=7, column=0, columnspan=3, pady=10)

# Initialize database and display products
create_db()
display_products()

app.mainloop()
