'''
winning_percentage = 73.81
print(type(winning_percentage))
x = 8 + 22 *7 - 4
print(x)
names = {"0":"Jimmy", "1":"Lex","2":"Jayden"}
print(names,["0"])
'''
'''
#Append Dictionary to list
#Remember to ask question on how to add to specific position in a dictionary
dick = {"country": "El Paso", "registered_voters": 123456}
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(2, dick)
print(voting_data)
'''
'''
IF & Nested IF Statement Examples
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

score = int(input("What is your test score?"))
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
'''
'''
IF-ELIF_ELSE Statement
In an if-elif-elsestatement, the if, elif, and elsestatements are all aligned, and the conditionally executed blocks are indented.
socre = int(input("What is your test score?"))
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    '''
'''
#Membership Operators IN & NOT IN
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
    '''
'''
#Logical Operators AND, OR, NOT combined with Membership
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties."
'''
'''
#While Loop
x = 0
while x <= 5:
    print(x)
    x = x + 1
'''
'''
#For Loops
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
'''
'''
counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])
'''
'''
#This allows you to loop through dictionary using the key()method and for loop 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
'''
''''
#This will get us the value of the keys in a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
    #print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
'''
'''
#Item method will print the key, value pairs of the dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in counties_dict.items():
    print(str(key) + "county has " + str(value) + " registerd voters")
'''
'''
#For loop can iterate through multiple dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
    #print(county_dict)
#for i in range(len(voting_data)):

      #print(voting_data[i])
 # We can retrieve the values only by using a nested for loop
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)   
# We can choose to only get the values from registered voters
for county_dict in voting_data:
    print(county_dict['registered_voters'])   
''' 