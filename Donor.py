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
    return render_template('donor.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            addressline1 = request.form['addressline1']
            addressline2 = request.form['addressline2']
            gender = request.form['gender']
            email = request.form['email']
            contact = request.form['contact']
            username = request.form['username']
            password = request.form['password']

            # Insert form data into the database
            cursor.execute(
                "INSERT INTO donors (first_name, last_name, addressline1, addressline2, gender, email, contact, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (first_name, last_name, addressline1, addressline2, gender, email, contact, username, password)
            )
            db.commit()
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
