#-1. Given a list: [("name", "Elie"), ("job", "Instructor")], 
# create a dictionary that looks like this: 
# {'job': 'Instructor', 'name': 'Elie'} 
# (Note: The order does not matter).
print('-----------')
list1 = [("name", "Elie"), ("job", "Instructor")]
dict1 = {}
for key, value in list1:
    dict1[key] = value
print(dict1)

#2. Given two lists: ["CA", "NJ", "RI"] and 
# ["California", "New Jersey", "Rhode Island"], 
# return a dictionary that looks like this:
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
print('-----------')

list2 = ["CA", "NJ", "RI"]
list3 = ["California", "New Jersey", "Rhode Island"]
dict2 = {}
for i in range(len(list2)):
    dict2[list2[i]] = list3[i]
print(dict2)

#3. Create a dictionary where the keys are vowels in the alphabet
# and the values are 0. Your dictionary should look like this: 
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
# (Do not use the fromkeys method).
print('-----------')
vowels = ['a', 'e', 'i', 'o', 'u']
dict3 = {}  
for vowel in vowels:
    dict3[vowel] = 0
print(dict3)

#4. Create a dictionary where the key is the
# position of the letter in the alphabet, 
# and the value is the letter itself.
# You should return something like this:

print('-----------')
import string
alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
dict4 = {}
for index, letter in enumerate(alphabet, start=1):
    dict4[index] = letter
print(dict4)