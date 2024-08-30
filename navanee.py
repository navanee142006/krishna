import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    print("Table created successfully.")

# Insert data into the table
def insert_data(name, age):
    cursor.execute('''
        INSERT INTO users (name, age)
        VALUES (?, ?)
    ''', (name, age))
    conn.commit()
    print("Data inserted successfully.")

# Query data from the table
def query_data():
    cursor.execute('''
        SELECT * FROM users
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update data in the table
def update_data(user_id, name, age):
    cursor.execute('''
        UPDATE users
        SET name = ?, age = ?
        WHERE id = ?
    ''', (name, age, user_id))
    conn.commit()
    print("Data updated successfully.")

# Delete data from the table
def delete_data(user_id):
    cursor.execute('''
        DELETE FROM users
        WHERE id = ?
    ''', (user_id,))
    conn.commit()
    print("Data deleted successfully.")

# Main function to demonstrate functionality
def main():
    create_table()
    
    # Insert some data
    insert_data('Alice', 30)
    insert_data('Bob', 25)
    
    # Query and display data
    print("Data before update:")
    query_data()
    
    # Update data
    update_data(1, 'Alice Smith', 31)
    
    # Query and display data again
    print("Data after update:")
    query_data()
    
    # Delete data
    delete_data(2)
    
    # Query and display data again
    print("Data after deletion:")
    query_data()

# Run the main function
if __name__ == '__main__':
    main()

# Close the connection
conn.close()

