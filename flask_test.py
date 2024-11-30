from flask import Flask

app = Flask(__name__)


# Conversion function
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


# Root route
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


# Greet route
@app.route('/greet')
def greet():
    return '<h1>Hello!</h1>'


# Celsius to Fahrenheit route
@app.route('/f/<celsius>')
def convert_temperature(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f'<h1>{celsius_float}°C is {fahrenheit:.2f}°F</h1>'
    except ValueError:
        return '<h1>Invalid input. Please enter a numeric value.</h1>'


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
