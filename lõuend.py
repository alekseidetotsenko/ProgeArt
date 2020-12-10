import mustrid, kunst, cairo
from inspect import getmembers, isfunction # nende abil saab kujunduste faili funktsioonidest listi teha

# loen kujunduste funktsioonid sisse
mustrite_list = []
for muster in getmembers(mustrid):
    if isfunction(muster):
        mustrite_list.append(muster)
        
def lõuend(c, mustri_nr, laius, kõrgus):
    cr.set_source_rgba(0, 0, 0, 0)
    cr.rectangle(0, 0, laius, kõrgus)
    cr.fill()
    
    mustrite_list[mustri_nr](c, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    
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