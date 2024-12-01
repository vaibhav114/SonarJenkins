import os

# 1. Hardcoded credentials and printing sensitive data
def connect_to_db():
    username = "root"  # Hardcoded credentials
    password = "12345"  # Hardcoded password
    print(f"Connecting to database with username: {username} and password: {password}")  # Exposing credentials
    # Simulating a bad connection (e.g., missing actual connection logic)

# 2. SQL Injection vulnerability and concatenation of user input
def unsafe_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "';"  # Vulnerable to SQL Injection
    print("Executing query: " + query)  # Directly logging the potentially dangerous query
    # Executing without sanitizing or using prepared statements

# 3. Path traversal vulnerability without validation
def read_file(file_name):
    if "../" in file_name:  # Extremely naive attempt at sanitization
        print("Trying to block path traversal, but failing.")
    with open(file_name, 'r') as file:  # Potential path traversal issue
        data = file.read()
        print("File content: " + data)  # Printing file content unsafely

# 4. Use of insecure hashing algorithm and poor error handling
def hash_password(password):
    import hashlib
    try:
        hashed = hashlib.md5(password.encode()).hexdigest()  # Using MD5 (insecure)
        print("MD5 hash of password: " + hashed)
    except:
        print("Something went wrong while hashing, but I'm not telling you what!")

# 5. Environment variables logging (security issue)
def log_environment():
    print("Listing all environment variables for fun and insecurity:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

# 6. Unused imports and inefficient code
import random
for i in range(1000000):  # Inefficient loop doing nothing
    pass

if __name__ == "__main__":
    connect_to_db()
    unsafe_query("'; DROP TABLE users; --")
    read_file("/etc/passwd")
    hash_password("very_secure_password")
    log_environment()