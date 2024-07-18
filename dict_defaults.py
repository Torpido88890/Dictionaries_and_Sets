from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0) #It serches the key and returns its default value and also if key is not there it adds the key and initiate the value by 0.
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0) #it only searches the key and return the default valuue
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
