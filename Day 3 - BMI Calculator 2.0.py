height = float(input("What is your height in inches?"))
weight = int(input("What is your weight in pounds?"))
bmi_output = ((weight/(height*height)) * 703)

if bmi_output < 18:
  print(f"Your BMI is {bmi_output}, you are underweight.")
elif bmi_output <= 24:
  print(f"Your BMI is {bmi_output}, you have a normal weight.")
elif bmi_output <= 29:
  print(f"Your BMI is {bmi_output}, you are slightly overweight.")
elif bmi_output <= 34:
  print(f"Your BMI is {bmi_output}, you are obese.")
elif bmi_output >= 35:
  print(f"Your BMI is {bmi_output}, you are clinically obese.")
