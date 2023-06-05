from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # Handle weather data retrieval and processing here
    # Access form data from the request using request.form['<input_name>']
    # Example: city = request.form['city']

    # Example: Send the processed weather data back to the frontend
    weather_data = {
        'temperature': '25°C',
        'conditions': 'Sunny',
        'humidity': '65%'
    }
    return weather_data

# Add more Flask routes and functions as needed

if __name__ == '__main__':
    app.run(debug=True)
