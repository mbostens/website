from flask_cors import CORS
from flask import render_template, Flask
import os
# Flask app setup
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    print("Current Working Directory:", os.getcwd())
    print("Template search path:", app.jinja_loader.searchpath)
    return render_template("index.html")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)