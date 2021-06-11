'''
#Function 1
def two_lists(n): #Define the function two_list to n
  list_1 = [] # Create first list for the numbers
  list_2 = [] #Create a second list for the word
  for i in n: #Create a for loop for i in n
    if i.isdigit() == True: #Create an if statement that's true
      list_1.append(i) #append() list_1 which adds a single item to the existing list
    else: #Create you else in the if statement
      list_2.append(i) #append() list_2 which adds a single item to the existing list
  print("Numbers List:") #Print a prompt that shows the number list output
  print(list_1) #Print list 1 which is the list with numbers
  print("Words List:") #Print a prompt that shows the word list output
  return list_2 #end the execution(returns) of list_2

print(two_lists([(s) for s in input("Type in any letter and/or number separated by spaces:\n").split()])) #Prompt the user to input letters or numbers separated by spaces and all placed in one line
'''

'''
#Function 2
def descend(n): # defining the function descend to n
  even_list = [] #Create a list called even_list
  length = len(n) #Find the length of n
  for i in range(length): #create a for loop with a range for length
    if i * 2 // 2 % 2 == 1: #create an if statement of the remainder of 2 being able to equal 
      even_list.append(int(n[i])) #append() even_list which adds a single item to the existing list
  for i in range(length): #create a for loop with a range for length
    if i * 2 // 2 % 2 == 1: #create an if statement 
      n[i] = (str(max(even_list))) #this finds the max numbers
      place = even_list.index(max(even_list)) #search for a given element from the start of the list and returns the lowest index 
      even_list[place] = 0 #Deletes the max number
  print("Every second number is now in order:") #
  return (' '.join(n)) #end the execution(return) and joins n

a = input("Input any number: \n") #Prompt the user to input any number
s= a.split() #split returns the list of the words in the string/line
print(descend(s)) # prints the function descen and (s)
'''
