import random
import datetime


def generate_passport_number():
    """Generate a sample passport number."""
    letters = ''.join(random.choices(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2
    ))
    digits = ''.join(random.choices('0123456789', k=7))
    return letters + digits


def get_user_input():
    """Collect user information."""

    name = input("Enter full name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    nationality = input("Enter nationality: ")
    address = input("Enter address: ")

    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

    return {
        "Name": name,
        "Date of Birth": dob,
        "Nationality": nationality,
        "Address": address,
        "Passport Number": generate_passport_number()
    }


def display_passport(info):
    """Display passport information."""

    print("\n--- Passport Information ---")

    for key, value in info.items():
        print(f"{key}: {value}")

    print("-----------------------------")


def save_passport(info):
    """Save information to a text file."""

    filename = f"passport_{info['Passport Number']}.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")

    print(f"Sample passport record saved as {filename}")


def main():
    info = get_user_input()

    if info:
        display_passport(info)

        save_option = input(
            "Save passport record to file? (yes/no): "
        ).strip().lower()

        if save_option == 'yes':
            save_passport(info)
        else:
            print("Record was not saved.")


if _name_ == "_main_":
    main()