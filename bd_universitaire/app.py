
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def chart():
    return render_template('../Site web/Connexion - Université Laval.html')

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5001)



