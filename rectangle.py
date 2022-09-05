#Exercise 2.5
talents = input("Enter talents:\n")
pounds = input("Enter pounds:\n")
lots = input("Enter lots:\n")

f_tl = float(talents)
f_pnds = float(pounds) + f_tl * 20
f_lots = float(lots) + f_pnds * 32

kilo = int(f_lots * 13.3 // 1000)
print(kilo, f_lots)

print("The weight in modern units:")
print(kilo, "kilograms and", f_lots * 13.3 - (kilo * 1000), "grams.\n")