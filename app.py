from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NAna*#12",
    database="HairSelling"
)

@app.route("/")
def index():
    return render_template("hair_buy_or_sell.html")

@app.route("/submit-hair", methods=["POST"])
def submit_hair():
    name = request.form["name"]
    contact = request.form["contact"]
    gender = request.form["gender"]
    age = int(request.form["age"])
    hair_length = float(request.form["hair-length"])
    hair_thickness = float(request.form["hair-thickness"])
    hair_type = request.form["hair-type"]
    hair_color = request.form["hair-color"]
    hair_weight = float(request.form["hair-weight"])
    price_per_gram = float(request.form["price-per-gram"])
    comments = request.form["comments"]

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO HairSale 
        (name, contact, gender, age, hair_length, hair_thickness, hair_type, hair_color, hair_weight, price_per_gram, comments)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, contact, gender, age, hair_length, hair_thickness, hair_type, hair_color, hair_weight, price_per_gram, comments))
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
