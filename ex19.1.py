def war_machines(tanks, planes, artilery):
    print "Our military force is composed of %d pieces of war machines" % (tanks + planes + artilery)


def war_machines_separate (tanks, planes, artilery):
    print "Divided we have the following forces:\n -%d Tanks\n -%d Planes\n -%d  Artilery Pieces\n" % (tanks, planes, artilery)
    
    
    
    
    
print "Numbers Directly:"
war_machines(30, 50, 5)
war_machines_separate(30, 50, 5)

print "Variables from Script:"
tanks = 40
planes = 60
artilery = 6

war_machines(tanks, planes, artilery)
war_machines_separate(tanks, planes, artilery)

print "Math + Variables:"
war_machines(tanks + 20, planes + 30, artilery + 5)
war_machines_separate(30+30, 50-20, 6-5)

print "Random.. or not :)"
war_machines(tanks - tanks, planes - planes, artilery - artilery)
war_machines_separate(2*tanks, 2*planes, 2*artilery)