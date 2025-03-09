from tkinter import *
from tkinter import messagebox

def ATM_SIMULATION():
    users = {
        "user1": {"pin": "1234", "balance": 10000},
        "user2": {"pin": "5678", "balance": 30000},
    }
    MAX_USERS = 5

    window = Tk()
    window.geometry("400x400")
    window.title("ATM Simulation")
    window.config(background="white")

    Label(window, text="Welcome to XYZ ATM Services", background="white", font=('Calibri', 12, 'bold')).pack(pady=10)
    icon = PhotoImage(file="gh.png")
    window.iconphoto(True, icon)

    username_label = Label(window, text="Username:", background="white", font=("Calibri", 10, 'bold'))
    username_label.pack()
    username_entry = Entry(window, width=20)
    username_entry.pack()

    pin_label = Label(window, text="PIN (4 digits):", background="white", font=("Calibri", 10, 'bold'))
    pin_label.pack()
    pin_entry = Entry(window, width=20, show="#")
    pin_entry.pack()

    def create_account():
        username = username_entry.get()
        pin = pin_entry.get()

        if len(users) >= MAX_USERS:
            messagebox.showerror("Error", "User limit reached!!!!!")
            return
        
        if not username or not pin:
            messagebox.showerror("Error", "Please fill in all the boxes")
            return
        
        if username in users:
            messagebox.showerror("Error", "Username already taken....")
            return

        if len(pin) != 4 or not pin.isdigit():
            messagebox.showerror("Error", "PIN must be 4 digits.")
            return

        users[username] = {"pin": pin, "balance": 0}
        messagebox.showinfo("Success", f"Account created for {username}!")
        username_entry.delete(0, END)
        pin_entry.delete(0, END)

    def login():
        username = username_entry.get()
        pin = pin_entry.get()

        if not username or not pin:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if username in users and users[username]["pin"] == pin:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            username_entry.delete(0, END)
            pin_entry.delete(0, END)
            open_main_menu(username)
        else:
            messagebox.showerror("Error", "Invalid username or PIN.")

    def open_main_menu(username):
        main_menu = Toplevel(window)
        main_menu.geometry("400x300")
        main_menu.title("Main Menu")
        main_menu.config(background="white")

        Label(main_menu, text=f"Welcome, {username}!", background="white", font=("Calibri", 12, 'bold')).pack(pady=10)

        def view_balance():
            balance = users[username]["balance"]
            messagebox.showinfo("Balance", f"Your balance is: {balance} PKR")

        def withdraw_cash():
            def one_thousand():
                if 1000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 1000
                    messagebox.showinfo("Success", f"Successfully withdrawn 1000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()

            def five_thousand():
                if 5000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 5000
                    messagebox.showinfo("Success", f"Successfully withdrawn 5000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()
            
            def ten_thousand():
                if 10000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 10000
                    messagebox.showinfo("Success", f"Successfully withdrawn 10000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()
            
            def three_thousand():
                if 3000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 3000
                    messagebox.showinfo("Success", f"Successfully withdrawn 15000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()
            
            def twenty_five_thousand():
                if 25000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 25000
                    messagebox.showinfo("Success", f"Successfully withdrawn 20000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()
            
            def fifty_thousand():
                if 50000 > users[username]["balance"]:
                    messagebox.showerror("Error", "Insufficient funds.")
                else:
                    users[username]["balance"] -= 50000
                    messagebox.showinfo("Success", f"Successfully withdrawn 20000 PKR. New balance: {users[username]['balance']} PKR.")
                    withdraw_window.destroy()
                
            
            def other_amount():
                other_window = Toplevel(withdraw_window)
                other_window.geometry("300x200")
                other_window.title("Withdraw Cash")
                other_window.config(background="white")

                Label(other_window, text="Enter Amount:", font=("Calibri"), background="white").pack(pady=10)
                withdraw_entry = Entry(other_window, width=20)
                withdraw_entry.pack()

                def perform_withdrawal():
                    amount = withdraw_entry.get()
                    if not amount.isdigit():
                        messagebox.showerror("Error", "Please enter a valid amount.")
                        return

                    amount = int(amount)
                    if amount > users[username]["balance"]:
                        messagebox.showerror("Error", "Insufficient funds.")
                    else:
                        users[username]["balance"] -= amount
                        messagebox.showinfo("Success", f"Successfully withdrawn {amount} PKR. New balance: {users[username]['balance']} PKR.")
                        other_window.destroy()

                Button(other_window, text="Withdraw", command=perform_withdrawal, background="green").pack(pady=10)

            withdraw_window = Toplevel(main_menu)
            withdraw_window.geometry("400x400")
            withdraw_window.title("Withdraw Cash")
            withdraw_window.config(background="gray")
    
            
            Button(withdraw_window, text="1000", command=one_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="3000", command=three_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="5000", command=five_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="10000", command=ten_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="25000", command=twenty_five_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="50000", command=fifty_thousand, background="white").pack(pady=10)
            Button(withdraw_window, text="Other", command=other_amount, background="white").pack(pady=10)

            

        def deposit_cash():
            def perform_deposit():
                amount = deposit_entry.get()
                if not amount.isdigit():
                    messagebox.showerror("Error", "Please enter a valid amount.")
                    return

                amount = int(amount)
                users[username]["balance"] += amount
                messagebox.showinfo("Success", f"Successfully deposited {amount} PKR. New balance: {users[username]['balance']} PKR.")
                deposit_window.destroy()

            deposit_window = Toplevel(main_menu)
            deposit_window.geometry("300x200")
            deposit_window.title("Deposit Cash")
            deposit_window.config(background="white")
            Label(deposit_window, text="Enter Amount:", background="white").pack(pady=10)
            deposit_entry = Entry(deposit_window, width=20)
            deposit_entry.pack()
            Button(deposit_window, text="Deposit", command=perform_deposit, background="green").pack(pady=10)


        Button(main_menu, text="View Balance", command=view_balance, background="gray").pack(pady=5)
        Button(main_menu, text="Withdraw Cash", command=withdraw_cash, background="gray").pack(pady=5)
        Button(main_menu, text="Deposit Cash", command=deposit_cash, background="gray").pack(pady=5)
        Button(main_menu, text="Exit", command=main_menu.destroy, background="red").pack(pady=5)

    Button(window, text="Create Account", command=create_account, background="blue", foreground="white").pack(pady=10)
    Button(window, text="Login", command=login, background="green", foreground="white").pack(pady=10)
    Button(window, text="Exit", command=window.destroy, background="red", foreground="white" , width= 7 ).pack(pady=5)

    window.mainloop()

ATM_SIMULATION()
