#multiple error with general exception
num1=10
num2=0

try:
  num=num1/num2
  print(num)

except ValueError as e:
    print("Value Error")
except ZeroDivisionError:
    print("Division by zero")

except Exception as e:
    print("General Error")

