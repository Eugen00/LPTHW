x = "There are %d types of people." %10 #this is where you asign the variable x and give value to %d
binary = "binary" #variable asignment
do_not = "don't"  #variable asignment
y = "Those who know %s and thos who %s." %(binary, do_not) #variable asignment that contains 2 strings in one string

print x #afisarea variabilei x
print y #afisarea variabilei y


print "I said: %r." %x #folosirea %r arata ca pc-ul afiseaza atat formatul %s cat si %d
print "I also said; '%s'." %y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #??

print joke_evaluation % hilarious #??

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#adaugand + intrecele doua stringuri w si e creeaza un string care contine cele doua stringuri

