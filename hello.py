from flask import Flask, render_template, request

app = Flask(__name__)

# Some sample data 
coffee_options = [
    {
        'name': 'Cappuccino',
        'type': 'Espresso',
        'description': 'A traditional Italian coffee drink.',
        'rating': 4.5
    },
    {
        'name': 'Latte',
        'type': 'Espresso',
        'description': 'A coffee drink made with espresso and steamed milk.',
        'rating': 4.2
    },
    {
        'name': 'Mocha',
        'type': 'Espresso',
        'description': 'A chocolate-flavored coffee drink.',
        'rating': 4.0
    }
]

@app.route('/')
def index():
    return render_template('index.html', coffee_options=coffee_options)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    filtered_options = [option for option in coffee_options if keyword.lower() in option['name'].lower()]
    return render_template('index.html', coffee_options=filtered_options)

if __name__ == '__main__':
    app.run(debug=True)


