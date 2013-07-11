from sys import argv
script, file = argv

text = open(file)

print "The file %r will be oppened now." % (file)
print text.read()

text.close()