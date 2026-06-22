import psycopg
import logging

logging.basicConfig(
    filename="dblog.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

connection = psycopg.connect(
    dbname="reservego",
    user="farhanahmedmudgal"
)

cursor = connection.cursor()

def waitlist_entry(customer_name, phone_number, party_size, customer_visits):

    cursor.execute("""
INSERT INTO waitlist_entries
(name, phone_number, party_size, seated, no_show, finished)
VALUES (%s, %s, %s, %s, %s, %s)
""",(
    customer_name,
    phone_number,
    party_size,
    False,
    False,
    False
))
    connection.commit()
    


def active_waitlist():
    cursor.execute(
        """SELECT * FROM waitlist_entries WHERE seated = false AND no_show = false AND finished = false"""
    )
    return cursor.fetchall()




