# Week 1: generate synthetic Northwind support tickets
import random
import csv
from datetime import datetime, timedelta  # NEW: dates and lengths of time

random.seed(42)

first_ticket = {
    "ticket_id": "NW-0001",
    "customer": "Harbour Foods Ltd",
    "order_id": "ORD-48213",
    "complaint": "Pallet shows as in Rotterdam for 9 days. Where is it?",
    "urgency": "high",
    "category": "tracking",
    "created_at": "2026-10-16 09:00",  # NEW
    "first_response_hours": 216,        # NEW: 9 days, the Harbour Foods case
    "status": "answered",               # NEW
}

customers = [
    "Harbour Foods Ltd",
    "Pennine Steel",
    "Brightwell Pharmacy",
    "Coastline Furniture",
    "Northgate Electronics",
    "Ashford Garden Supply",
    "Meridian Textiles",
    "Kestrel Auto Parts",
    "Bluewater Beverages",
    "Oakridge Building Supplies",
    "Halden Medical",
    "Thornbury Paper Co",
    "Silverline Cosmetics",
    "Ridgeway Toys",
    "Fairmont Wine Imports",
    "Granite Office Supplies",
    "Lowland Dairy",
    "Westbrook Sports",
    "Cobalt Machinery",
    "Elmfield Books",
]

complaints = {
    "delays": [
        "Delivery arrived two days late.",
        "Our shipment was due Tuesday and still hasn't arrived.",
        "Third late delivery this month. We're losing patience.",
        "Collection was booked for 9am, driver never showed up.",
        "Order stuck at the Felixstowe depot for a week.",
        "Your estimated delivery date has changed four times.",
        "Need this pallet before Friday or our production line stops.",
        "Delivery window was 8-12, driver came at 6pm.",
    ],
    "tracking": [
        "Tracking page has not updated since Monday.",
        "Tracking says delivered but nothing arrived.",
        "The tracking link in your email doesn't work.",
        "Status has said 'in transit' for 11 days.",
        "Tracking shows our goods in Manchester, but they were going to Bristol.",
        "Can't find my order on your website using the order number.",
    ],
    "damage": [
        "Two boxes in the shipment were damaged.",
        "Pallet was wrapped badly and half the cartons were crushed.",
        "Glass items arrived broken.",
        "Refrigerated goods arrived warm. The whole load is spoiled.",
        "Forklift damage on three pallets.",
        "Packaging was wet when it arrived, stock is ruined.",
        "Seal on the container was broken on arrival.",
    ],
    "wrong_delivery": [
        "Driver left the goods at the wrong dock.",
        "We received someone else's order.",
        "Only 8 of 12 pallets were delivered.",
        "Goods went to our old address even though we updated it.",
        "Driver refused to unload at our site.",
        "Delivery was left outside in the rain with no signature.",
    ],
    "billing": [
        "Invoice amount does not match the quote.",
        "We were charged twice for the same shipment.",
        "Fuel surcharge on our invoice wasn't in the contract.",
        "Still waiting for a credit note promised last month.",
        "Invoice has the wrong VAT number.",
        "Why was there a waiting time charge? Your driver was late, not us.",
        "Need a copy of an invoice from last March.",
    ],
    "refunds_claims": [
        "How do I claim for damaged goods?",
        "Submitted a claim 6 weeks ago and heard nothing.",
        "Want a refund for the late delivery as per our agreement.",
        "Your claim form keeps rejecting our upload.",
        "What is your refund policy for missed collections?",
    ],
    "customs_hazardous": [
        "Shipment held at customs. What paperwork is missing?",
        "Do you need an export declaration for goods to Norway?",
        "Can you transport lithium batteries?",
        "Hazardous goods label missing on our delivery note.",
    ],
    "account_general": [
        "Need to change the delivery address on an existing order.",
        "How do I add a new user to our account?",
        "Can we book a regular weekly collection?",
        "Who is our account manager now?",
        "Can you send proof of delivery for last week's order?",
        "Your phone line kept me on hold for 40 minutes.",
        "Nobody replied to my email from last week.",
        "Want to cancel the order booked for tomorrow.",
        "Can you quote for 20 pallets to Glasgow?",
        "Is your Leeds warehouse open on Saturdays?",
        "Can you deliver to a site with no loading bay?",
        "Driver was rude to our warehouse staff.",
    ],
}

urgencies = ["low", "medium", "high"]
urgency_weights = {
    "delays": [30, 45, 25],
    "tracking": [45, 40, 15],
    "damage": [15, 40, 45],
    "wrong_delivery": [25, 45, 30],
    "billing": [55, 35, 10],
    "refunds_claims": [45, 40, 15],
    "customs_hazardous": [10, 40, 50],
    "account_general": [75, 20, 5],
}

# NEW: "now" for the dataset. Fixed, so every run gives the same dates.
reference_date = datetime(2026, 10, 25, 9, 0)

tickets = [first_ticket]

for i in range(2, 501):
    category = random.choice(list(complaints.keys()))

    # NEW: when the ticket arrived and how long support took to reply
    age_hours = random.randint(1, 60 * 24)
    created_at = reference_date - timedelta(hours=age_hours)
    response_hours = round(random.triangular(4, 216, 68))
    if response_hours <= age_hours:
        status = "answered"
    else:
        status = "awaiting_response"
        response_hours = ""  # no reply yet, so unknown

    ticket = {
        "ticket_id": f"NW-{i:04d}",
        "customer": random.choice(customers),
        "order_id": "ORD-" + str(random.randint(10000, 99999)),
        "complaint": random.choice(complaints[category]),
        "category": category,
        "urgency": random.choices(urgencies, weights=urgency_weights[category])[0],
        "created_at": created_at.strftime("%Y-%m-%d %H:%M"),  # NEW
        "first_response_hours": response_hours,                 # NEW
        "status": status,                                       # NEW
    }
    tickets.append(ticket)

with open("data/tickets.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=first_ticket.keys())
    writer.writeheader()
    writer.writerows(tickets)

print("Saved", len(tickets), "tickets to data/tickets.csv")

# NEW: Daniel's number. Average first response for answered tickets.
total = 0
count = 0
for t in tickets:
    if t["status"] == "answered":
        total = total + t["first_response_hours"]
        count = count + 1

print("Answered:", count, "| Average first response:", round(total / count), "hours")