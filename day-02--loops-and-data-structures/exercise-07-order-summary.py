orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

for orderID , dict in orders.items():
    print(orderID , dict["customer"])

completed = 0
for orderID , dict in orders.items():
    if dict["status"] == "Completed":
        print(orderID , dict["customer"])
        completed +=1

pending = len(orders) - completed

orders["ORD-004"] = {
    "customer" : "Samrat",
    "amount"   : 100000,
    "status"   : "Completed"
}

print(f"Completed : {completed}")
print(f"Pending : {pending}")
print(orders)
