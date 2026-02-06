Soap="mum"
print("OriginalString:",Soap)
rev=Soap[::-1]
print("ReverseString:",rev)

if Soap==rev:
    print("Palindrome")
else:
    print("Not Palindrome")