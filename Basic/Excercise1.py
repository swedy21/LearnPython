# Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum

print("""Feladat: Given two integer numbers return their product.
If the product is greater than 1000, then return their sum \n""")

number1 = input("Első szám: ")
number2 = input("Második szám: ")

if number1*number2 > 1000:
    print("A két szám összege: {}", number1+number2)
else:
    print("A két szám szorzata: {}", number1*number2)
