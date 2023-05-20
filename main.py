from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smj_airline_reservation"
)

cursor = db.cursor()

# Create table if not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS reservations (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  trip_type ENUM('one_way', 'return') NOT NULL,
                  departure_date DATE NOT NULL,
                  return_date DATE,
                  num_travelers INT NOT NULL,
                  total_amount DECIMAL(10, 2) NOT NULL,
                  first_name VARCHAR(50),
                  last_name VARCHAR(50),
                  dob DATE,
                  payment_info VARCHAR(100)
                 )""")

# Commit changes and close cursor
db.commit()
cursor.close()
db.close()

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for reservation form
@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        # Get form data
        trip_type = request.form['trip_type']
        departure_date = request.form['departure_date']
        return_date = request.form['return_date']
        num_travelers = int(request.form['num_travelers'])

        # Calculate total amount
        total_amount = 100.0 * num_travelers  # Example calculation, you can change as needed

        # Get traveler details
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        payment_info = request.form['payment_info']

        # Insert reservation into database
        db = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="smj_airline_reservation"
        )
        cursor = db.cursor()
        cursor.execute("""INSERT INTO reservations 
                          (trip_type, departure_date, return_date, num_travelers, total_amount,
                           first_name, last_name, dob, payment_info)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                       (trip_type, departure_date, return_date, num_travelers, total_amount,
                        first_name, last_name, dob, payment_info))
        db.commit()
        cursor.close()
        db.close()

        return redirect('/success')  # Redirect to success page after reservation

    return render_template('reservation.html')

# Route for success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
