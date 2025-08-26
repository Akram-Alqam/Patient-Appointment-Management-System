from datetime import datetime
import re

appointments = []

def validation_date(date):
    """Validate date format (YYYY-MM-DD). Returns True if valid, False otherwise."""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validation_time(time):
    """Validate time format (HH:MM, 24-hour). Returns True if valid, False otherwise."""
    pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
    return bool(re.match(pattern, time))

def add():
    """Add a new appointment with validated user input."""
    while True:
        patient_name = input("Enter patient name (letters and spaces only): ").strip()
        if patient_name and all(c.isalpha() or c.isspace() for c in patient_name):
            break
        print("Invalid name. Please use letters and spaces only.")

    while True:
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
        if validation_date(appointment_date):
            break
        print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-09-01).")

    while True:
        appointment_time = input("Enter appointment time (HH:MM, 24-hour): ").strip()
        if validation_time(appointment_time):
            break
        print("Invalid time format. Please use HH:MM (e.g., 14:30).")

    appointment = { "name" : patient_name, "date" : appointment_date, "time" : appointment_time}

    print(f"\nConfirm appointment: {patient_name} on {appointment_date} at {appointment_time}")
    confirm = input("add this appointment? (y/n): ").lower().strip()
    if confirm == 'y':
        appointments.append(appointment)
        print("Appointment added successfully!")
    else:
        print("Appointment not added.")

def show():
    """Display all appointments in a formatted table."""
    if not appointments:
        print("No appointments available.")
        return

    print("\n=== All Appointments ===")
    print(f"{'No.':<4} | {'Patient Name':<20} | {'Date':<12} | {'Time':<8}")
    print("-" * 50)
    for index, appt in enumerate(appointments, 1):
        print(f"{index:<4} | {appt['name']:<20} | {appt['date']:<12} | {appt['time']:<8}")

def deletet():
    """Delete an appointment by number with confirmation."""
    if not appointments:
        print("No appointments to delete.")
        return
    show()
    try:
        choice = input("Enter appointment number to delete (or 0 to cancel): ").strip()
        choice = int(choice)
        if choice == 0:
            print("Deletion cancelled.")
            return
        if 1 <= choice <= len(appointments):
            appt = appointments[choice - 1]
            print(f"\nConfirm deletion: {appt['name']} on {appt['date']} at {appt['time']}")
            confirm = input("Delete this appointment? (y/n): ").lower().strip()
            if confirm == 'y':
                removed = appointments.pop(choice - 1)
                print(f"Appointment for {removed['name']} deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid appointment number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Display main menu and handle user choices."""
    while True:
        print("\n=== Hospital Appointment Management System ===")
        print("1. Add New Appointment")
        print("2. View All Appointments")
        print("3. Delete Appointment")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            add()
        elif choice == "2":
            show()
        elif choice == "3":
            deletet()
        elif choice == "4":
            print("Thank you for using the Appointment Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    print("Welcome to the Hospital Appointment Management System")
    main_menu()