# Working with Strings:-
# for X in "Kush":
#     print(X, end = "eats")
# for x in "banana":
#     print(x)

mystr = "kush is a good boy"
print(mystr)

print(mystr[:4])
print(mystr[1:])
print(mystr[0:3])    # Here 0 is included but 3 is excluded.
print(mystr[0:4])    # Here 0 is included but 4 is excluded.

# Length of any string
print(len(mystr))         # Length is 18 but index will start from 0 to 17
print(mystr[0:18])        # If we want full string then enter the full length in the square bracket as shown.

print(mystr[0:4:2])       # the value printed will be ks (first check 0 to 4(Kush) then last :2 represents -skipping of everynext character.)

print(mystr[::-1])        # It will reverse the string. How it works (in shortmake the last digit positive and then reverse the string

print(mystr[::-2])      # First write the output by skiping one character (That is output what comes when the digit 2 is positive.then reverse

print(mystr[-3:-2:1])

print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.endswith("boy"))
print(mystr.endswith("bdoy"))
print(mystr.capitalize())  # It will capitalize first letter of the string
print(mystr.count("o"))    # It will count how many times the "o" occurs in the string
print(mystr.find("is"))    # It will return the index from where "is" is starting
print(mystr.lower())       # full string will become lower
print(mystr.upper())       # full string will become in upper case
print(mystr.isupper())
print(mystr.replace("is", "are"))

# Check string

mystring = "Kush is Best student"
print("Best" in mystring)     # Output = True
print