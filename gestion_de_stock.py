import mysql.connector
from tkinter import *
from tkinter import messagebox

cnx = mysql.connector.connect(user='root', password='noah06600', host='localhost')
cursor = cnx.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS store")

cursor.execute("USE store")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        price INT,
        quantity INT,
        id_category INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
""")

cursor.execute("INSERT INTO category (name) VALUES ('Electronics'), ('Clothing'), ('Food')")

cursor.execute("""
    INSERT INTO product (name, description, price, quantity, id_category) 
    VALUES 
        ('iPhone', 'Latest model', 1000, 10, 1),
        ('T-shirt', '100% cotton', 20, 50, 2),
        ('Bread', 'Freshly baked', 3, 100, 3)
""")

cnx.commit()

window = Tk()
window.title("Stock Management")

def add_product():
    name = name_entry.get()
    description = description_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    id_category = id_category_entry.get()

    cursor.execute("""
        INSERT INTO product (name, description, price, quantity, id_category) 
        VALUES (%s, %s, %s, %s, %s)
    """, (name, description, price, quantity, id_category))

    cnx.commit()

    messagebox.showinfo("Success", "Product added successfully")

name_entry = Entry(window)
name_entry.pack()
description_entry = Entry(window)
description_entry.pack()
price_entry = Entry(window)
price_entry.pack()
quantity_entry = Entry(window)
quantity_entry.pack()
id_category_entry = Entry(window)
id_category_entry.pack()

add_button = Button(window, text="Add Product", command=add_product)
add_button.pack()

window.mainloop()

cursor.close()
cnx.close()
