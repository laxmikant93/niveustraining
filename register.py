import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Create a function to handle user registration
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    # Connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="user_registration"
        )
        cursor = connection.cursor()

        # Insert user data into the database
        insert_query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (username, password, email))
        connection.commit()

        messagebox.showinfo("Success", "Registration successful!")
        clear_entries()

    except mysql.connector.Error as err:
        print("Error:", err)
        messagebox.showerror("Error", "Registration failed!")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create a function to clear the entry fields
def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("User Registration Form")

# Create and place form elements
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

# Start the tkinter main loop
root.mainloop()
