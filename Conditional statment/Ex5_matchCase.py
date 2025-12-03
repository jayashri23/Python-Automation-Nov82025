from unittest import case

#Cases example: if case not match then use underline symbol
#when multiple option available then use case loop
num=7
match num:
    case "sunday":
        print("1")
    case "monday":
        print("2")
    case "tuesday":
       print("3")
    case "wensday":
        print("4")
    case "thursday":
        print("5")
    case "friday":
        print("6")
    case "saturday":
       print("7")
    case _:
        print("Please enter valid input")

