from sys import argv

script, filename = argv

txt = open(filename)

print "Her's your file %r:" % filename
print txt.read()

