def ad(a, b):
    print "Aduna %d si %d . . . " % (a, b)
    return a + b
    
def sc(a, b):
    print "Scade %d si %d . . . " % (a, b)
    return a - b
    
def inm(a, b):
    print "Inmulteste %d si %d . . . " % (a, b)
    return a * b
    
def im(a, b):
    print "Imparte %d si %d . . . " % (a, b)
    return a / b
    
adunare=ad(5,5)
scadere=sc(8,6)
inmultire=inm(5,6)
impartire=im(8,4)

print "Rezultatele sunt urmatoarele:\nAdunarea -> %d\nScaderea -> %d\nInmultirea -> %d\nImpartire -> %d\n" % (adunare, scadere, inmultire, impartire)

print "Si acum partea complicata dar si partea fun :)"

puzzle = ad(adunare, sc(scadere, inm(inmultire, im(impartire, 2))))

print "Rezultatul este: ", puzzle, "Destept nu? :)"