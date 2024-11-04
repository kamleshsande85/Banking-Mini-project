import sqlite3
import random
from tkinter import messagebox, simpledialog
import tkinter as tk
# from user_interface import BankingApp


class Database:
    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):

        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT UNIQUE NOT NULL,
                account_holder TEXT NOT NULL,
                dob TEXT NOT NULL,
                father_name TEXT,
                mother_name TEXT,
                address TEXT,
                bank_name TEXT,
                branch_name TEXT,
                mobile_number TEXT,
                account_type TEXT CHECK (account_type IN ('SAVING', 'CURRENT')) NOT NULL,
                balance REAL DEFAULT 0,
                role TEXT CHECK (role IN ('user', 'admin')) NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT,
                amount REAL NOT NULL,
                transaction_type TEXT CHECK (transaction_type IN ('deposit', 'withdraw')) NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_number) REFERENCES users(account_number)
            )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()

    # Add methods to interact with users and transactions (CRUD operations)

    def add_user(
        self,
        account_number,
        account_holder,
        balance,
        role,
        ppassword,
        date_of_birth,
        father_name,
        mother_name,
        address,
        bank_name,
        branch_name,
        mobile_number,
        account_type
    ):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO users (
            
                account_number,
                account_holder,
                balance,
                ppassword,
                role,
                dob,
                father_name,
                mother_name,
                address,
                bank_name,
                branch_name,
                mobile_number,
                account_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (

            account_number,
            account_holder,
            balance,
            ppassword,  # Ensure you are using ppassword here
            role,
            date_of_birth,
            father_name,
            mother_name,
            address,
            bank_name,
            branch_name,
            mobile_number,
            account_type
        ))
        self.connection.commit()

    def get_users(self, account_number):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT * FROM users where account_number=?', (account_number,))
        data = cursor.fetchall()
        # print(data)
        # print(type(data))
        return data

    def get_transactions(self, account_number):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT * FROM transactions WHERE account_number = ?', (account_number,))
        return cursor.fetchall()

    def add_transaction(self, account_number, amount, transaction_type):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO transactions (account_number, amount, transaction_type) VALUES (?, ?, ?)',
                       (account_number, amount, transaction_type))
        self.connection.commit()

    def update_balance(self, account_number, new_balance):
        cursor = self.connection.cursor()
        cursor.execute('UPDATE users SET balance = ? WHERE account_number = ?',
                       (new_balance, account_number))
        self.connection.commit()

    def get_balance(self, account_number):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT balance FROM users WHERE account_number = ?', (account_number,))
        data = cursor.fetchall()
        # print(data)
        return data[0][0]

    def generate_account_number(self):
        # Generate a random 8-digit number as a string
        return str(random.randint(10000000, 99999999)), str(random.randint(1000, 9999))

        # Example usage
        account_number = generate_account_number()
        print("Generated Account Number:", account_number)

    def deposit_by_admin(self):
        cursor = self.connection.cursor()
        account_number = simpledialog.askstring(
            "Account number", "Enter account number:")

        try:
            # Fetch the current balance for the specified account number
            cursor.execute(
                "SELECT balance FROM users WHERE account_number = ?", (account_number,))
            amount = cursor.fetchone()

            # Check if account exists
            if amount is None:
                raise ValueError("Account number does not exist.")

            deposit_amount = simpledialog.askfloat("Deposit", "Enter amount:")

            # Check if deposit amount is valid
            if deposit_amount is None or deposit_amount <= 0:
                raise ValueError("Please enter a valid deposit amount.")

            # Calculate the new balance
            new_amount = amount[0] + deposit_amount

            # Update the user's balance in the database
            cursor.execute(
                "UPDATE users SET balance = ? WHERE account_number = ?", (new_amount, account_number))
            self.connection.commit()  # Commit the changes

            # Inform the user about the successful transaction
            messagebox.showinfo("Success", f"Successfully deposited {
                                deposit_amount} into account {account_number}. New balance: {new_amount:.2f}")

        except ValueError as ve:
            # Handle specific value errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def widraw_by_admin(self):
        cursor = self.connection.cursor()
        account_number = simpledialog.askstring(
            "Account number", "Enter account number:")

        try:
            # Fetch the current balance for the specified account number
            cursor.execute(
                "SELECT balance FROM users WHERE account_number = ?", (account_number,))
            amount = cursor.fetchone()

            # Check if account exists
            if amount is None:
                raise ValueError("Account number does not exist.")

            deposit_amount = simpledialog.askfloat("Deposit", "Enter amount:")

            # Check if deposit amount is valid
            if deposit_amount is None or deposit_amount <= 0:
                raise ValueError("Please enter a valid deposit amount.")

            # Calculate the new balance
            new_amount = amount[0] - deposit_amount

            # Update the user's balance in the database
            cursor.execute(
                "UPDATE users SET balance = ? WHERE account_number = ?", (new_amount, account_number))
            self.connection.commit()  # Commit the changes

            # Inform the user about the successful transaction
            messagebox.showinfo("Success", f"Successfully Widrew {
                                deposit_amount} into account {account_number}. New balance: {new_amount:.2f}")

        except ValueError as ve:
            # Handle specific value errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def view_transaction_by_admin(self):
        cursor = self.connection.cursor()
        account_number = simpledialog.askstring(
            "Account number", "Enter account number:")

        try:
            cursor.execute(
                "select * from transactions where account_number = ?", (account_number,))
            data = cursor.fetchall()

            # self.connection.commit()  # Commit the changes

            # Inform the user about the successful transaction
            messagebox.showinfo("Transaction", f"Transaction history\n {data}")

        except ValueError as ve:
            # Handle specific value errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def check_by_admin(self):
        cursor = self.connection.cursor()
        account_number = simpledialog.askstring(
            "Account number", "Enter account number:")

        try:
            # Fetch the current balance for the specified account number
            cursor.execute(
                "SELECT balance FROM users WHERE account_number = ?", (account_number,))
            amount = cursor.fetchone()

            # Check if account exists
            if amount is None:
                raise ValueError("Account number does not exist.")

            # Inform the user about the successful transaction
            messagebox.showinfo("Balance ", f"Your balance is {amount[0]}")

        except ValueError as ve:
            # Handle specific value errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def add_user_by_admin(self):
        # Create a new Toplevel window for account creation by admin
        frame = tk.Toplevel(bg="#053048")
        frame.title("Account Creation by Admin")
        frame.geometry("800x600")

        tk.Label(frame, text="Create Account", font=("Arial", 20),
                 bg="#053048", fg="#FCFBFA").grid(row=0, columnspan=2, pady=20)

        # Account Holder Name
        tk.Label(frame, text="Account Holder Name:", bg="#053048",
                 fg="#FCFBFA").grid(row=1, column=0, padx=5, pady=10)
        self.holder_name_entry = tk.Entry(frame)
        self.holder_name_entry.grid(row=1, column=1, padx=5, pady=10)

        # Date of Birth
        tk.Label(frame, text="Date of Birth (DD/MM/YYYY):", bg="#053048",
                 fg="#FCFBFA").grid(row=2, column=0, padx=5, pady=10)
        self.dob_entry = tk.Entry(frame)
        self.dob_entry.grid(row=2, column=1, padx=5, pady=10)

        # Father's Name
        tk.Label(frame, text="Father's Name:", bg="#053048",
                 fg="#FCFBFA").grid(row=3, column=0, padx=5, pady=10)
        self.father_name_entry = tk.Entry(frame)
        self.father_name_entry.grid(row=3, column=1, padx=5, pady=10)

        # Mother's Name
        tk.Label(frame, text="Mother's Name:", bg="#053048",
                 fg="#FCFBFA").grid(row=4, column=0, padx=5, pady=10)
        self.mother_name_entry = tk.Entry(frame)
        self.mother_name_entry.grid(row=4, column=1, padx=5, pady=10)

        # Address
        tk.Label(frame, text="Address:", bg="#053048", fg="#FCFBFA").grid(
            row=5, column=0, padx=5, pady=10)
        self.address_entry = tk.Entry(frame)
        self.address_entry.grid(row=5, column=1, padx=5, pady=10)

        # Bank Name
        tk.Label(frame, text="Bank Name:", bg="#053048", fg="#FCFBFA").grid(
            row=6, column=0, padx=5, pady=10)
        self.bank_name_entry = tk.Entry(frame)
        self.bank_name_entry.grid(row=6, column=1, padx=5, pady=10)

        # Branch Name
        tk.Label(frame, text="Branch Name:", bg="#053048",
                 fg="#FCFBFA").grid(row=7, column=0, padx=5, pady=10)
        self.branch_name_entry = tk.Entry(frame)
        self.branch_name_entry.grid(row=7, column=1, padx=5, pady=10)

        # Mobile Number
        tk.Label(frame, text="Mobile Number:", bg="#053048",
                 fg="#FCFBFA").grid(row=8, column=0, padx=5, pady=10)
        self.mobile_number_entry = tk.Entry(frame)
        self.mobile_number_entry.grid(row=8, column=1, padx=5, pady=10)

        # Account Type
        tk.Label(frame, text="Account Type:", bg="#053048",
                 fg="#FCFBFA").grid(row=9, column=0, padx=5, pady=10)
        self.account_type_var = tk.StringVar(value="SAVING")
        tk.Radiobutton(frame, text="SAVING", variable=self.account_type_var,
                       value="SAVING", bg="#053048").grid(row=9, column=1, padx=5, pady=10)
        tk.Radiobutton(frame, text="CURRENT", variable=self.account_type_var,
                       value="CURRENT", bg="#053048").grid(row=9, column=2, padx=5, pady=10)

        # Create Button
        tk.Button(frame, text="Create", command=self.create_new_account, bg="#053048",
                  fg="#FCFBFA", width=15).grid(row=11, columnspan=2, padx=5, pady=10)

        # Close Button
        tk.Button(frame, text="Close", command=frame.destroy, bg="#053048",
                  fg="#FCFBFA", width=15).grid(row=12, columnspan=2, padx=5, pady=10)

    def create_new_account(self):

        account_number, ppassword = self.generate_account_number()
        account_holder = self.holder_name_entry.get()
        # password = self.new_password_entry.get()
        # user_id = self.user_id
        # account_number = account_number
        # account_holder = account_holder
        balance = 0.0  # or another default value
        role = 'user'  # or 'admin' if applicable
        # ppassword = password,  # password or encrypted password
        date_of_birth = self.dob_entry.get()
        father_name = self.father_name_entry.get()
        mother_name = self.mother_name_entry.get()
        address = self.address_entry.get()
        bank_name = self.bank_name_entry.get()
        branch_name = self.branch_name_entry.get()
        mobile_number = self.mobile_number_entry.get()
        account_type = self.account_type_var.get()
        print(account_number,
              account_holder,
              balance,
              role,
              ppassword,
              date_of_birth,
              father_name,
              mother_name,
              address,
              bank_name,
              branch_name,
              mobile_number,
              account_type)

        if account_number and account_holder and ppassword:
            try:
                # self.db.add_user(self.user_id, account_number,
                #                  account_holder, password)
                self.add_user(
                    account_number,
                    account_holder,
                    balance,
                    role,
                    ppassword,
                    date_of_birth,
                    father_name,
                    mother_name,
                    address,
                    bank_name,
                    branch_name,
                    mobile_number,
                    account_type
                )

                messagebox.showinfo(
                    "Success", f"Account created successfully!\nYour account number is {account_number}\nPassword is {ppassword}")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to create account: {str(e)}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def remove_user_by_admin(self):

        cursor = self.connection.cursor()
        account_number = simpledialog.askstring(
            "Account number", "Enter account number to delete:")

        try:
            # Check if the account exists
            cursor.execute(
                "SELECT * FROM users WHERE account_number = ?", (account_number,))
            user = cursor.fetchone()

            if user is None:
                raise ValueError("Account number does not exist.")

            # Proceed to delete the record
            cursor.execute(
                "DELETE FROM users WHERE account_number = ?", (account_number,))
            self.connection.commit()  # Commit the changes

            # Inform the user about the successful deletion
            messagebox.showinfo("Success", f"Account number {
                                account_number} has been deleted successfully.")

        except ValueError as ve:
            # Handle specific value errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
