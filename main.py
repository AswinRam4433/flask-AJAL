from flask import Flask, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Updated Flask Routes"})



people = [
    {"id": "#1", "name": "User1", "tickets": []},
    {"id": "#2", "name": "User2", "tickets": []},
    {"id": "#3", "name": "User3", "tickets": []},
    {"id": "#4", "name": "User4", "tickets": []},
    {"id": "#5", "name": "User5", "tickets": []},
]

tickets = []


def assign_ticket(ticket):
    for person in people:
        if len(person["tickets"]) < len(people):
            ticket["assigned_to"] = ticket["assigned_to"]
            person["tickets"].append(ticket["ticket_id"])
            print(json.dumps(people,indent=4))
            return

valid_ids=['#1','#2','#3','#4','#5']

@app.route('/ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    try:
        if "user_id" not in data or "issue" not in data:
            return jsonify({"message": "Bad Request-Missing Parameters", "success": False, "data": {}}), 400
        
        if data["user_id"] not in valid_ids:
            return jsonify({"message": "Bad Request-Invalid ID", "success": False, "data": {}}), 400



        ticket = {
            "ticket_id": str(len(tickets) + 1),
            "issue_description": data["issue"],
            "assigned_to": data["user_id"], 
            "raised_by": data["user_id"]
        }

        assign_ticket(ticket)

        tickets.append(ticket)
        print(tickets)

        response_data = {
            "ticket_id": ticket["ticket_id"],
            "assigned_to": ticket["assigned_to"]
        }

        return jsonify({"message": "Ticket created successfully", "success": True, "data": response_data}), 201
    
    except:
        return jsonify({"message": "Internal Server Error-Exception Encountered", "success": False, "data": {}}), 500



    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
