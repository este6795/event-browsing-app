import sqlite3

# Connect to the SQLite database
# If the file does not exist, it will be created automatically
sqliteConnection = sqlite3.connect("EventPlannerDB.db")

# Create cursor object to interact with the database
cursor = sqliteConnection.cursor()

# ----------------------------- READ EVENTS ----------------------------- #
# Function to read all events from the events table
def read_events():
    """
    Reads all event records from the events table.
    Returns a list of tuples, each representing an event record.
    """

    # SQL query to select all records from the events table
    sql_command = "SELECT * FROM events"

    # Execute the query
    cursor.execute(sql_command)

    # Fetch all results from the executed query
    events = cursor.fetchall()

    return events


print(read_events())