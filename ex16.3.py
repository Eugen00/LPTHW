from sys import argv
script, file = argv

txt = open(file)

print "The file %r will be oppened now" %(file)

print txt.read()