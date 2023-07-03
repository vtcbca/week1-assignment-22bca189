def a(number):
    b=str(number)
    if b==b[::-1]:
        return True
    else:
        return False
num=input("Enter a number:")

if num.isdigit():
    num=int(num)
    if a(num):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Invalid input.please enter a valid number.")
