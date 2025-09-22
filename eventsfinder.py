"""I'll import the needed libraries:
json - this is where the events added by artists and event organizers will add
datetime - so that it handles the date properly as it will be part of the details about the event
# I will start by getting the event deatils and then putting them in a dictionary then save them in a json file
"""
#Added Flask with CORS to make it a web API.
##Added supabase as the database
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Allow requests from lovable frontend

# let's get the details from the artists and the event organizers
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in the .env file")

supabase:Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Event:
    def __init__(self, title, host,tribe, event_venue, start_date, end_date, ticket_link):
        # host can be anyone,,event organizer or an artist
        self.title = title
        self.host = host
        self.tribe = tribe
        self.event_venue = event_venue 
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date().isoformat()
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date().isoformat()
        self.ticket_link = ticket_link

## now let us make it a dictionary for JSON saving

    def to_dict(self):
        return {
            "title": self.title,
            "host": self.host,
            "tribe": self.tribe,
            "event_venue": self.event_venue,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "ticket_link": self.ticket_link
        }
    
# Collecting the details from the artist or event organizer
#title = input("Enter title of the event: ")
#host = input("Enter artist name: ")
#tribe = input("Enter tribe: ")
#location = input("Enter location: ")
#date = input("Enter event date (YYYY-MM-DD): ")
#ticket_link = input("Enter ticket link (URL): ")

# Create an Event object
#event = Event(title, host, tribe, location, date, ticket_link)

## let's save the details entered by the host to JSON
## JSON is already imported


# Flask API endpoints ,,,let me comment out this block with json and use supabase database
@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    # validate required details
    required_details = ['title', 'host', 'tribe', 'event_venue', 'start_date', 'end_date']
    if not all(field in data for field in required_details):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        event = Event(
            data['title'], data['host'], data['tribe'],
            data['event_venue'], data['start_date'], data['end_date'], data['ticket_link']
        )
        event_dict = event.to_dict()  # Call the method with parentheses
    except ValueError as e:
        return jsonify({"error": f"Invalid date format: {str(e)}"}), 400
# save to Supabase
    try:
        response = supabase.table('events').insert(event_dict).execute()
        if not response.data:
            return jsonify({"error": "Failed to add event to Supabase"}), 500
        event_id = response.data[0]['id']
    except Exception as e:
        return jsonify({"error": f"Supabase insert failed: {str(e)}"}), 500


    # save to json
    #events_list = []
    #try:
        #with open("events_details.json", "r") as f:
            #content = f.read().strip()
        #if content:
            #events_list = json.loads(content)
    #except FileNotFoundError:
       # events_list = []
    #events_list.append(event.to_dict())
   # with open("events_details.json", "w") as f:
        #json.dump(events_list, f, indent=4)
    return jsonify({"message": "Event added"}), 201

@app.route('/view_events', methods=['GET'])
def get_events():
    #supabase
    try:
        response = supabase.table('events').select('*').execute()
        events_list = response.data or []
    except Exception as e:
        try:
            with open("events_details.json", "r") as f:
                events_list = json.load(f) or []
        except FileNotFoundError:
            events_list = []
        return jsonify({"warning": f"Fetched from JSON backup: {str(e)}", "data": events_list}), 200

    return jsonify(events_list), 200

@app.route('/')
def home():
    return "Flask is running! Try /view_events or POST to /add_event"


# Now let us have the fans viewing the events from the json file
# Let us come up with a function caleed view_events
# we will use enumerate which returns a pair of index and the value,hence will go through the list of events and return each event with their index
# the fstring lines will print each detail of the event
def view_events():
    try:
        with open("events_details.json", "r") as f:
            events_list = json.load(f)
    except FileNotFoundError:
        events_list = []
    
    for i, event in enumerate(events_list, start=1):
        print(f"\nEvent {i}:")
        print(f"Title: {event['title']}")
        print(f"Host: {event['host']}")
        print(f"Tribe: {event['tribe']}")
        print(f"event_venue: {event['event_venue']}")
        print(f"Start_Date: {event['start_date']}")
        print(f"End_date:{event['end_date']}")
        print(f"Ticket Link: {event['ticket_link']}")
    
if __name__ == '__main__':
    def migrate_to_supabase():
        import json
    try:
        with open("events_details.json", "r") as f:
            events = json.load(f) or []
            for event in events:
                # Handle legacy data if it uses 'location' instead of 'event_venue'
                if 'location' in event:
                    event['event_venue'] = event.pop('location')
                # Ensure all required fields are present
                required_fields = ['title', 'host', 'tribe', 'event_venue', 'start_date', 'end_date', 'ticket_link']
                event_data = {k: event[k] for k in required_fields if k in event}
                supabase.table('events').insert(event_data).execute()
            print("Migration to Supabase completed successfully!")
    except FileNotFoundError:
        print("No events_details.json file found, skipping migration.")
    except Exception as e:
        print(f"Migration failed: {str(e)}")

    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default 5000
    app.run(host='0.0.0.0', port=port, debug=True)