from colorama import Fore, Back #I downloaded a library with colors and I imported modules named Fore and Back

def MyPolin(a: str) -> str: # I define a function MyPolin with parameter "a" from a string class
    a=a.lower() # I call a string method "lower", methods returns new values (a copy of string) for "a" argument and assigns the value to "a". This method converts a string into lower case.
    IDontNeed = [" ",",",".","!","?","'","-"] #I create a data set that includs symbols which need to be deleted from the string
    for BadSymbol in IDontNeed: #a key word "for" for a loop to execute a set of statements, once for each item in a data set
        a = a.replace(BadSymbol,"") # I call a string method "replace" which returns a string where BadSymbol is replaced with "" (ie remove) and assigns the value to "a".
    return a == a[::-1] # at the end of the body of the function MyPolin I return a boolean value True (if "a" equal revesed "a") or False
# Slicing p[::-1] in Python means - get the characters from position 0 : to the "end" position (till the last character) : with step (-1 means to start the slice from the end of the string)
print(Fore.BLACK)
print(Back.CYAN)
p = input("Please, write something down : ") #I assign the value from the console to "p" (the function "input" always return a string)

if MyPolin(p): #a key word "if" checks logical conditions (returns a boolean value True or False) - if the function MyPolin returns True
    print(Back.GREEN)
    print(p, 'has been already a palindrome') # then prints this phrase
else:
#otherwise I check a potential palindrome (according to to the task (spec) - this is a palindrome with 2 reversed letters
    is_polin = False #when this value be equal True you will see "This is not a palindrome"
    p_list = list(p) #I need to use a list in Python istead of string values to have a chance to change the original string
    for i in range(0, len(p)-1): #this loop to execute a set of statements, once for each item in list "p" from i = zero index of list "p" to i = length of the list "p" without last 2 indexes
        tmp = p_list[i] #tmp assigned i-th symbol
        p_list[i] = p_list[i+1] #on the previous symbol I assigne a second symbol
        p_list[i+1] = tmp #on the first symbol I assigne "tmp"
        new_string = ''.join(p_list) #I assigne to a new variable "new_string" the value from string method "join" that can take any items in a tuple (in this case "p_list") into a string

        if MyPolin(new_string): #I call the function MyPolin with argument "new_string", if it returns "True"
            is_polin = True #then is_polin assignes to True
            break #exit the loop when is_polin = True
        else: #if MyPolin is False, then I return a list to the initial state
            p_list[i+1] = p_list[i]
            p_list[i] = tmp
    if is_polin: #when True
        print(Back.MAGENTA)
        print('This is a potential palindrome: ', str(new_string))
    else:
        print(Back.RED)
        print('This is not a palindrome')
input()
