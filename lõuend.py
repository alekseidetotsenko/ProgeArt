from mustrid import*
from kunst import *
from kribukrabu import*
import cairo
from inspect import getmembers, isfunction # nende abil saab kujunduste faili funktsioonidest listi teha

def lõuend(cr, muster, laius, kõrgus, taust, värv):
    print(taust)
    print(värv)
    if taust == 1:
        cr.set_source_rgba(int(värv[0][0]/255), int(värv[0][1]/255), int(värv[0][2]/255), 0.5)
    else:
        cr.set_source_rgba(0, 0, 0, 0)
    cr.rectangle(0, 0, laius, kõrgus)
    cr.fill()
    
    eval(muster)(cr, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    
# funktsioonid svg ja png loomiseks
def svg_fail(muster, laius, kõrgus, faili_nimi, taust, värv):
    pilt = cairo.SVGSurface('Valminud kunstiteosed/' +faili_nimi + '.svg', laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, muster, laius, kõrgus, taust, värv)#teeb pildi põhja ja kutsub välja vastava
    
    pilt.finish()
    
def png_fail(muster, laius, kõrgus, faili_nimi, taust, värv):
    pilt = cairo.ImageSurface(cairo.FORMAT_ARGB32, laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, muster, laius, kõrgus, taust, värv)
    
    pilt.write_to_png('Valminud kunstiteosed/' +faili_nimi + '.png')