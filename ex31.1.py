print "You enter a dark room with three doors labeled 'Door 1' 'Door 2' and 'Door 3'. Which door do you choose?"

door = raw_input("> ")

if door == " Door 1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "Thea bear eats your face off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "Door 2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothspins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input ("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else: 
        print "The insanity rots your eyes into a pool of muck. Good job!"
        
elif door == "Door 3":
    print "This door is full of snakes. What can you do?"
    print "1. Use the flamethrower"
    print "2. Try to exit the room"
    print "3. Eat all the snakes" 
    
    snakes = raw_input ("> ")
    
    if snakes == "1":
        print "You lucky mofo! Al the snakes are crisped.. where the fuck do you find a flamethrower?"
    elif snakes == "2": 
        print "Burned!! There is no other room!!"
    elif snakes == "3":
        print "How can you eat so many snakes? you fat bastard!"
    else:
        print "You are eaten by the snakes"

else: 
    print "You stumble around and fall int a knife and die. Good job!"