"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

numbers = {
    "zero" : 0, 
    "one" : 1,
    "two" : 2,
    "three": 3,
    "four" : 4,
    "five" : 5 
}
print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


suma = numbers[a] + numbers[c]
subt = numbers[a] - numbers[c]

if b == "plus": 
        print(f"{a} plus {c} equals {suma}")
if b == "minus": 
        print(f"{a} minus {c} equals {subt}")



print("Thanks for using this calculator, goodbye :)")
print("And dont forget to subscribe to my YT channel: Charlie Sket")


# Lo único que no consigo a la hora de meter un input inválido es que salga el error 
# que yo quiera, he probado try/except en todas partes pero lo único que hago es estropear el código. 
