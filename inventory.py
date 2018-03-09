#Ammaar Siddiqui
#Comp Prog
#2/28/18
import time#imports time so I can use the functions time has
def dictionaries():#main function
    inventory={"apples":500,"oranges":250,"bananas":200,"pears":300}#defines all the key-value pairs in the dictionary
    what=input("What item do you need to change: ")#asks what item you want to change
    minus=int(input("How many to remove: "))#asks how many you want to remove
    inventory[what]-=minus#minuses that amount
    print("You now have "+str(inventory[what])+" "+what)#prints the message
    time.sleep(3)#waits for three seconds
    quit()#quits program

dictionaries()#runs main function
    
