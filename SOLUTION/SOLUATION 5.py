def a(string):
   
    vowels = ['a', 'e', 'i', 'o', 'u']
 
    count = 0
    string = string.lower()
    
    for char in string:
       
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
result = a(string)
print("Number of vowels:", result)
