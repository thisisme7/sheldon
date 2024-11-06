from flask import Flask, request, render_template
import sheldon

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        result = sheldon.main(request.form.get('selection'))
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="localhost", port=8002, debug=True)
