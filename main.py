from flask import Flask, render_template,  make_response
from flask_cors import CORS

# Flask config
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(__name__)
CORS(app)

# Основная страница
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
