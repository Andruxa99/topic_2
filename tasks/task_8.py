oklad: int = 50000
tax_rate: float = 0.13

tax: float = oklad * tax_rate
salary: float = oklad - tax

print("Размер зарплаты:", oklad, "рублей")
print("Размер подоходного налога:", tax, "рублей")
print("Сумма на руки:", salary, "рублей")
