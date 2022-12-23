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



Write a program that always asks the user to enter a number. When the user enters the negative number -1, the program should stop requesting the user to enter a number. The program must then calculate the average of the numbers entered excluding the -1.

Make use of the while loop repetition structure to implement the program.
