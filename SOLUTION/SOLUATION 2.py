def sum_of_digits(number):
   
    b= str(number)
   
    digit_sum = 0
    

    for digit in b:
       
        digit_sum += int(digit)
  
    return digit_sum

num = int(input("Enter a number: "))


result = sum_of_digits(num)
print("Sum of digits:", result)
