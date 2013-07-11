from sys import argv

script, user_name, number = argv
prompt = '>>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Where do you live %s?" % user_name
live = raw_input(prompt)

print "Are you a boy or a girl %s?" % (user_name)
gender = raw_input(prompt)

print "I know that you have %s pets!" % (number)

print "Am I right %s? Do you have %s pets?" % (user_name, number)
raw_input(prompt)

pets = number

print """
Alright, so you live in %r.
I also know that you are a %r.
And you have %r pets. Nice!.
""" % (live, gender, pets)