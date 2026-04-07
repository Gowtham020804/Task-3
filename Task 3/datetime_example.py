from datetime import datetime

def get_date_from_user(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        print("Valid Date:", date)

    except ValueError:
        print("Error: Incorrect date format. Use YYYY-MM-DD")