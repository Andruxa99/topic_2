oklad: int = 50000
tax_rate: float = 0.13

tax: float = oklad * tax_rate
salary: float = oklad - tax

print("Размер з/п:",oklad,"рублей")
print("Налог:",tax,"рублей")
print("Сумма на руки:",salary,"рублей")
