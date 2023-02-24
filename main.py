import sqlite3
import hashlib

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    conn.close()

def check_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))

    user = c.fetchone()

    conn.close()

    return user is not None


def main():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT UNIQUE, 
                 password TEXT)''')

    conn.close()

    while True:
        print("Enter 1 to sign up or 2 to log in: ")
        choice = input()

        if choice == '1':
            print("Enter your username: ")
            username = input()

            print("Enter your password: ")
            password = input()

            create_user(username, password)
            print("User created successfully.")

        elif choice == '2':
            print("Enter your username: ")
            username = input()

            print("Enter your password: ")
            password = input()

            if check_login(username, password):
                print("Login successful.")
            else:
                print("Incorrect username or password.")

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
