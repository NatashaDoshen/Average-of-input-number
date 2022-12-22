list_of_numbers = []
max_length = 10

while len(list_of_numbers) < max_length:
  number = input("enter the number")
  list_of_numbers.append (int(number))
  print(list_of_numbers)
  if number == "-1":
    break
  

res = sum(list_of_numbers)

print(res)
excluding_number = res +1
print(excluding_number)

avg = excluding_number/len(list_of_numbers)
print(avg)
