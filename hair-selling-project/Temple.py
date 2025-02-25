from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# Database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="NAna*#12",
    db="Donors"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('temple.html')  # Ensure "donor.html" is inside the "templates" folder

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            state = request.form['state']
            city = request.form['city']
            address1 = request.form['addressline1']
            address2 = request.form['addressline2']
            email = request.form['email']
            contact = request.form['contact']
            username = request.form['username']
            password = request.form['password']

            # Hash the password before storing
            hashed_password = generate_password_hash(password)

            # Insert form data into the database
            cursor.execute(
                "INSERT INTO temples (name, state, city, addressline1, addressline2, email, contact, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (name, state, city, address1, address2, email, contact, username, hashed_password)
            )
            db.commit()
            flash("Registration successful!", "success")
        except MySQLdb.Error as err:
            flash(f"Database error: {err}", "danger")
            db.rollback()
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
