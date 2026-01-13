def BMI(w, h):
    bmi = float(w) / (float(h) ** 2)
    return bmi


weight = input("Weight(kg) : ")
height = input("Height(m) : ")

print(f"BMI = {BMI(weight, height):.2f}")
