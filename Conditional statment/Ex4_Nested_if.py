Pre=900
if Pre>=400:     #outer_If
    print("Entrance Exam clear")
    Main=8600
    if Main>=700:  #innner if
        print("Main exam cleared")
        print("Congratulations!")
    else:
        print("Main exam not cleared")
        print("Try next time")
else:
    print("Entrance Exam not clear")



ShoppingAmt=330
print("###############")
if ShoppingAmt>=300:
    print("free delivery")
    amt=20
    if amt>=200:
        print(" additional 10% discount")
    else:
        print("No additional discount")
else:
    print("not free delivery")
