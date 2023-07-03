def print_part_of_string(string, start_char, end_char):
    start_index = string.find(start_char)
    end_index = string.find(end_char)
    
  
    if start_index != -1 and end_index != -1:
   
        part_of_string = string[start_index:end_index+1]
        return part_of_string
    else:
        return None

string = input("Enter a string: ")
start_char = input("Enter the start character: ")
end_char = input("Enter the end character: ")

result = print_part_of_string(string, start_char, end_char)

if result is not None:
    print("Part of the string:", result)
else:
    print("Start or end character not found in the string.")
