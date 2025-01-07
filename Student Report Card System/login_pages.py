def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

def sign_up(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = self.hash_password(password)

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        connection.close()

        print(f"User {username} signed up")

def sign_in(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = self.hash_password(password)

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = cursor.fetchone()
        connection.close()

        if user:
            print(f"User {username} signed in")
            return True
        else:
            print("Invalid username or password")
            return False