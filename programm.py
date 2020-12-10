from tkinter import *
from PIL import ImageTk,Image
from os import listdir, path
import cairo, math, random, copy # siia kõik, mida mustrite juures kasutatud on. vb oleks parem seda kuidagi teisiti teha
import lõuend as l# siin on programmi kunsti pool



# generate funktsioon tuleb siia.
def loo_muster():
    global kast_pildi_laius
    global kast_pildi_kõrgus
    global kast_faili_nimi
    global valitud_nimi
    kast_pildi_kõrgus = kast_pildi_kõrgus.get()
    print(kast_pildi_kõrgus)
    kast_pildi_laius = kast_pildi_laius.get()
    print(kast_pildi_laius)
    kast_faili_nimi = kast_faili_nimi.get()
    pilt = valitud_nimi
    print(valitud_nimi)
    print(valitud_tüüp.get())
    print(kast_faili_nimi)
    if valitud_tüüp.get() == 0:
        l.svg_fail(pilt, int(kast_pildi_laius), int(kast_pildi_kõrgus), kast_faili_nimi)
    else:
        l.png_fail(pilt, int(kast_pildi_laius), int(kast_pildi_kõrgus), kast_faili_nimi)



# edasi liikumise nupu funktsioon
def edasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
        
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv)
    pilt.grid(row = pildi_akna_rida, column = pildi_akna_veerg, columnspan = pildi_akna_ulatus)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bg = tausta_värv, fg = teksti_värv, bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = loenduri_rida, column = loenduri_veerg, columnspan = loenduri_ulatus, sticky = W + E)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">>", command = lambda: edasi( e(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_edasi.grid(row = edasi_nupu_rida, column = edasi_nupu_veerg, sticky = E)
    nupp_tagasi = Button(raam, text = "<<", command = lambda: tagasi(t(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_tagasi.grid(row = tagasi_nupu_rida, column = tagasi_nupu_veerg, sticky = W)

# tagasi liikumise nupu funktsioon
def tagasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
    
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv)
    pilt.grid(row = pildi_akna_rida, column = pildi_akna_veerg, columnspan = pildi_akna_ulatus)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bg = tausta_värv, fg = teksti_värv, bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = loenduri_rida, column = loenduri_veerg, columnspan = loenduri_ulatus, sticky = W + E)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">>", command = lambda: edasi( e(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_edasi.grid(row = edasi_nupu_rida, column = edasi_nupu_veerg, sticky = E)
    nupp_tagasi = Button(raam, text = "<<", command = lambda: tagasi(t(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_tagasi.grid(row = tagasi_nupu_rida, column = tagasi_nupu_veerg, sticky = W)
    
# menüü valiku funktsioon
def näidise_valik(*args):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
    global valitud_nimi
    valitud_nimi = valik.get()
    for i in range(len(valikud)):
        if valikud[i] == valitud_nimi:
            pildi_nr = i
            pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv)
            pilt.grid(row = pildi_akna_rida, column = pildi_akna_veerg, columnspan = pildi_akna_ulatus)
    
    # nuppude uuendus
    nupp_edasi = Button(raam, text = ">>", command = lambda: edasi( e(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_edasi.grid(row = edasi_nupu_rida, column = edasi_nupu_veerg, sticky = E)
    nupp_tagasi = Button(raam, text = "<<", command = lambda: tagasi(t(pildi_nr)), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
    nupp_tagasi.grid(row = tagasi_nupu_rida, column = tagasi_nupu_veerg, sticky = W)
    
    # näidiste loenduri uuendus
    pildi_loendur = Label(raam, text = str(pildi_nr + 1) + ' \\ ' + str(len(näidised)), bg = tausta_värv, fg = teksti_värv, bd = 1, relief = SUNKEN, anchor = E)
    pildi_loendur.grid(row = loenduri_rida, column = loenduri_veerg, columnspan = loenduri_ulatus, sticky = W + E)
    
    # dropdown menüü valiku uuendus
    valik.set(valikud[pildi_nr])
    
raam = Tk()
raam.title("ArtProjekt")
tausta_värv = '#404040'
raam.configure(bg = tausta_värv)
ikoon = PhotoImage(file = 'ikoon.png')
raam.iconphoto(False, ikoon)

# vidinate asukohad, värvid
teksti_värv = '#F0F0F0'
nupu_tausta_värv = '#606060'
nupu_taust_vajutades = '#C88C8C'
mustri_nupu_taust = '#30AA30'
mustri_nupp_vajutades = '#40BB40'
mustri_nupu_tekst = teksti_värv
pildi_akna_värv = '#000000'
kasti_tausta_värv = nupu_tausta_värv

nime_sildi_rida, nime_sildi_veerg = 0, 0
nime_kasti_rida, nime_kasti_veerg, nime_kasti_ulatus = 0, 1, 4

laiuse_sildi_rida, laiuse_sildi_veerg = 1, 0
laiuse_kasti_rida, laiuse_kasti_veerg = 1, 1

kõrguse_sildi_rida, kõrguse_sildi_veerg = 2, 0 
kõrguse_kasti_rida, kõrguse_kasti_veerg = 2, 1

tüübi_sildi_rida, tüübi_sildi_veerg = 3, 0
svg_nupu_rida, svg_nupu_veerg = 3, 1
png_nupu_rida, png_nupu_veerg = 3, 2

pildi_akna_rida, pildi_akna_veerg, pildi_akna_ulatus = 4, 0, 4

tagasi_nupu_rida, tagasi_nupu_veerg = 5, 0
edasi_nupu_rida, edasi_nupu_veerg = 5, 3
menüü_rida, menüü_veerg, menüü_ulatus = 5, 1, 2

mustri_nupu_rida, mustri_nupu_veerg, mustri_nupu_ulatus = 6, 0, 4

loenduri_rida, loenduri_veerg, loenduri_ulatus = 7, 0, 4

# loen näidised sisse
näidised = []

näidiste_kaust = 'näidised' # siit saab näidiste kausta nime vahetada
faili_aadress = path.realpath(__file__) # selle pythoni faili aadress
üldine_aadress = path.dirname(faili_aadress) # üldise kausta aadress
näidiste_aadress = üldine_aadress + '\\' + näidiste_kaust + '\\' # näidiste kausta aadress

näidiste_nimed = listdir(näidiste_aadress) # see loeb näidiste nimed sisse
for nimi in näidiste_nimed: # see avab näidised ja salvestab pildid ükshaaval järjendisse
    näidised.append(ImageTk.PhotoImage(Image.open(näidiste_aadress + nimi)))

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
pilt = Label(image = näidised[0], bg = pildi_akna_värv)
pilt.grid(row = pildi_akna_rida, column = pildi_akna_veerg, columnspan = pildi_akna_ulatus)

# näidiste loendur
pildi_loendur = Label(raam, text = '1 \\ ' + str(len(näidised)), bg = tausta_värv, fg = teksti_värv, bd = 1, relief = SUNKEN, anchor = E)
pildi_loendur.grid(row = loenduri_rida, column = loenduri_veerg, columnspan = loenduri_ulatus, sticky = W + E)
    
# dropdown menüü
valikud = []
for nimi in näidiste_nimed:
    valikud.append(nimi[:-4]) #võtab järelt ära faili laiendi. tulemus on näidise nimeks
valik = StringVar()
valik.set(valikud[0])

menüü = OptionMenu(raam, valik, *valikud)
menüü.config(bg = tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_tausta_värv, activeforeground = teksti_värv, highlightthickness = 0)
menüü.grid(row = menüü_rida, column = menüü_veerg, columnspan = menüü_ulatus, sticky = W + E)

# annab funktsioonile näidise_valik argumendi
valik.trace('w', näidise_valik)

# nupud ja lahtrid Aleksei koodist. Tegin ainult eestikeelseks ja panin asukoha parameetrid muutujatena.
# nupud
nupp_edasi = Button(raam, text = ">>", command = lambda: edasi(1), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
nupp_edasi.grid(row = edasi_nupu_rida, column = edasi_nupu_veerg, sticky = E)
nupp_tagasi = Button(raam, text = "<<", command = lambda: tagasi(piir), bg = nupu_tausta_värv, fg = teksti_värv, bd = 0, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
nupp_tagasi.grid(row = tagasi_nupu_rida, column = tagasi_nupu_veerg, sticky = W)
nupp_loo_muster = Button(raam, text='Loo muster', command = loo_muster, fg = mustri_nupu_tekst, bg = mustri_nupu_taust, bd = 0, activebackground = mustri_nupp_vajutades, activeforeground = mustri_nupu_tekst)
nupp_loo_muster.grid(row = mustri_nupu_rida, column = mustri_nupu_veerg, columnspan = mustri_nupu_ulatus, sticky = W + E)

# svg ja png valiku nupud. NEED ON VAJA VEEL KORDA TEHA
silt_faili_tüüp = Label(raam, text = 'Tüüp:', bg = tausta_värv, fg = teksti_värv)
silt_faili_tüüp.grid(row = tüübi_sildi_rida, column = tüübi_sildi_veerg, sticky = W)

valitud_tüüp = IntVar()
nupp_png = Radiobutton(raam, text = '.png', value = 1, variable = valitud_tüüp, bg = tausta_värv, fg = teksti_värv) # siia on kuidagi vaja lisada see: lambda: png_fail(c, laius, kõrgus)
nupp_png.grid(row = png_nupu_rida, column = png_nupu_veerg)
nupp_svg = Radiobutton(raam, text = ".svg", value = 0, variable = valitud_tüüp, bg = tausta_värv, fg = teksti_värv) # ja siia see: lambda: svg_fail(c, laius, kõrgus)
nupp_svg.grid(row = svg_nupu_rida, column = svg_nupu_veerg)

# faili nime sisestamise osa
silt_faili_nimi = Label(raam, text = 'Nimi:', bg = tausta_värv, fg = teksti_värv)
silt_faili_nimi.grid(row = nime_sildi_rida, column = nime_sildi_veerg, sticky = W)
kast_faili_nimi = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv, bd = 0)
kast_faili_nimi.grid(row = nime_kasti_rida, column = nime_kasti_veerg, columnspan = nime_kasti_ulatus, sticky = W)

# laiuse ja kõrguse sisestamise osa
silt_pildi_laius = Label(raam, text = 'Laius:', bg = tausta_värv, fg = teksti_värv)
silt_pildi_laius.grid(row = laiuse_sildi_rida, column = laiuse_sildi_veerg, sticky = W)
kast_pildi_laius = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv, bd = 0)
kast_pildi_laius.grid(row = laiuse_kasti_rida, column = laiuse_kasti_veerg, sticky = W)

silt_pildi_kõrgus = Label(raam, text = 'Kõrgus:', bg = tausta_värv, fg = teksti_värv)
silt_pildi_kõrgus.grid(row = kõrguse_sildi_rida, column = kõrguse_sildi_veerg, sticky = W)
kast_pildi_kõrgus = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv, bd = 0)
kast_pildi_kõrgus.grid(row = kõrguse_kasti_rida, column = kõrguse_kasti_veerg, sticky = W)


raam.mainloop()