from mustrid import*
from kunst import *
from kribukrabu import*
import cairo
from inspect import getmembers, isfunction # nende abil saab kujunduste faili funktsioonidest listi teha
from os import listdir

def lõuend(cr, muster, laius, kõrgus, taust, värv):
    if taust == 1:
        cr.set_source_rgb(värv[0][0]/255.0, värv[0][1]/255.0, värv[0][2]/255.0)
        cr.paint()
    
    eval(muster)(cr, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    
def originaalne_nimi(failinimi, laiend):
    valmis_tööd = listdir("Valminud kunstiteosed")
    a = 0
    uus_nimi = failinimi + laiend
    while uus_nimi in valmis_tööd:
         uus_nimi = failinimi + '(' + str(a) + ')'+ laiend
         a += 1
    return uus_nimi
    
# funktsioonid svg ja png loomiseks
def svg_fail(muster, laius, kõrgus, faili_nimi, taust, värv):
    uus_nimi = originaalne_nimi(faili_nimi, '.svg')
    
    pilt = cairo.SVGSurface('Valminud kunstiteosed/' + uus_nimi, laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, muster, laius, kõrgus, taust, värv)#teeb pildi põhja ja kutsub välja vastava
    
    pilt.finish()
    
def png_fail(muster, laius, kõrgus, faili_nimi, taust, värv):
    uus_nimi = originaalne_nimi(faili_nimi, '.png')
    
    pilt = cairo.ImageSurface(cairo.FORMAT_ARGB32, laius, kõrgus)
    c = cairo.Context(pilt)
    lõuend(c, muster, laius, kõrgus, taust, värv)
    
    pilt.write_to_png('Valminud kunstiteosed/' + uus_nimi)