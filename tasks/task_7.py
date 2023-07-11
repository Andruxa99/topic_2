cost: int = 1000
discount: int = 20
quantity: int = 3

# total_cost: float = (cost - (cost * (discount / 100))) * quantity
total_cost: float = (cost * (1 - discount / 100)) * quantity

print("Стоимость вашего заказа:", total_cost, "рублей")
