number = [1,2,4,1,8,6,5,87,5,]
new_num =[num**2 for num in number]
print(new_num)

even_num =[num for num in number if num%2 == 0]
print(even_num)