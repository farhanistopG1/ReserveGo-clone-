import logging 
from database import waitlist_entry
from database import active_waitlist


logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def entry_processesing(customer_name, phone_number, party_size, customer_visits):
    try:
        logging.info(f"Adding customer to waitlist: {customer_name}, Phone: {phone_number}")
        waitlist_entry(customer_name, phone_number, party_size, customer_visits)

    except Exception as e:
        logging.error(f"Error adding customer to waitlist: {e}")
        return {"error": "Failed to add customer to waitlist."}

    
    
def show_active_waitlist():
    return  active_waitlist()