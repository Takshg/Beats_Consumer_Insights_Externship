import pandas as pd
import random

# Define mock data
products = [
    {"product_id": "PID001", "attributes": "Color: Black, Style: Wireless"},
    {"product_id": "PID002", "attributes": "Color: White, Style: Wired"},
    {"product_id": "PID003", "attributes": "Color: Red, Style: Over-Ear"},
    {"product_id": "PID004", "attributes": "Color: Blue, Style: Noise Cancelling"},
    {"product_id": "PID005", "attributes": "Color: Gray, Style: Bluetooth"}
]

reviews = [
    "The sound quality is amazing. Highly recommend!",
    "Decent for the price, but a bit uncomfortable.",
    "Battery life is poor, and the fit is uncomfortable.",
    "Exceeded my expectations. Great bass and clarity.",
    "Sound is okay, but there are better options."
]

# Generate synthetic dataset
data = []
for i in range(1, 101):
    product = random.choice(products)
    review = random.choice(reviews)
    data.append({
        "review_id": f"R{i}",
        "product_id": product["product_id"],
        "title": random.choice(["Great sound!", "Good value", "Not satisfied", "Amazing!", "Average"]),
        "author": f"User{i}",
        "rating": random.choice([1, 2, 3, 4, 5]),
        "content": review,
        "timestamp": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
        "is_verified": random.choice([True, False]),
        "helpful_count": random.randint(0, 50),
        "product_attributes": product["attributes"]
    })

# Save as CSV
mock_data = pd.DataFrame(data)
mock_data.to_csv("data/mock_dataset.csv", index=False)
print("Mock dataset created: mock_dataset.csv")
