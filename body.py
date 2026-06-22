from fastapi import FastAPI
from pydantic import BaseModel
from organs import entry_processesing
from organs import show_active_waitlist



app = FastAPI()

class Waitlist_Entry(BaseModel):
    wait_list_number : int
    seated : bool # will be used in the version 2 
    no_show : bool 
    finished : bool
    wait_list_time_in : int


class customer_data(BaseModel):
    customer_name: str
    phone_number : int
    party_size : int 
    customer_visits : int 


class restaurant_data(BaseModel):  # will be used for the version 2
    restaurant_name : str 
    restaurant_location : str 
    restaurant_capacity : int
    customer_data : customer_data

@app.post("/waitlist")
def add_to_waitlist(waitlist: customer_data): 
    entry_processesing(waitlist.customer_name, waitlist.phone_number, waitlist.party_size, 
    waitlist.customer_visits)
    return {"message": "Customer added to waitlist successfully"}
    
@app.get("/waitlist")
def get_waitlist():
    return show_active_waitlist()

 
