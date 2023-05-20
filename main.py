import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sunshine",
    database="smj_airline_reservation"
)
cursor = conn.cursor()

# Function to create a new reservation
def create_reservation():
    trip_type = trip_var.get()
    departure_date = departure_var.get()
    return_date = return_var.get()
    num_travelers = num_travelers_var.get()
    total_amount = 200.00 if trip_type == "one_way" else 300.00
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = dob_entry.get()
    payment_card_number = card_entry.get()
    reservation_status = "success"
    try:
        sql = "INSERT INTO reservations (trip_type, departure_date, return_date, num_travelers, total_amount, first_name, last_name, date_of_birth, payment_card_number, reservation_status) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (trip_type, departure_date, return_date, num_travelers, total_amount, first_name, last_name, date_of_birth, payment_card_number, reservation_status)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Reservation created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to read reservations
def read_reservations():
    cursor.execute("SELECT * FROM reservations")
    result = cursor.fetchall()
    return result

# Function to delete a reservation
def delete_reservation():
    reservation_id = delete_id_var.get()
    try:
        sql = "DELETE FROM reservations WHERE id = %s"
        values = (reservation_id,)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Reservation deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to update a reservation
def update_reservation():
    reservation_id = update_id_var.get()
    trip_type = trip_var.get()
    departure_date = departure_var.get()
    return_date = return_var.get()
    num_travelers = num_travelers_var.get()
    total_amount = 200.00 if trip_type == "one_way" else 300.00
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = dob_entry.get()
    payment_card_number = card_entry.get()
    reservation_status = "success"
    try:
        sql = "UPDATE reservations SET trip_type = %s, departure_date = %s, return_date = %s, num_travelers = %s, total_amount = %s, first_name = %s, last_name = %s, date_of_birth = %s, payment_card_number = %s, reservation_status = %s WHERE id = %s"
        values = (trip_type, departure_date, return_date, num_travelers, total_amount, first_name, last_name, date_of_birth, payment_card_number, reservation_status, reservation_id)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Reservation updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display reservations in a table
def display_reservations():
    result = read_reservations()
    if result:
        display_text.delete("1.0", END)
        display_text.insert(END, "ID\tTrip Type\tDeparture Date\tReturn Date\tNum Travelers\tTotal Amount\tFirst Name\tLast Name\tDate of Birth\tPayment Card Number\tReservation Status\n")
        for row in result:
            display_text.insert(END, f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\t{row[10]}\n")
    else:
        display_text.delete("1.0", END)
        display_text.insert(END, "No reservations found.")

# Create GUI window
root = Tk()
root.title("Airline Reservation System")

# Create labels
trip_label = Label(root, text="Trip Type:")
departure_label = Label(root, text="Departure Date:")
return_label = Label(root, text="Return Date:")
num_travelers_label = Label(root, text="Number of Travelers:")
first_name_label = Label(root, text="First Name:")
last_name_label = Label(root, text="Last Name:")
dob_label = Label(root, text="Date of Birth:")
card_label = Label(root, text="Payment Card Number:")
delete_id_label = Label(root, text="Reservation ID for Deletion:")
update_id_label = Label(root, text="Reservation ID for Update:")

# Create entry fields
trip_var = StringVar()
trip_combobox = Combobox(root, textvariable=trip_var, values=["one_way", "round_trip"])
departure_var = StringVar()
departure_entry = Entry(root, textvariable=departure_var)
return_var = StringVar()
return_entry = Entry(root, textvariable=return_var)
num_travelers_var = IntVar()
num_travelers_entry = Entry(root, textvariable=num_travelers_var)
first_name_entry = Entry(root)
last_name_entry = Entry(root)
dob_entry = Entry(root)
card_entry = Entry(root)
delete_id_var = IntVar()
delete_id_entry = Entry(root, textvariable=delete_id_var)
update_id_var = IntVar()
update_id_entry = Entry(root, textvariable=update_id_var)

# Create buttons
create_button = Button(root, text="Create Reservation", command=create_reservation)
read_button = Button(root, text="Display Reservations", command=display_reservations)
delete_button = Button(root, text="Delete Reservation", command=delete_reservation)
update_button = Button(root, text="Update Reservation", command=update_reservation)

# Create text box to display reservations
display_text = Text(root, height=10, width=100)

# Grid layout for GUI elements
trip_label.grid(row=0, column=0, sticky=W)
trip_combobox.grid(row=0, column=1)
departure_label.grid(row=1, column=0, sticky=W)
departure_entry.grid(row=1, column=1)
return_label.grid(row=2, column=0, sticky=W)
return_entry.grid(row=2, column=1)
num_travelers_label.grid(row=3, column=0, sticky=W)
num_travelers_entry.grid(row=3, column=1)
first_name_label.grid(row=4, column=0, sticky=W)
first_name_entry.grid(row=4, column=1)
last_name_label.grid(row=5, column=0, sticky=W)
last_name_entry.grid(row=5, column=1)
dob_label.grid(row=6, column=0, sticky=W)
dob_entry.grid(row=6, column=1)
card_label.grid(row=7, column=0, sticky=W)
card_entry.grid(row=7, column=1)
create_button.grid(row=8, column=0, columnspan=2)
delete_id_label.grid(row=9, column=0, sticky=W)
delete_id_entry.grid(row=9, column=1)
delete_button.grid(row=10, column=0, columnspan=2)
update_id_label.grid(row=11, column=0, sticky=W)
update_id_entry.grid(row=11, column=1)
update_button.grid(row=12, column=0, columnspan=2)
read_button.grid(row=13, column=0, columnspan=2)
display_text.grid(row=14, column=0, columnspan=2)


root.mainloop()

