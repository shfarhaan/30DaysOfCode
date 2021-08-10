# Enter your code here. Read input from STDIN. Print output to STDOUT

# First we import system library to read STDIN
import sys 

# Then we will read in the phonebook entries
n = int(sys.stdin.readline().strip())

# We create our phonebook variable which is a Dictionary Datatype
phone_book = dict()

# Then we read n numbers of std input
for i in range(n):
    # for each line we will split the line into the name and phone number
    entry =  sys.stdin.readline().strip().split(' ')
    
    # Now we add that to the phone_book dictionary
    phone_book[entry[0]] = entry[1]
    
# Here we read in the queries
query = sys.stdin.readline().strip()

# We'll start by reading the first value, and while there is a valid query to execute
# we will look-up the number in our phone_book

while query:
    phone_number = phone_book.get(query)
    
    # if the phone_number exists, we will print the results of our query 
    # else print "Not found" if goes otherwise.
    if phone_number:
        print(query + '=' + phone_number)
    else:
        print('Not found')
    query = sys.stdin.readline().strip()