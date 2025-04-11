from datetime import datetime

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Please use the format YYYY-MM-DD.")
        return

    today = datetime.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    print(f"🎉 You are {age_years} years old.")

if __name__ == "__main__":
    print("📅 Age Calculator")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    calculate_age(dob)
