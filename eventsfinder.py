"""I'll import the needed libraries:
json - this is where the events added by artists and event organizers will add
datetime - so that it handles the date properly as it will be part of the details about the event
# I will start by getting the event deatils and then putting them in a dictionary then save them in a json file
"""
#Added Flask with CORS to make it a web API.
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import json

app = Flask(__name__)
CORS(app)  # Allow requests from lovable frontend

# let's get the details from the artists and the event organizers
# 

class Event:
    def __init__(self, title, host,tribe, location, date, ticket_link):
        # host can be anyone,,event organizer or an artist
        self.title = title
        self.host = host
        self.tribe = tribe
        self.location = location
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date().isoformat()
        self.ticket_link = ticket_link

## now let us make it a dictionary for JSON saving

    def to_dict(self):
        return {
            "title": self.title,
            "host": self.host,
            "tribe": self.tribe,
            "location": self.location,
            "date": self.date,
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

#with open("events_details.json", "w") as f:##now f is the created file
    #json.dump([event.event_details_dictionary()], f,)##getting the details from the objects and saving them in dictionary form
#I had used the above but I realized that it only allows one event to the file,,,as any update will ovewrite the other events
# so let's allow for more events to be updated
# start with an empty list
#events_list = []

# now we open the file in r and w mode
#let's load existing events
#try:
    #with open("events_details.json", 'r') as f:
        #content = f.read()
        #if content.strip():  # check not empty
            #events_list = json.loads(content)
#except FileNotFoundError:
    # if the file doesn't exist yet, just skip
    #events_list = []

# we add new event
#events_list.append(event.event_details_dictionary())

#print(events_list)

# now let's save updated events
#with open("events_details.json", "w") as f:# f is the file
   # json.dump(events_list, f, indent=4)

# Flask API endpoints
@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    event = Event(
        data['title'], data['host'], data['tribe'],
        data['location'], data['date'], data['ticket_link']
    )
    events_list = []
    try:
        with open("events_details.json", "r") as f:
            content = f.read().strip()
            if content:
                events_list = json.loads(content)
    except FileNotFoundError:
        events_list = []

    
    events_list.append(event.to_dict())
    with open("events_details.json", "w") as f:
        json.dump(events_list, f, indent=4)
    return jsonify({"message": "Event added"}), 201

@app.route('/view_events', methods=['GET'])
def get_events():
    with open("events_details.json", "r") as f:
        events_list = json.load(f)
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
        print(events_list)
        return
    print(events_list)
    for i, event in enumerate(events_list, start=1):
        print(f"\nEvent {i}:")
        print(f"Title: {event['title']}")
        print(f"Host: {event['host']}")
        print(f"Tribe: {event['tribe']}")
        print(f"Location: {event['location']}")
        print(f"Date: {event['date']}")
        print(f"Ticket Link: {event['ticket_link']}")
    
if __name__ == '__main__':
    app.run(debug=True)