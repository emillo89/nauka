#List

fruits = ['Cherry','Apple', 'Pear']
states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
          "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
          "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
          "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
          "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
          "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
          "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# count states
num_of_states = len(states)
print(num_of_states)

#latest state
lates = states[-1]
print(lates)

# first states
print(states[0])

#extend list
states.extend(['Emil','Kowalski'])
print(states)