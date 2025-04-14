student_data ={
    "id1":{
        'name':"Aarav",
        'age':10
    },
    "id2" :{
         'name':"ishaan",
        'age':7
    }
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

#activity2 

# Initialize dictionary
test_dict = {'Hello' : 5, 'what' : 2, 'is' : 5, 'your' : 5, 'name' : 5}
  
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
  
# Initialize value 
K = 5
  
# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
      
# printing result 
print("Frequency of K is : " + str(res))





#activity 3

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
 
# search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
 
# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))

#acp

# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print dictionary
print("Test Dictionary:", test_dict)

# Ask user for the value to search frequency
value = int(input("Enter the value to check its frequency: "))

# Calculate frequency (number of keys having this value)
frequency = list(test_dict.values()).count(value)

# Display the result
print(f"The frequency of value '{value}' in the dictionary is: {frequency}")





