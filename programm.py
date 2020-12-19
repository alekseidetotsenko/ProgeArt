from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk,Image
from os import listdir, path
import cairo, math, random, copy # siia kõik, mida mustrite juures kasutatud on. vb oleks parem seda kuidagi teisiti teha
import lõuend as l# siin on programmi kunsti pool



# nupu "loo disain" vajutamisel
def loo_muster():
    kõrgus = kast_pildi_kõrgus.get()
    laius = kast_pildi_laius.get()
    failinimi = kast_faili_nimi.get()
    kunstityyp = valitud_nimi
    taust = valik_taust.get()
    
    if valitud_tüüp.get() == 1:
        l.svg_fail(kunstityyp, int(laius), int(kõrgus), failinimi, taust, värv)
    else:
        l.png_fail(kunstityyp, int(laius), int(kõrgus), failinimi, taust, värv)



# funktsioonid edasi ja tagasi nupu jaoks
def edasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
        
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv, bd = 0)
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

def tagasi(pildi_nr):
    global pilt
    global nupp_edasi
    global nupp_tagasi
    global valik
    
    # eelmine näidis eest ära ja uus asemele
    pilt.grid_forget()
    pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv, bd = 0)
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
    

# valikmenüü funktsioon
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
            pilt = Label(image = näidised[pildi_nr], bg = pildi_akna_värv, bd = 0)
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

#Tausta värvi valimine ja värvi näitav nupp
def vali_värv():
    global värv
    
    if valik_taust.get() == 1:
        värv = askcolor(title = "Tausta värv")
        nupp_vali_värv = Button(raam, text= "      ", command = vali_värv, bg = värv[1], fg = teksti_värv, bd = 1, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv, highlightthickness = 0)
        nupp_vali_värv.grid(row=2, column=3, sticky= W)

# raam
raam = Tk()
raam.title("ArtProjekt")
tausta_värv = '#404040'
raam.configure(bg = tausta_värv)
ikoon = PhotoImage(file = 'ikoon.png')
raam.iconphoto(False, ikoon)


# vidinate asukohad, värvid
teksti_värv = '#FFFFFF'
nupu_tausta_värv = '#404040'
nupu_taust_vajutades = '#606060'
mustri_nupu_taust = '#20B2AA'
mustri_nupp_vajutades = '#20B2AA'
mustri_nupu_tekst = teksti_värv
pildi_akna_värv = tausta_värv
kasti_tausta_värv = nupu_taust_vajutades

nime_sildi_rida, nime_sildi_veerg = 0, 0
nime_kasti_rida, nime_kasti_veerg, nime_kasti_ulatus = 0, 1, 1
mustri_nupu_rida, mustri_nupu_veerg, mustri_nupu_ulatus = 0, 2, 2

laiuse_sildi_rida, laiuse_sildi_veerg = 1, 0
laiuse_kasti_rida, laiuse_kasti_veerg = 1, 1

kõrguse_sildi_rida, kõrguse_sildi_veerg = 2, 0 
kõrguse_kasti_rida, kõrguse_kasti_veerg = 2, 1

tüübi_sildi_rida, tüübi_sildi_veerg = 3, 0
svg_nupu_rida, svg_nupu_veerg = 3, 1
png_nupu_rida, png_nupu_veerg = 3, 2

tagasi_nupu_rida, tagasi_nupu_veerg = 4, 0
edasi_nupu_rida, edasi_nupu_veerg = 4, 3
menüü_rida, menüü_veerg, menüü_ulatus = 4, 1, 2

pildi_akna_rida, pildi_akna_veerg, pildi_akna_ulatus = 5, 0, 4

loenduri_rida, loenduri_veerg, loenduri_ulatus = 6, 0, 4


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
pilt = Label(image = näidised[0], bg = pildi_akna_värv, bd = 0)
pilt.grid(row = pildi_akna_rida, column = pildi_akna_veerg, columnspan = pildi_akna_ulatus)

# näidiste loendur
pildi_loendur = Label(raam, text = '1 \\ ' + str(len(näidised)), bg = tausta_värv, fg = teksti_värv, bd = 1, relief = SUNKEN, anchor = E)
pildi_loendur.grid(row = loenduri_rida, column = loenduri_veerg, columnspan = loenduri_ulatus, sticky = W + E)
    
# dropdown menüü
valikud = []
for nimi in näidiste_nimed:
    valikud.append(nimi[:-4]) #võtab järelt ära faili laiendi. tulemus on näidise nimeks
valitud_nimi = valikud[0]
valik = StringVar()
valik.set(valitud_nimi)

