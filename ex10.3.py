a = "Now I will make a list"
b = """
This list will contain the neceessary hardware to build a ne PC.
Here is the list: 
\t - Flat Screen 
\t - Case 
\t - Power Source 
\t - Mother Board
\t - Video Card 
\t - Peripherals
""" 

screen = 300
case = 50
power = 50
mother = 150
video = 1000
periph = 200
total_cost = screen + case + power + mother + video + periph

c = "The total price of the new PC will be %s$" % (total_cost)

d = "Here is the list of component by price:" 
e = "\t - Flat Screen costs: %s$" % screen
f = "\t - Case costs: %s$" % case
g = "\t - Power Source costs: %s$" % power
h = "\t - Mother Board  costs: %s$" % mother
i = "\t - Video Card costs: %s$ (expensive isn't it?!)" % video
j = "\t - Peripherals costs: %s$" % periph

print a
print b
print c
print d
print e
print f
print g
print h
print i
print j
