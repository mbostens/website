from flask_cors import CORS
from flask import render_template, Flask

# Flask app setup
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template("index.html")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)