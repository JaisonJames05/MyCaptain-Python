list1= [12, -7, 5, 64, -14] 
list2= [12, 14, -95, 3]
pos_num1 = list(filter(lambda x: (x >= 0), list1))
pos_num2 = list(filter(lambda x: (x >= 0), list2))
print(f"Input 1:{list1}")
print(f"Positive numbers in list 1 are : {pos_num1}")
print(f"Input 2:{list2}")
print(f"Positive numbers in list 2 are : {pos_num2}")

