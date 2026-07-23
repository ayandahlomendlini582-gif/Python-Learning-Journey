import tkinter 
window = tkinter.Tk()


window.title("Inventory Management System")
window.geometry("620x520")

frame = tkinter.Frame(window)
frame.pack()



name_label = tkinter.Label(window, text="Name: ")
name_entry = tkinter.Entry(window,)
name_label.pack()
name_entry.pack()

description_label = tkinter.Label(window, text="Description: ")
description_entry = tkinter.Entry(window,)
description_label.pack()
description_entry.pack()

quantity_label = tkinter.Label(window, text="Quantity: ")
quantity_entry = tkinter.Entry(window,)
quantity_label.pack()
quantity_entry.pack()

price_label = tkinter.Label(window, text="Price: ")
price_entry = tkinter.Entry(window,)
price_label.pack()
price_entry.pack()

add_btn = tkinter.Button(window, text="Add Product")
add_btn.pack()

update_btn = tkinter.Button(window, text="Update Product")
update_btn.pack()

delete_btn = tkinter.Button(window, text="Delete Product")
delete_btn.pack()





window.mainloop()