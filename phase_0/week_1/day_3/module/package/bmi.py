def BMI(nama,weight,height): #wight in kg and height in m
    BMI_formula = weight / (height**2)
    if BMI_formula > 0:
        if BMI_formula < 18.5:
            return print(f"BMI {nama} = {round(BMI_formula,2)} masuk dalam kategori underweight")
        elif 18.5<=BMI_formula<= 24.9:
            return print(f"BMI {nama} = {round(BMI_formula,2)} masuk dalam kategori normal")
        elif 25<=BMI_formula<= 29.9:
            return print(f"BMI {nama} = {round(BMI_formula,2)} masuk dalam kategori overweight")
        else:
            return print(f"BMI {nama} = {round(BMI_formula,2)} masuk dalam kategori very overweight")
    else:
        return print(f"BMI {nama} tidak valid")