menüü = OptionMenu(raam, valik, *valikud)
menüü.config(bg = tausta_värv, fg = teksti_värv, bd = 1, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv, highlightthickness = 0)
menüü.grid(row = menüü_rida, column = menüü_veerg, columnspan = menüü_ulatus)

# annab funktsioonile näidise_valik argumendi
valik.trace('w', näidise_valik)

# nupud ja lahtrid Aleksei koodist. Tegin ainult eestikeelseks ja panin asukoha parameetrid muutujatena.
# nupud
nupp_edasi = Button(raam, text = ">>", command = lambda: edasi(1), bg = nupu_tausta_värv, fg = teksti_värv, bd = 1, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
nupp_edasi.grid(row = edasi_nupu_rida, column = edasi_nupu_veerg, sticky = E)
nupp_tagasi = Button(raam, text = "<<", command = lambda: tagasi(piir), bg = nupu_tausta_värv, fg = teksti_värv, bd = 1, activebackground = nupu_taust_vajutades, activeforeground = teksti_värv)
nupp_tagasi.grid(row = tagasi_nupu_rida, column = tagasi_nupu_veerg, sticky = W)

värv = ('kohahoidja', tausta_värv)
#tausta värvi valiku nupp
valik_taust = IntVar()
kas_taust = Checkbutton(raam, text='Taust: ', variable = valik_taust, command = vali_värv, selectcolor = tausta_värv, highlightbackground = tausta_värv, activebackground = tausta_värv, activeforeground = teksti_värv, fg = teksti_värv, bg = tausta_värv)
kas_taust.grid(row = 2, column = 2, sticky = E)


nupp_loo_muster = Button(raam, text='Loo disain', font = 'Helvetica 10 bold', command = loo_muster, fg = mustri_nupu_tekst, bg = mustri_nupu_taust, pady = 5, bd = 1, activebackground = mustri_nupp_vajutades, activeforeground = mustri_nupu_tekst)
nupp_loo_muster.grid(row = mustri_nupu_rida, rowspan = 1, column = mustri_nupu_veerg, columnspan = mustri_nupu_ulatus, sticky = W + E + N + S)

# svg ja png valiku nupud
silt_faili_tüüp = Label(raam, text = 'Fail:', bg = tausta_värv, fg = teksti_värv)
silt_faili_tüüp.grid(row = tüübi_sildi_rida, column = tüübi_sildi_veerg, sticky = W)

valitud_tüüp = IntVar()
nupp_png = Radiobutton(raam, text = '.png', value = 0, variable = valitud_tüüp, selectcolor = tausta_värv, highlightbackground = tausta_värv, activebackground = tausta_värv, activeforeground = teksti_värv, fg = teksti_värv, bg = tausta_värv)
nupp_png.grid(row = png_nupu_rida, column = png_nupu_veerg)
nupp_svg = Radiobutton(raam, text = ".svg", value = 1, variable = valitud_tüüp, selectcolor = tausta_värv, highlightbackground = tausta_värv, activebackground = tausta_värv, activeforeground = teksti_värv, fg = teksti_värv, bg = tausta_värv)
nupp_svg.grid(row = svg_nupu_rida, column = svg_nupu_veerg)

# faili nime sisestamise osa
silt_faili_nimi = Label(raam, text = 'Nimi:', bg = tausta_värv, fg = teksti_värv)
silt_faili_nimi.grid(row = nime_sildi_rida, column = nime_sildi_veerg, sticky = W)
kast_faili_nimi = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv)
kast_faili_nimi.grid(row = nime_kasti_rida, column = nime_kasti_veerg, columnspan = nime_kasti_ulatus, sticky = W)
kast_faili_nimi.insert(0,'minu_fail')

# laiuse ja kõrguse sisestamise osa
silt_pildi_laius = Label(raam, text = 'Laius:', bg = tausta_värv, fg = teksti_värv)
silt_pildi_laius.grid(row = laiuse_sildi_rida, column = laiuse_sildi_veerg, sticky = W)
kast_pildi_laius = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv)
kast_pildi_laius.grid(row = laiuse_kasti_rida, column = laiuse_kasti_veerg, sticky = W)
kast_pildi_laius.insert(0,'1920')

silt_pildi_kõrgus = Label(raam, text = 'Kõrgus:', bg = tausta_värv, fg = teksti_värv)
silt_pildi_kõrgus.grid(row = kõrguse_sildi_rida, column = kõrguse_sildi_veerg, sticky = W)
kast_pildi_kõrgus = Entry(raam, bg = kasti_tausta_värv, fg = teksti_värv)
kast_pildi_kõrgus.grid(row = kõrguse_kasti_rida, column = kõrguse_kasti_veerg, sticky = W)
kast_pildi_kõrgus.insert(0,'1080')

raam.mainloop()