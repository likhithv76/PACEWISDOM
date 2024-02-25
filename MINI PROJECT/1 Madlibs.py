take = input("Hello!\U0001F600, would you like to play the Mad Libs game? (y/n)")
if take == 'y':
    Adjective = input("Adjective: ")
    Name1 = input("Name: ")
    Name2 = input("Another Name: ")
    Noun = input("Noun: ")

    madlib = f"{Name1} and {Name2} had been planning their {Adjective} adventure for months. They packed their {Noun} and set off on a journey to explore the {Adjective} lands beyond their {Noun}. Along the way, they encountered {Adjective}challenges and made {Adjective} memories that would last a lifetime."
    print(madlib)

elif take == 'n':
    print("okay, see you later")

else:
    print("Invalid Option!")


  
