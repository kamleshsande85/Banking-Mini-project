import tkinter as tk
from tkinter import messagebox, simpledialog
from models import Database


class BankingApp:
    def __init__(self):
        self.db = Database()
        self.window = tk.Tk()
        self.window.title("Banking Application")
        self.window.geometry("900x600")
        self.window.config(bg="#053048")
        self.current_account = None  # Track the logged-in account
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_window()

        tk.Label(self.window, text="Welcome to Banking App",
                 font=("Arial", 20), bg="#053048", fg="#FCFBFA").pack(pady=20)

        tk.Button(self.window, text="Login", command=self.login,
                  bg="#053048", fg="#FCFBFA", width=10).pack(pady=10)
        tk.Button(self.window, text="Admin Login", command=self.admin,
                  bg="#053048", fg="#FCFBFA", width=10).pack(pady=10)
        tk.Button(self.window, text="Create Account",
                  command=self.create_account,  bg="#053048", fg="#FCFBFA", width=10).pack(pady=10)

    def login(self):
        self.clear_window()
        tk.Label(self.window, text="Login", font=("Arial", 20),
                 bg="#053048", fg="#FCFBFA").pack(pady=20)

        tk.Label(self.window, text="Account Number:",
                 bg="#053048", fg="#FCFBFA").pack()
        self.account_number_entry = tk.Entry(self.window)
        self.account_number_entry.pack()

        tk.Label(self.window, text="Password:",
                 bg="#053048", fg="#FCFBFA").pack()
        self.password_entry = tk.Entry(
            self.window, show="*")  # Hide password input
        self.password_entry.pack()

        tk.Button(self.window, text="Login", bg="#053048",
                  fg="#FCFBFA", command=self.login_user).pack(pady=10)
        tk.Button(self.window, text="Back", bg="#053048", fg="#FCFBFA",
                  command=self.create_login_screen).pack(pady=10)

    def login_user(self):
        account_number = self.account_number_entry.get()
        print(type(account_number))
        password = self.password_entry.get()
        print(type(password))
        user = self.db.get_users(account_number)

        if user and user[0][13] == password:  # Check if the password matches
            self.current_account = account_number
            self.create_user_dashboard()
        else:
            messagebox.showerror(
                "Error", "Invalid account number or password.")

    def create_account(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="Create Account",
                 font=("Arial", 20), bg="#053048", fg="#FCFBFA").grid(row=0, columnspan=2, pady=20)

        tk.Label(frame, text="Account Holder Name:", bg="#053048", fg="#FCFBFA").grid(
            row=1, column=0, padx=5, pady=10)
        self.holder_name_entry = tk.Entry(frame)
        self.holder_name_entry.grid(row=1, column=1, padx=5, pady=10)

        tk.Label(frame, text="Date of Birth (DD/MM/YYYY):", bg="#053048", fg="#FCFBFA").grid(row=2,
                                                                                             column=0, padx=5, pady=10)
        self.dob_entry = tk.Entry(frame)
        self.dob_entry.grid(row=2, column=1, padx=5, pady=10)

        tk.Label(frame, text="Father's Name:", bg="#053048", fg="#FCFBFA").grid(
            row=3, column=0, padx=5, pady=10)
        self.father_name_entry = tk.Entry(frame)
        self.father_name_entry.grid(row=3, column=1, padx=5, pady=10)

        tk.Label(frame, text="Mother's Name:", bg="#053048", fg="#FCFBFA").grid(
            row=4, column=0, padx=5, pady=10)
        self.mother_name_entry = tk.Entry(frame)
        self.mother_name_entry.grid(row=4, column=1, padx=5, pady=10)

        tk.Label(frame, text="Address:", bg="#053048", fg="#FCFBFA").grid(
            row=5, column=0, padx=5, pady=10)
        self.address_entry = tk.Entry(frame)
        self.address_entry.grid(row=5, column=1, padx=5, pady=10)

        tk.Label(frame, text="Bank Name:", bg="#053048", fg="#FCFBFA").grid(
            row=6, column=0, padx=5, pady=10)
        self.bank_name_entry = tk.Entry(frame)
        self.bank_name_entry.grid(row=6, column=1, padx=5, pady=10)

        tk.Label(frame, text="Branch Name:", bg="#053048", fg="#FCFBFA").grid(
            row=7, column=0, padx=5, pady=10)
        self.branch_name_entry = tk.Entry(frame)
        self.branch_name_entry.grid(row=7, column=1, padx=5, pady=10)

        tk.Label(frame, text="Mobile Number:", bg="#053048", fg="#FCFBFA").grid(
            row=8, column=0, padx=5, pady=10)
        self.mobile_number_entry = tk.Entry(frame)
        self.mobile_number_entry.grid(row=8, column=1, padx=5, pady=10)

        tk.Label(frame, text="Account Type:", bg="#053048", fg="#FCFBFA").grid(
            row=9, column=0, padx=5, pady=10)
        self.account_type_var = tk.StringVar(value="SAVING")
        tk.Radiobutton(frame, text="SAVING", variable=self.account_type_var,
                       value="SAVING", bg="#053048").grid(row=9, column=1, padx=5, pady=10)
        tk.Radiobutton(frame, text="CURRENT", variable=self.account_type_var,
                       value="CURRENT", bg="#053048").grid(row=9, column=2, padx=5, pady=10)

        tk.Button(frame, text="Create",
                  command=self.create_new_account, bg="#053048", fg="#FCFBFA", width=15).grid(row=11, columnspan=2, padx=5, pady=10)
        tk.Button(frame, text="Back",
                  command=self.create_login_screen, bg="#053048", fg="#FCFBFA", width=15).grid(row=12, columnspan=2, padx=5, pady=10)

    def create_new_account(self):

        account_number, ppassword = self.db.generate_account_number()
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
                self.db.add_user(
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
                self.create_login_screen()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to create account: {str(e)}")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def create_user_dashboard(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="User Dashboard", font=(
            "Arial", 20), bg="#053048", fg="#FCFBFA").pack()

        tk.Button(frame, text="Deposit",
                  command=self.deposit, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Withdraw",
                  command=self.withdraw, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Check Balance",
                  command=self.check_balance, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="View Transactions",
                  command=self.view_transactions, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Logout",
                  command=self.logout, bg="#053048", fg="#FCFBFA", width=10).pack(pady=15)

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount > 0:
            # print(self.current_account)
            self.db.add_transaction(self.current_account, amount, 'deposit')
            new_balance = self.db.get_balance(self.current_account) + amount
            self.db.update_balance(self.current_account, new_balance)
            messagebox.showinfo("Success", f"Deposited: {
                                amount}. New Balance: {new_balance}")
        else:
            messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        current_balance = self.db.get_balance(self.current_account)
        if amount > 0 and amount <= current_balance:
            self.db.add_transaction(self.current_account, amount, 'withdraw')
            new_balance = current_balance - amount
            self.db.update_balance(self.current_account, new_balance)
            messagebox.showinfo("Success", f"Withdrew: {
                                amount}. New Balance: {new_balance}")
        else:
            messagebox.showerror(
                "Error", "Invalid amount or insufficient balance.")

    def check_balance(self):
        balance = self.db.get_balance(self.current_account)
        messagebox.showinfo("Balance", f"Current Balance: {balance}")

    def view_transactions(self):
        transactions = self.db.get_transactions(self.current_account)
        transaction_history = "\n".join(
            [f"{t[3]}: {t[2]} - {t[1]}" for t in transactions])
        if transaction_history:
            messagebox.showinfo("Transaction History", transaction_history)
        else:
            messagebox.showinfo("Transaction History",
                                "No transactions found.")

    def logout(self):
        self.current_account = None
        self.create_login_screen()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def admin(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="Admin Login", bg="#053048",
                 fg="#FCFBFA").grid(row=0, columnspan=2, padx=5, pady=15)
        tk.Label(frame, text="User ID", bg="#053048",
                 fg="#FCFBFA").grid(row=1, column=0, padx=5, pady=15)

        # Store Entry widget in an instance variable for later access
        self.admin_entry = tk.Entry(frame)
        self.admin_entry.grid(row=1, column=1)

        tk.Label(frame, text="Password", bg="#053048",
                 fg="#FCFBFA").grid(row=2, column=0, padx=5, pady=15)

        # Store Entry widget in an instance variable for later access
        self.admin_password = tk.Entry(frame, show="*")
        self.admin_password.grid(row=2, column=1)

        tk.Button(frame, text="Login", bg="#053048", fg="#FCFBFA", command=self.adminLogin).grid(
            row=3, columnspan=2, padx=5, pady=15)
        tk.Button(self.window, text="Back", bg="#053048", fg="#FCFBFA",
                  command=self.create_login_screen).pack(pady=10)

    def adminLogin(self):
        user_id = self.admin_entry.get()
        password = self.admin_password.get()

        if user_id == "Yaman" and password == "8520":
            self.adminDasbord()
        else:
            messagebox.showerror("Wrong details", "Wrong user ID or password")

    def adminDasbord(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="Admin Dashboard", font=(
            "Arial", 20), bg="#053048", fg="#FCFBFA").pack()

        tk.Button(frame, text="User Management",
                  command=self.admin_user_management, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Transaction Monitoring",
                  command=self.Transaction_Monitoring, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Back",
                  command=self.create_login_screen, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)

    def admin_user_management(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="User Management", font=(
            "Arial", 20), bg="#053048", fg="#FCFBFA").pack()

        tk.Button(frame, text="Deposit",
                  command=self.db.deposit_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Withdraw",
                  command=self.db.widraw_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Check Balance",
                  command=self.db.check_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="View Transactions",
                  command=self.db.view_transaction_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Add user",
                  command=self.db.add_user_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Remove user",
                  command=self.db.remove_user_by_admin, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Back",
                  command=self.adminDasbord, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)

    def Transaction_Monitoring(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg="#053048")
        frame.pack()
        tk.Label(frame, text="Transaction Monitoring", font=(
            "Arial", 20), bg="#053048", fg="#FCFBFA").pack()

        tk.Button(frame, text="Transction history ",
                  command=self.transaction_history_log, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="User details",
                  command=self.User_details, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)
        tk.Button(frame, text="Back",
                  command=self.adminDasbord, bg="#053048", fg="#FCFBFA", width=15).pack(pady=10)

    def transaction_history_log(self):
        try:
            # Connect to the database
            import sqlite3
            from tkinter import ttk
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            # Fetch all rows from the url_resolution table
            cursor.execute("SELECT * FROM transactions")
            rows = cursor.fetchall()
            conn.close()

            # Create a new top-level window for history
            historyFrame = tk.Toplevel(self.window)
            historyFrame.title("Transaction History")
            historyFrame.geometry("800x400")

            # Frame for Treeview with Scrollbars
            tree_frame = tk.Frame(historyFrame)
            # tree_frame.grid(row=1, column=0, sticky="nsew")
            tree_frame.pack(fill=tk.BOTH, expand=True)

            # Configure Scrollbars
            vsb = tk.Scrollbar(tree_frame, orient="vertical")
            hsb = tk.Scrollbar(tree_frame, orient="horizontal")

            # Define Treeview columns and settings
            tree = ttk.Treeview(
                tree_frame,
                columns=("transaction_id", "account_number",
                         "amount", "transaction_type", "timestamp"),
                show="headings",
                yscrollcommand=vsb.set,
                xscrollcommand=hsb.set,
            )

            vsb.config(command=tree.yview)
            hsb.config(command=tree.xview)
            vsb.pack(side=tk.RIGHT, fill=tk.Y)
            hsb.pack(side=tk.BOTTOM, fill=tk.X)

            # Define column headings and format
            columns = {"transaction_id": "transaction_id", "account_number": "account_number",
                       "amount": "amount", "transaction_type": "transaction_type", "timestamp": "timestamp"}
            for col, header in columns.items():
                tree.heading(col, text=header, anchor="center")
                tree.column(col, anchor="center", width=150)

            # Insert data into the Treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Styling for readability
            style = ttk.Style()
            style.configure("Treeview", rowheight=25)
            style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
            tree.tag_configure("odd", background="#E8E8E8")

            # Alternate row colors
            for index, item in enumerate(tree.get_children()):
                if index % 2 == 0:
                    tree.item(item, tags=("odd",))

            # Pack the Treeview
            tree.pack(fill=tk.BOTH, expand=True)

        except sqlite3.Error as e:
            messagebox.showerror(
                "Database Error", f"Error accessing the database: {e}")

    def User_details(self):
        try:
            # Connect to the database
            import sqlite3
            from tkinter import ttk
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            # Fetch all rows from the url_resolution table
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            conn.close()

            # Create a new top-level window for history
            historyFrame = tk.Toplevel(self.window)
            historyFrame.title("User details")
            historyFrame.geometry("800x400")

            # Frame for Treeview with Scrollbars
            tree_frame = tk.Frame(historyFrame)
            # tree_frame.grid(row=1, column=0, sticky="nsew")
            tree_frame.pack(fill=tk.BOTH, expand=True)

            # Configure Scrollbars
            vsb = tk.Scrollbar(tree_frame, orient="vertical")
            hsb = tk.Scrollbar(tree_frame, orient="horizontal")

            # Define Treeview columns and settings
            tree = ttk.Treeview(
                tree_frame,
                columns=("user_id", "account_number",
                         "account_holder", "dob", "father_name", "mother_name", "address", "bank_name", "branch_name", "mobile_number", "account_type", "balance", "role", "password"),
                show="headings",
                yscrollcommand=vsb.set,
                xscrollcommand=hsb.set,
            )

            vsb.config(command=tree.yview)
            hsb.config(command=tree.xview)
            vsb.pack(side=tk.RIGHT, fill=tk.Y)
            hsb.pack(side=tk.BOTTOM, fill=tk.X)

            # Define column headings and format
            columns = {"user_id": "user_id", "account_number": "account_number",
                       "account_holder": "account_holder", "dob": "dob", "father_name": "father_name", "mother_name": "mother_name", "address": "address", "bank_name": "bank_name", "branch_name": "branch_name", "mobile_number": "mobile_number", "account_type": "account_type", "balance": "balance", "role": "role", "password": "password"}
            for col, header in columns.items():
                tree.heading(col, text=header, anchor="center")
                tree.column(col, anchor="center", width=150)

            # Insert data into the Treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Styling for readability
            style = ttk.Style()
            style.configure("Treeview", rowheight=25)
            style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
            tree.tag_configure("odd", background="#E8E8E8")

            # Alternate row colors
            for index, item in enumerate(tree.get_children()):
                if index % 2 == 0:
                    tree.item(item, tags=("odd",))

            # Pack the Treeview
            tree.pack(fill=tk.BOTH, expand=True)

        except sqlite3.Error as e:
            messagebox.showerror(
                "Database Error", f"Error accessing the database: {e}")

# import sqlite3

    def run(self):
        self.window.mainloop()
