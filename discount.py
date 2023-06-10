from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_discount', methods=['POST'])
def calculate_discount():
    purchase_amount = float(request.form['purchase_amount'])
    discount = 0

    if purchase_amount <= 10000:
        discount = 0.1
    elif purchase_amount <= 20000:
        discount = 0.15
    elif purchase_amount <= 50000:
        discount = 0.2
    else:
        discount = 0.3

    discount_amount = purchase_amount * discount
    final_amount = purchase_amount - discount_amount

    return render_template('result.html', purchase_amount=purchase_amount, discount=discount,
                           discount_amount=discount_amount, final_amount=final_amount)


if __name__ == '__main__':
    app.run(debug=True)
