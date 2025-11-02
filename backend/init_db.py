import sqlite3

# Connect to a database file (it creates the file if it doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.executescript("""CREATE TABLE IF NOT EXISTS Users (
    USER_ID INT PRIMARY KEY,
    NAME VARCHAR(255),
    USER_PASSWORD VARCHAR(255),
    EMAIL VARCHAR(255),
    DOB DATE
);
    CREATE TABLE IF NOT EXISTS UserContacts (
    CONTACT_ID INT PRIMARY KEY,
    USER_ID INT,
    ADDRESS VARCHAR(255),
    PHONE_NUMBER VARCHAR(20),
    FOREIGN KEY (USER_ID) REFERENCES Users(USER_ID)
);

  CREATE TABLE IF NOT EXISTS UserAccounts (
    ACCOUNT_ID INT PRIMARY KEY,
    USER_ID INT,
    ACCOUNT_NUMBER VARCHAR(50),
    ACCOUNT_TYPE VARCHAR(50),
    BALANCE DECIMAL(12,2),
    FOREIGN KEY (USER_ID) REFERENCES Users(USER_ID)
);


CREATE TABLE IF NOT EXISTS UserStatus (
    USER_ID INT PRIMARY KEY,
    STATUS VARCHAR(50),
    FOREIGN KEY (USER_ID) REFERENCES Users(USER_ID)
);  
""")

conn.commit()
conn.close()