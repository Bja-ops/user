def register_user():
    smalls = 'abcdefghijklmnopqrstuvwxyz'
    bigs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '0123456789'

    while True:
        login = input("Enter login: ")
        password = input("Enter password: ")

        count_smalls = sum(1 for c in login if c in smalls)
        count_bigs = sum(1 for c in login if c in bigs)
        count_numbers = sum(1 for c in login if c in nums)

        count_smalls1 = sum(1 for c in password if c in smalls)
        count_bigs1 = sum(1 for c in password if c in bigs)
        count_numbers1 = sum(1 for c in password if c in nums)

        login_ok = True
        if count_bigs < 1:
            print("Login must have at least one uppercase letter.")
            login_ok = False
        if count_smalls < 1:
            print("Login must have at least two lowercase letters.")
            login_ok = False
        if count_numbers < 2:
            print("Login must have at least three digits.")
            login_ok = False
        if login_ok:
            print("Login is good.")
        else:
            print("Login doesn't meet requirements.")

        password_ok = True
        if count_bigs1 < 1:
            print("Password must have at least one uppercase letter.")
            password_ok = False
        if count_smalls1 < 1:
            print("Password must have at least 2 lowercase letters.")
            password_ok = False
        if count_numbers1 < 2:
            print("Password must have at least three digits.")
            password_ok = False
        if password_ok:
            print("Password is good.")
        else:
            print("Password doesn't meet requirements.")

        if login_ok and password_ok:
            print("All requirements met. Registration complete. Data saved to file user.txt")
            with open("user.txt", "a") as file:
                file.write(f"Login: {login}\n ")
                file.write(f"Password: {password}\n")
            break

def login():
    while True:
        login_input = input("Enter login: ")
        password_input = input("Enter password: ")

        try:
            with open("user.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("No registered users found. Please register first.")
            return

        # Look for matching login/password pair
        for i in range(0, len(lines), 2):
            stored_login = lines[i].strip().replace("Login: ", "")
            stored_password = lines[i+1].strip().replace("Password: ", "")

            if stored_login == login_input and stored_password == password_input:
                print("Login success")
                return  # Exit function after successful login

        print("Bad login or password. Try again.\n")


# register_user()
login()
