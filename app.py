from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/" , methods = ["POST"])
def hello():
    if request.method == "POST":
        original_price = request.form['original_price']
        discount = request.form['discount']
        dis_price = int(original_price) - (int(original_price) * (int(discount) / 100))
        
        mk = dis_price
        

    return render_template("index.html", my_sal = mk,org = original_price, dis =discount )
    


@app.route("/") 
def submit():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

