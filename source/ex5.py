def inches_to_cm(inches):
    return inches * 2.54


def lbs_to_Kg(lbs):
    return lbs * 0.453592


name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = inches_to_cm(height) #cm
weight_in_kg = lbs_to_Kg(weight)  # Kg

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall ({height_in_cm} cm).")
print(f"He's {weight} pounds heavy ({weight_in_kg} kg). ")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age} years, {height} height, and {weight} lbs I get {total}.")
