# Q1
fruits_list =[]

# Q2
n = int(input("Enter the number of elements for the list: "))
for i in range(n):
    print("Enter the element:")
    ele=input()
    fruits_list.append(ele)

# Q3
print(fruits_list[1])
print(fruits_list[3])
print(fruits_list[1:2:1])

# Q4
print("fruits in the list: ", len(fruits_list))

# Q5
fruits_list[3]="Pear"
print(fruits_list)

# Q6
print("apple" in fruits_list)

# Q7
fruits_list.remove("banana")
fruits_list.pop()
print(fruits_list)

# Q8
additional_fruits=['watermelon','kiwi']
fruits_list=fruits_list+additional_fruits
print(fruits_list)

# Q9
fruits_list.sort()
print(fruits_list)

# Q10
print(fruits_list.count('kiwi'))