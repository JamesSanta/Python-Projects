#
# Python: 3.11.4
#
# Coder: James Santa

def start(nice=0,mean=0, name=""):
    # Getting user info
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """Check if this is a new game.
    If it is then get users name
    If it is not a new game thank the player for playing and continue."""

    #If users name is not known they are a new player and name is needed.
    
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop == True:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches your for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick =="n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms of...")
            mean = (mean+ 1)
            stop = False
         
    pick = input("\nA stranger asks you for a \ndollar. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
    if pick =="n":
            print("\nThe stranger walks away smiling and thanking you...")
            nice = (nice + 1)
            stop = False
    if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms of...")
            mean = (mean+ 1)
            stop = False

    pick = input("\nA stranger asks you for \nthe time. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
    if pick =="n":
            print("\nThe stranger walks away smiling and thanking you...")
            nice = (nice + 1)
            stop = False
    if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms of...")
            mean = (mean+ 1)
            stop = False
    score(nice,mean,name) # # variables to the score
    
def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #function is being passed values stored in the 3 variables
    if nice > 2:    #if condition is valid, call the win function passing in the variables for use
        win(nice,mean,name)
    if mean > 2:    #if condition is valid, call the lose function passing in the variables for use
        lose(nice,mean,name)
    else:   #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute wildcards for variables values
    print("\nNice job {}, you win! \nEveryones loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    # Substitute wildcards for variables values
    print("\nAhhh, too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call the again function and pass in the variables
    again(nice,mean,name)
    



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #The name variable does not reset as it is the same user playing the game
    start(nice,mean,name)

    
    



if __name__ =="__main__":
    start()
