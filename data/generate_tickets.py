# Week 1: generate synthetic Northwind support tickets
import random
import csv

random.seed(42)

first_ticket = {
    "ticket_id": "NW-0001",
    "customer": "Harbour Foods Ltd",
    "order_id": "ORD-48213",
    "complaint": "Pallet shows as in Rotterdam for 9 days. Where is it?",
    "urgency": "high",
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

complaints = [
    # Delays
    "Delivery arrived two days late.",
    "Our shipment was due Tuesday and still hasn't arrived.",
    "Third late delivery this month. We're losing patience.",
    "Collection was booked for 9am, driver never showed up.",
    "Order stuck at the Felixstowe depot for a week.",
    "Your estimated delivery date has changed four times.",
    "Need this pallet before Friday or our production line stops.",
    "Delivery window was 8-12, driver came at 6pm.",
    # Tracking
    "Tracking page has not updated since Monday.",
    "Tracking says delivered but nothing arrived.",
    "The tracking link in your email doesn't work.",
    "Status has said 'in transit' for 11 days.",
    "Tracking shows our goods in Manchester, but they were going to Bristol.",
    "Can't find my order on your website using the order number.",
    # Damage
    "Two boxes in the shipment were damaged.",
    "Pallet was wrapped badly and half the cartons were crushed.",
    "Glass items arrived broken.",
    "Refrigerated goods arrived warm. The whole load is spoiled.",
    "Forklift damage on three pallets.",
    "Packaging was wet when it arrived, stock is ruined.",
    "Seal on the container was broken on arrival.",
    # Wrong delivery
    "Driver left the goods at the wrong dock.",
    "We received someone else's order.",
    "Only 8 of 12 pallets were delivered.",
    "Goods went to our old address even though we updated it.",
    "Driver refused to unload at our site.",
    "Delivery was left outside in the rain with no signature.",
    # Billing
    "Invoice amount does not match the quote.",
    "We were charged twice for the same shipment.",
    "Fuel surcharge on our invoice wasn't in the contract.",
    "Still waiting for a credit note promised last month.",
    "Invoice has the wrong VAT number.",
    "Why was there a waiting time charge? Your driver was late, not us.",
    "Need a copy of an invoice from last March.",
    # Refunds and claims
    "How do I claim for damaged goods?",
    "Submitted a claim 6 weeks ago and heard nothing.",
    "Want a refund for the late delivery as per our agreement.",
    "Your claim form keeps rejecting our upload.",
    "What is your refund policy for missed collections?",
    # Customs and hazardous goods
    "Shipment held at customs. What paperwork is missing?",
    "Do you need an export declaration for goods to Norway?",
    "Can you transport lithium batteries?",
    "Hazardous goods label missing on our delivery note.",
    # Account and general
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
]

urgencies = ["low", "medium", "high"]

tickets = [first_ticket]

for i in range(2, 501):
    ticket = {
        "ticket_id": f"NW-{i:04d}",
        "customer": random.choice(customers),
        "order_id": "ORD-" + str(random.randint(10000, 99999)),
        "complaint": random.choice(complaints),
        "urgency": random.choices(urgencies, weights=[50, 35, 15])[0],
    }
    tickets.append(ticket)

with open("data/tickets.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=first_ticket.keys())
    writer.writeheader()
    writer.writerows(tickets)

print("Saved", len(tickets), "tickets to data/tickets.csv")