# Uuendatud 06.12.
# Lisasin funktsioonide valimiseks vajalikud osad.
# Aga praegu on probleemiks kuidas funktsioonid ja näidised kokku viia.
# Puudu on ka generate nupp ja svg ja png nupud, nii et kogu see funktsioonide sisse lugemine ei paista kuskilt välja.

from tkinter import *
from PIL import ImageTk,Image
from os import listdir, path
import cairo, math, random, copy # siia kõik, mida mustrite juures kasutatud on. vb oleks parem seda kuidagi teisiti teha
import mustrid # siia mustrite fail, kus kõik on koos. iga muster on eraldi funktsioonina ja ilma raamita
from inspect import getmembers, isfunction # nende abil saab kujunduste faili funktsioonidest listi teha

raam = Tk()
raam.title("ArtProjekt")
# ikoon = PhotoImage(file = r'C:\Users\Laptop\Desktop\Programmeerimine I\ArtProjekt\New folder\kausutajaliides katse\uus_ikoon.png')
# raam.iconphoto(False, ikoon)
nuppude_raam_1 = Frame(raam) # neid oleks kõigi nuppude paigutamiseks vaja
nuppude_raam_1.grid(row = 2, column = 1, columnspan = 3, sticky = W)

# loen näidised sisse
näidised = []

näidiste_kaust = 'näidised' # siit saab näidiste kausta nime vahetada
faili_aadress = path.realpath(__file__) # selle pythoni faili aadress
üldine_aadress = path.dirname(faili_aadress) # üldise kausta aadress
näidiste_aadress = üldine_aadress + '\\' + näidiste_kaust + '\\' # näidiste kausta aadress

näidiste_nimed = listdir(näidiste_aadress) # see loeb näidiste nimed sisse
for nimi in näidiste_nimed: # see avab näidised ja salvestab pildid ükshaaval järjendisse
    näidised.append(ImageTk.PhotoImage(Image.open(näidiste_aadress + nimi)))

# loen kujunduste funktsioonid sisse
mustrite_list = []
for muster in getmembers(mustrid):
    if isfunction(muster):
        mustrite_list.append(muster)

# funktsioonid svg ja png loomiseks
def svg_fail(mustri_nr, laius, kõrgus, faili_nimi):
    pilt = cairo.SVGSurface(faili_nimi + '.svg', laius, kõrgus)
    c = cairo.Context(pilt)    
    mustrite_list[mustri_nr](c, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    pilt.finish()
def png_fail(mustri_nr, laius, kõrgus, faili_nimi):
    pilt = cairo.ImageSurface(cairo.FORMAT_ARGB32, laius, kõrgus)
    c = cairo.Context(pilt)
    mustrite_list[mustri_nr](c, laius, kõrgus) # valib funktsiooni ja annab sellele vajalikud argumendid
    pilt.write_to_png(faili_nimi + '.png')

# funktsioonid näidiste vahetamiseks, et ei oleks 'out of range' vea ohtu
piir = len(näidised) - 1
def e(arv, alumine = 0, ülemine = piir): # edasi liikumiseks
    if arv == ülemine:
        return alumine
    else:
        return arv + 1
def t(arv, alumine = 0, ülemine = piir): # tagasi liikumiseks
    if arv == alumine:
        return ülemine
    else:
        return arv - 1

# näidise kuvamine
pilt = Label(image = näidised[0])
pilt.grid(row = 0, column = 1)

# näidiste loendur
pildi_loendur = Label(raam, text = '1 \\ ' + str(len(näidised)), bd = 1, relief = SUNKEN, anchor = E)
pildi_loendur.grid(row = 3, column = 0, columnspan = 3, sticky = W + E)

# edasi liikumise nupu funktsioon
def edasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
        
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr])
    pilt.grid(row = 0, column = 1)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = 3, column = 0, columnspan = 3, sticky = W + E)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">", command = lambda: edasi(e(pildi_nr)))
    nupp_edasi.grid(row = 0, column = 2)
    nupp_tagasi = Button(raam, text = "<", command = lambda: tagasi(t(pildi_nr)))
    nupp_tagasi.grid(row = 0, column = 0)

# tagasi liikumise nupu funktsioon
def tagasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
    
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr])
    pilt.grid(row = 0, column = 1)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = 3, column = 0, columnspan = 3, sticky = W + E)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">", command = lambda: edasi(e(pildi_nr)))
    nupp_edasi.grid(row = 0, column = 2)
    nupp_tagasi = Button(raam, text = "<", command = lambda: tagasi(t(pildi_nr)))
    nupp_tagasi.grid(row = 0, column = 0)
    
# dropdown menüü
valikud = []
for nimi in näidiste_nimed:
    valikud.append(nimi[:-4]) #võtab järelt ära faili laiendi. tulemus on näidise nimeks
valik = StringVar()
valik.set(valikud[0])

menüü = OptionMenu(raam, valik, *valikud)
menüü.pack(in_ = nuppude_raam_1, side = LEFT)

# menüü valiku funktsioon
def näidise_valik(*args):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
    
    valitud_nimi = valik.get()
    for i in range(len(valikud)):
        if valikud[i] == valitud_nimi:
            pildi_nr = i
            pilt = Label(image = näidised[pildi_nr])
            pilt.grid(row = 0, column = 1)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">", command = lambda: edasi(e(pildi_nr)))
    nupp_edasi.grid(row = 0, column = 2)
    nupp_tagasi = Button(raam, text = "<", command = lambda: tagasi(t(pildi_nr)))
    nupp_tagasi.grid(row = 0, column = 0)
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = 3, column = 0, columnspan = 3, sticky = W + E)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])

# annab funktsioonile näidise_valik argumendi
valik.trace('w', näidise_valik)

# nupud
nupp_edasi = Button(raam, text = ">", command = lambda: edasi(1))
nupp_edasi.grid(row = 0, column = 2)
nupp_tagasi = Button(raam, text = "<", command = lambda: tagasi(piir))
nupp_tagasi.grid(row = 0, column = 0)

raam.mainloop()