# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here

# Create a Dictionary
courses={'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60}

#See the marks
print(courses)

#Add all the marks
total=65+70+80+70+60

#print total
print(total)

#Calculate the percentage
percentage=(345/500)*100

#print percentage
print(percentage)

# Code ends here


# --------------
# Code starts here

#Create a dictionary
mathematics={'Geoffrey Hinton':78 , 'Andrew Ng':95 , 'Sebastian Raschka':65 , 'Yoshua Beniio':50 , 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

# calculate the max value

topper = max(mathematics,key = mathematics.get)
print (topper)


# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here

#split the name
first_name=topper.split()[0]
last_name=topper.split( )[1]

#Display the name
full_name=last_name +' '+first_name
print(full_name)

# Convert in to uppercase
certificate_name=full_name.upper( )

# Print the name
print(certificate_name)
# Code ends here


