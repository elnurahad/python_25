from typing import List, Tuple


def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
    total_price = 0.0
    for product in products:
        total_price += product[1] * product[2]
    return total_price


products = [
    ("Apple", 1.50, 10),
    ("Banana", 0.75, 15),
    ("Orange", 1.25, 20),
    ("Grapes", 2.00, 5)
]

with open("products.txt", "w") as file:
    for product in products:
        file.write(f"{product[0]}, {product[1]}, {product[2]}\n")

print("File 'products.txt' has been successfully created")


with open("products.txt", "r") as file:
    lines = [line.strip().split(", ") for line in file.readlines()]

product_list = [(item[0], float(item[1]), int(item[2])) for item in lines]
print("Total price :", calculate_total_price(product_list))