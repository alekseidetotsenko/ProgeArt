from mustrid import*
from kunst import *
import cairo
from inspect import getmembers, isfunction # nende abil saab kujunduste faili funktsioonidest listi teha

def lõuend(cr, mustri_nr, laius, kõrgus):
    cr.set_source_rgba(0, 0, 0, 0)
    cr.rectangle(0, 0, laius, kõrgus)
    cr.fill()
    
    eval(mustri_nr)(cr, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    
# funktsioonid svg ja png loomiseks
def svg_fail(mustri_nr, laius, kõrgus, faili_nimi):
    pilt = cairo.SVGSurface(faili_nimi + '.svg', laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, mustri_nr, laius, kõrgus)#teeb pildi põhja ja kutsub välja vastava
    
    pilt.finish()
    
def png_fail(mustri_nr, laius, kõrgus, faili_nimi):
    pilt = cairo.ImageSurface(cairo.FORMAT_ARGB32, laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, mustri_nr, laius, kõrgus)
    
    pilt.write_to_png(faili_nimi + '.png')