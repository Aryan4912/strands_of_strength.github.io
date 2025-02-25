const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Parse incoming request bodies
app.use(bodyParser.urlencoded({ extended: true }));

// MySQL connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'HairSelling'
});

db.connect(err => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the database');
});

// Route to handle form submission
app.post('/submit-hair', (req, res) => {
    const { name, contact, gender, age, hair_length, hair_thickness, hair_type, hair_color, hair_weight, price_per_gram, comments } = req.body;

    const sqlQuery = `INSERT INTO HairSale (name, contact, gender, age, hair_length, hair_thickness, hair_type, hair_color, hair_weight, price_per_gram, comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;

    db.query(sqlQuery, [name, contact, gender, age, hair_length, hair_thickness, hair_type, hair_color, hair_weight, price_per_gram, comments], (err, result) => {
        if (err) {
            console.error('Error inserting data:', err);
            res.send('Error occurred while submitting the form');
            return;
        }
        res.send('Form submitted successfully!');
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
