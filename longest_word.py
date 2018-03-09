#Ammaar Siddiqui
#Comp Prog
#3/6/18
def find_word():#defines function
    file=open("alice.txt","r")#opens the file
    everything=[]#makes empty list
    all_lines=file.readlines()#reads everything
    for x in all_lines:#for every line in all the lines it
        x=x.split()#splits the lines
        for y in x:#for evry word in the line
            everything.append(y)#appends to the empty list
    word=""#makes an empty string
    for x in everything:#for x in every word
        if len(x)>len(word):#checks if the length is larger than the word efors
            word=x#if it is than that word is now wthe longest word
    print('The longest word is "'+word+'". It is '+str(len(word))+" characters long")#prints message with the longest word

find_word()#runs the function
