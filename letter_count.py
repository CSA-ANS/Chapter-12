def counting_letters(text):#runs function using whatever string is passed to it
    count={}#makes empty dictionary
    for letter in text:#rusn through the string
        if letter in count.keys():#if the key is already there it
            count[letter]+=1#adds one
        else:#if not
            count[letter]=1#it makes anew key and gives it the value of 1
    return count#returns the dictionary
what=input("What string would you like to count: ")#asks for what string they would like to count
print(counting_letters(what))#passes what they enetered to the function and runs it
