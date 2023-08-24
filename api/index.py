from flask import Flask

app = Flask(__name__)

# csv_url = 'https://drive.google.com/uc?id=1JxlvKuK9esOHjkXMnHO1NPI3M8oty2bG'
# movie_complete_data = pd.read_csv(csv_url)

# @app.route('/get_top_5')
# def get_top_5():
#     top_5_data = movie_complete_data.head().to_dict(orient='records')
#     return jsonify(top_5_data)

@app.route('/')
def home():
    return 'Hello from Vamshi'

@app.route('/about')
def about():
    return 'About'
