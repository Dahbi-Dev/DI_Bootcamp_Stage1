# 1
print('-----------')

list1 = [1, 2, 3, 4]
print(list1)
# 2 
print('-----------')

list2 = [1, 2, 3, 4]
for i in list2:
    print(i * 20)
    
# 3
print('-----------')
list3 =  ["Elie", "Tim", "Matt"]
list4 = []
for i in list3:
   list4.append(i[0])
print(list4)

    
# 4
print('-----------')

list5 = [1, 2, 3, 4, 5, 6]
list6 = []
for i in list5:
    if i % 2 == 0:
        list6.append(i)
print(list6)

# 5- Given two lists [1, 2, 3, 4] and 
# [3, 4, 5, 6], return a new list that contains only 
# the values present in both lists: [3, 4].

print('-----------')

list7 = [1, 2, 3, 4]
list8 = [3, 4, 5, 6]
list9 = []
for i in list7:
    if i in list8:
        list9.append(i)
print(list9)
#6-Given a list of words ["Elie", "Tim", "Matt"], return a new list
# with each word reversed and in lowercase: ["eile", "mit", "ttam"].

print('-----------')

list10 = ["Elie", "Tim", "Matt"]
list11 = []
for i in list10:
    list11.append(i[::-1].lower())
print(list11)

#7-Given two strings "first" and "third", return a new list 
# of the letters that are present in both strings: ["i", "r", "t"].

print('-----------')
first = "first"
third = "third"
first_list = []
for i in first:
    if i in third and i not in first_list:
        first_list.append(i)
    print(first_list)
    
#8- For all numbers between 1 and 100, return
# a list of the numbers that are divisible
# by 12: [12, 24, 36, 48, 60, 72, 84, 96].

print('-----------')
list12 = []
for i in range(1,101):
    if i% 12 ==0:
        list12.append(i)
print(list12)

#9-Given the string "amazing", return a list with all
# the vowels removed: ["m", "z", "n", "g"].

print('-----------')
string1 = "amazing" 
vowels = "aeiou"
list13 = []
for i in string1:
    if i not in vowels:
        list13.append(i)
print(list13)

#10-Generate a list with the following
# value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

print('-----------')
list14 = []
for i in range(3):
    inner_list = []
    for j in range(3):
        inner_list.append(j)
    list14.append(inner_list)
print(list14)

#11- Generate a list with the following structure
# [
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]  

print('-----------')
list15 = []
for i in range(10):
    inner_list = []
    for j in range(10):
        inner_list.append(j)
    list15.append(inner_list)
print(list15)







