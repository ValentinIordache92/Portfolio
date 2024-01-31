def ft_and_inch_to_m (ft, inch = 0):
    return ft * 0.3048 + inch * 0.0254
    
def pound_to_kg (pound):
    return pound * 0.4535923

def bmi (weight, height):
    if weight < 20 or weight > 250 or height < 1 or height > 2.5:
        return None
    
    return weight / height ** 2

x = int(input("Press 1 if you want to express you weight in pounds or 2 if you want in kg: "))
y = int(input("Press 1 if you want to express your height in ft or 2 if you want in m: "))

if x == 1 and y == 1:
    pound = int(input("Select weight(lb): "))
    ft = int(input("Select height(ft): "))
    inch = int(input("Select height(inch)(press 0 if none): "))
    bmi_result = bmi(pound_to_kg(pound), ft_and_inch_to_m(ft, inch))

if x == 1 and y == 2:
    pound = int(input("Select weight(lb): "))
    height = float(input("Select height(m): "))
    bmi_result = bmi(pound_to_kg(pound), height)

if x == 2 and y == 1:
    weight = int(input("Select weight(kg): "))
    ft = int(input("Select height(ft): "))
    inch = int(input("Select height(inch)(press 0 if none): "))
    bmi_result = bmi(weight, ft_and_inch_to_m(ft, inch))

if x == 2 and y == 2:
    weight = int(input("Select weight(kg): "))
    height = float(input("Select height(m): "))
    bmi_result = bmi(weight, height)

print(bmi_result)

try:
    if bmi_result < 18.5:
        print("Underweight")
    elif bmi_result >= 18.5 and bmi_result < 25:
        print("Healthy weight")
    elif bmi_result >= 25 and bmi_result< 30:
        print("Overweight")
    else: print ("Obesity")

except:
    print("Wrong input of weight or height")