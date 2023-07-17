def a(number):
   
    num_str= str(number)
    power = len(num_str)
    
  
    digit_sum = sum(int(digit) ** power for digit in num_str)
    

    if digit_sum == number:
        return True
    else:
        return False

num = input("Enter a number: ")


if num.isdigit():
    num = int(num)
    if a(num):
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")
else:
    print("Invalid input. Please enter an integer number.")
