import tkinter as tk
from tkinter import messagebox

def calculate_payable_amount():
    try:
        purchase_amount = float(purchase_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()
        payment_method = payment_var.get()

        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative.")
        if age < 0:
            raise ValueError("Age cannot be negative.")

        if purchase_amount < 1000 or age >= 50:
            messagebox.showinfo("Result", "Sorry, you are not eligible for any free item or discount.")
            payable_amount = purchase_amount
        else:
            if gender == "male":
                free_item = "cake"
            elif gender == "female":
                free_item = "chocolate"

            if payment_method == "cash":
                discount = purchase_amount * 0.1
            elif payment_method == "card":
                discount = purchase_amount * 0.2

            payable_amount = purchase_amount - discount

            if gender in ["male", "female"]:
                messagebox.showinfo("Result", f"Congratulations! You get a free {free_item}")

            messagebox.showinfo("Result", f"Payable Amount: {payable_amount} TK")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Purchase Application")

# Create the labels and entries for input
purchase_label = tk.Label(window, text="Purchase Amount (in TK):")
purchase_label.pack()
purchase_entry = tk.Entry(window)
purchase_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar(window)
gender_var.set("male")
gender_radiobutton1 = tk.Radiobutton(window, text="Male", variable=gender_var, value="male")
gender_radiobutton1.pack()
gender_radiobutton2 = tk.Radiobutton(window, text="Female", variable=gender_var, value="female")
gender_radiobutton2.pack()

payment_label = tk.Label(window, text="Payment Method:")
payment_label.pack()
payment_var = tk.StringVar(window)
payment_var.set("cash")
payment_radiobutton1 = tk.Radiobutton(window, text="Cash", variable=payment_var, value="cash")
payment_radiobutton1.pack()
payment_radiobutton2 = tk.Radiobutton(window, text="Card", variable=payment_var, value="card")
payment_radiobutton2.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_payable_amount)
calculate_button.pack()

# Start the GUI event loop
window.mainloop()
