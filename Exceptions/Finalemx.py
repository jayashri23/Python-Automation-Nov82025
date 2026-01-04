#finalize block of code run always if exception occurs or not

from weakref import finalize

num=100
num2=0

print("--Start program--")
try:
    n=num/num2
    print(n)
except ZeroDivisionError:
    print("ZeroDivisionError")
print("--End program--")

finalize
num3=num+num2
print("Sum:",num3)
print("Finalize block run")