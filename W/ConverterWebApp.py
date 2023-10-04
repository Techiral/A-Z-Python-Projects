'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Currency Converter</title>
    <style>
        /* Add your CSS styles here to customize the appearance of the page */
    </style>
</head>
<body>
    <h1>Currency Converter</h1>
    <p>Supported Currencies: USD, EUR, GBP, JPY, INR, AUD, CAD, and more...</p>
    <form id="currencyConverterForm">
        <label for="fromCurrency">From Currency:</label>
        <select id="fromCurrency" required>
            <!-- Add options for available currencies using <option> tags -->
        </select>

        <label for="toCurrency">To Currency:</label>
        <select id="toCurrency" required>
            <!-- Add options for available currencies using <option> tags -->
        </select>

        <label for="amount">Amount:</label>
        <input type="number" id="amount" step="0.01" required>

        <button type="submit">Convert</button>
    </form>

    <div id="result"></div>

    <script>
        // Add your JavaScript code here for handling the form submission and displaying the result
    </script>
</body>
</html>
'''
from flask import Flask, render_template, request, jsonify
from forex_python.converter import CurrencyRates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Converter.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)

        return jsonify({'result': converted_amount})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
