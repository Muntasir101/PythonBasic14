from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"  # Change this to a secure secret key in production

@app.route("/", methods=["GET", "POST"])
def calculate_payable_amount():
    if request.method == "POST":
        try:
            purchase_amount = float(request.form["purchase_amount"])
            age = int(request.form["age"])
            gender = request.form["gender"]
            payment_method = request.form["payment_method"]

            if purchase_amount < 0:
                raise ValueError("Purchase amount cannot be negative.")
            if age < 0:
                raise ValueError("Age cannot be negative.")

            if purchase_amount < 1000 or age >= 50:
                flash("Sorry, you are not eligible for any free item or discount.")
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
                    flash(f"Congratulations! You get a free {free_item}")

                flash(f"Payable Amount: {payable_amount} TK")

        except ValueError as e:
            flash(str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
