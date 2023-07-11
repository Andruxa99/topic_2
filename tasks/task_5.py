weight_in_grams: int = 350000

weight_in_kilograms: float = 350000 / 1E3
weight_in_tons: float = 350000 / 1E6
# или так
# weight_in_tons: float = weight_in_kilograms / 1E3

print("Вес в килограммах:", weight_in_kilograms)
print("Вес в тоннах:", weight_in_tons)
