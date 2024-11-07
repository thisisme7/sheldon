from flask import Flask, request, render_template
import sheldon
from flask_wtf import CSRFProtect
import os

app = Flask(__name__)
app.secret_key = os.getenv(key='SECRET_KEY')
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        result = sheldon.main(request.form.get('selection'))
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002, debug=True)
