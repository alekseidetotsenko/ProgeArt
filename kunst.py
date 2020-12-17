from opensimplex import OpenSimplex #arvutab müra väärtus vastavatele x, y väärtustele

import cairo, random, math, copy

#Karolini mustrid
def viga(cr, laius, kõrgus):
    for siine in range(random.randint(0, 50)):
        cr.set_source_rgb(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
        cr.set_line_width(random.randint(1, 5))
        x, y = random.randint(0, laius), random.randint(0,kõrgus)
        cr.arc(x, y, random.randint(3,6), 0, 2 * math.pi)
        cr.fill()
        for pöördeid in range(random.randint(2, 12)):
            suund = random.randint(0,1)
            if suund==1:
                x = random.randint(0, laius)
            else:
                y = random.randint(0, kõrgus)
            cr.line_to(x, y)
        cr.arc(x, y, random.randint(3,6), 0, 2 * math.pi)

def siinid(cr, laius, kõrgus):    
    
    for väikseid_siine in range(random.randint(5, 10)):
        cr.set_source_rgb(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        cr.set_line_width(2)
        x, y = random.randint(0, laius), random.randint(0,kõrgus)
        for pöördeid in range(random.randint(30, 60)):
            suund = random.randint(0,3)
            if suund==1:
                x = x + random.randint(0, int(laius/20))
            elif suund==2:
                x = x - random.randint(0, int(laius/20))
            elif suund==3:
                y = y - random.randint(0, int(kõrgus/20))
            else:
                y = y + random.randint(0, int(kõrgus/20))
            cr.line_to(x, y)
        cr.stroke()
    
    minR = int(2*max(kõrgus, laius)/594)
    maxR = int(5*max(kõrgus, laius)/594)
    joone_laius = int(3*max(laius, kõrgus)/594)
    for siine in range(random.randint(10, 30)):
        cr.set_source_rgb(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        cr.set_line_width(random.randint(1, joone_laius))
        x, y = random.randint(0, laius), random.randint(0,kõrgus)
        
        cr.arc(x, y, random.randint(minR,maxR), 0, 2 * math.pi)
        cr.fill()
        for pöördeid in range(random.randint(2, 12)):
            suund = random.randint(0,1)
            if suund==1:
                x = random.randint(0, laius)
            else:
                y = random.randint(0, kõrgus)
            cr.line_to(x, y)
        cr.stroke()
        cr.arc(x, y, random.randint(minR,maxR), 0, 2 * math.pi)
        cr.fill()
        
def kõverik(cr, laius, kõrgus):
    #arvutab joone lauise vastavalt pildi mõõtmetele
    joone_laius = 2*max(laius, kõrgus)/594
    os = OpenSimplex(random.randint(0, 2**20))
    cr.set_line_width(joone_laius)
    cr.set_source_rgb(0, 0, 0)
    #viib null punkti keskele
    cr.translate(laius/2, kõrgus/2)
    #arvutab kui lähedal müravärja vaadeldakse 
    z1 = math.pi/180
    z = 0.5
    j = math.pi/90
    #arvutab raadiuse vastavalt pildi mõõtmetele
    suhe = min(laius, kõrgus)/4
    a=0
    while a < 2*math.pi:
        xoff = math.cos(a)
        yoff = math.sin(a)
        m = 0.75 + os.noise2d(xoff, yoff) + os.noise2d(xoff*z, yoff*z)/2
        r = suhe*m
        x = r*math.cos(j)
        y = r*math.sin(j)
        cr.line_to(x,y)
        #keerab pilti j kraadi
        cr.rotate(j)
        a+=j
        
    cr.stroke()
    
def joonestik(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = .002
    zoom1 = .006
    zoom2 = .009
    joone_laius = 2*max(laius, kõrgus)/594
    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(joone_laius)
    for i in range(round(kõrgus/15), kõrgus, round(kõrgus/15)):
        müra = (os.noise2d(0*zoom,i*zoom)*2+os.noise2d(0*zoom1,i*zoom1)/2+os.noise2d(0*zoom2,i*zoom2)/4)*100
        cr.move_to(0, i + müra)
        #liigub üle pildi ja teeb joone 
        for j in range(0, laius, round(laius/80)):
            müra = (os.noise2d(j*zoom,i*zoom)*2+os.noise2d(j*zoom1,i*zoom1)/2+os.noise2d(j*zoom2,i*zoom2)/4)*100
            cr.line_to(j, i+müra)
        müra = (os.noise2d(laius*zoom,i*zoom)*2+os.noise2d(laius*zoom1,i*zoom1)/2+os.noise2d(laius*zoom2,i*zoom2)/4)*100
        cr.line_to(laius, i+müra)
        cr.stroke()
        
def mäed(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = .002
    zoom1 = .004
    zoom2 = .01
    #valib milliine värv on paigal     
    paigal = random.randint(0, 2)
    
    rgb = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    
    for i in range(0, kõrgus, round(kõrgus/15)):
        os = OpenSimplex(random.randint(0, 2**20))
        if paigal == 0:#valib värvi kombinatsioonid et tekiks 
            r = rgb[0]
            g = 1-(rgb[1]*i)/kõrgus
            b = 1-(rgb[2]*i)/kõrgus
        elif paigal == 1:
            r = 1-(rgb[0]*i)/kõrgus
            g = rgb[1]
            b = 1-(rgb[2]*i)/kõrgus
        else:
            r = 1-(rgb[0]*i)/kõrgus
            g = 1-(rgb[1]*i)/kõrgus
            b = rgb[2]
        #cr.set_source_rgba(0.7, 1-(0.4*i)/kõrgus, 1-(0.9*i)/kõrgus, 1)
        cr.set_source_rgb(r, g, b)
        cr.line_to(0, i)
        for j in range(0, laius, round(laius/80)):
            müra = (os.noise2d(j*zoom,i*zoom)*2+os.noise2d(j*zoom1,i*zoom1)/2+os.noise2d(j*zoom2,i*zoom2)/4)*100
            cr.line_to(j, i+müra)
        #teeb kasti ja värvib selle
        cr.line_to(laius, i+müra)
        cr.line_to(laius, kõrgus)
        cr.line_to(0, kõrgus)
        cr.fill()
#kasutusel järgnevas funktsioonis
def punkt_ringis(cr, os, a, i):
    #joonistab joone uue x,y väärtuseni
    z2 = 1
    z = .05
    j = 0.1
    xoff = math.cos(a)+1
    yoff = math.sin(a)+1
    m = 1+os.noise2d(xoff*z, yoff*z)+os.noise2d(xoff*z2, yoff*z2)/4
    r = i*m
    x = r*math.cos(j)
    y = r*math.sin(j)
    cr.line_to(x,y)
    
def kõver_sibul(cr, laius, kõrgus):
    
    os = OpenSimplex(random.randint(0, 2**20))
    joone_laius = 2*max(laius, kõrgus)/594
    cr.set_line_width(joone_laius)
    cr.set_source_rgb(.4, .4, .4)
    cr.translate(laius/2, kõrgus/2)
    j = 0.1
    #mitu lopergust ringi üksteise sees
    for i in range(8):
        r = i * min(laius, kõrgus)/20
        a=0
        #loob loperguse ringi
        while a <= 2*math.pi:
            punkt_ringis(cr, os, a, r)
            cr.rotate(j)
            a+=j
        #lõpetab ringi ilusti
        cr.rotate(2*math.pi-a)
        punkt_ringis(cr, os, 0, r)
        cr.stroke()

def pusa(cr, laius, kõrgus):
    
    os = OpenSimplex(random.randint(0, 2**20))
    joone_laius = 2*max(laius, kõrgus)/594
    cr.set_line_width(joone_laius)
    cr.set_source_rgb(0, 0, 0)
    cr.translate(laius/2, kõrgus/2)
    z1 = math.pi/180
    z = 0.5
    j = math.pi/90
    suhe = min(laius, kõrgus)/5
    a=0
    while a < 2*math.pi:
        xoff = math.cos(a)
        yoff = math.sin(a)
        m = 1 + os.noise2d(xoff, yoff) + os.noise2d(xoff*z, yoff*z)/2
        r = suhe*m
        x = r*math.cos(j)
        y = r*math.sin(j)
        cr.line_to(x,y)
        cr.rotate(a)
        a+=j
        
    cr.stroke()
#värvib piksli kaardi funktsioonis    
def värvi(cr, x, y):
    cr.set_source_rgba(0, 0, 0, 0.5)
    cr.rectangle(x, y, 1, 1)
    cr.fill()

def kaart(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = .005    
    
    for i in range(laius):
        for j in range(kõrgus):
            müra = (1.0+os.noise2d(x=i*zoom, y=j*zoom))/2.0
            #asvutab soovitud vahemikud
            for x in range(1, 20):
                #kontrollib kas müra antud väärtus on voovitud vahemikes

                if müra<0.30 and x/20<müra<(x/20)+0.01:
                    värvi(cr, i, j)
                elif müra>0.70 and 1-(x/20)<müra<(1-(x/20))+0.01:
                    värvi(cr, i, j)
                elif 0.30<müra<0.70 and x/10<müra<(x/10)+0.02:
                    värvi(cr, i, j)

def udu(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**10))
    zoom = .002
    zoom1 = .004
    zoom2 = .01
    
    rgb = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    paigal = random.randint(0, 3)
    for i in range(round(kõrgus/15), kõrgus, round(kõrgus/15)):
        if paigal == 0:
            r = rgb[0]
            g = (rgb[1]*i)/kõrgus
            b = (rgb[2]*i)/kõrgus
        elif paigal == 1:
            r = (rgb[0]*i)/kõrgus
            g = rgb[1]
            b = (rgb[2]*i)/kõrgus
        else:
            r = (rgb[0]*i)/kõrgus
            g = (rgb[1]*i)/kõrgus
            b = rgb[2]
            
        
        #cr.set_source_rgba(0.5, (0.5*i)/kõrgus, (1*i)/kõrgus, (1*i)/kõrgus)
        cr.set_source_rgba(r, g, b, (1*i)/kõrgus)
        cr.line_to(0, i)
        for j in range(0, laius, round(laius/80)):
            müra = (os.noise2d(j*zoom,i*zoom)*2+os.noise2d(j*zoom1,i*zoom1)/2+os.noise2d(j*zoom2,i*zoom2)/4)*100
            cr.line_to(j, i+müra)
        cr.line_to(laius, i+müra)
        cr.line_to(laius, kõrgus)
        cr.line_to(0, kõrgus)
        cr.fill()
        
def sebra(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = min(laius, kõrgus)**-0.75
    
    for i in range(laius):
        for j in range(kõrgus):
            müra = (1.0+(os.noise2d(x=i*zoom, y=j*zoom)))/2.0
            if not(0.4<müra<0.6):
                cr.set_source_rgb(.9, .9, .9)
                cr.rectangle(i, j, 1, 1)
                cr.fill()
#joonistab ringi mullid funktsioonis            
def kera(cr, x, y, raadius):
    cr.set_source_rgba(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), 0.05)
    cr.arc(x, y, raadius, 0, 2 * math.pi)
    cr.fill()
        
def mullid(cr, laius, kõrgus):
    cr.set_line_width(1)

    for i in range(0,random.randint(20, 500)):
        kera(cr, random.randint(0, laius), random.randint(0, kõrgus), random.randint(0, min(laius,kõrgus)/2))

def õli(cr, laius, kõrgus):
    cr.set_line_width(1)

    mullid(cr, laius, kõrgus)
    
    #värv = (random.uniform(0, .3), random.uniform(0, .4), random.uniform(0, 1))
    värv = (random.randint(0, 80), random.randint(0, 58), random.randint(0, 255))
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = random.uniform(.03, .05)
    for i in range(laius):
        for j in range(kõrgus):
            müra = (1.0+(os.noise2d(x=i*zoom, y=j*zoom)))/2.0
            if müra<0.2 or 0.7<müra:
                cr.set_source_rgba(värv[0], värv[1], värv[2], 0.5)
                cr.rectangle(i, j, 1, 1)
                cr.fill()
        
def sibulad(c, laius, kõrgus):
    joone_laius = 2*max(laius, kõrgus)/594
    c.set_line_width(joone_laius)
    for i in range(0, random.randint(10,20)):
        x = random.randint(0, laius)
        y = random.randint(0, kõrgus)
        raadius = random.randint(3, round(min(laius,kõrgus)/4))
        for i in range(0,raadius,7):
            for i in range(0,raadius,7):
                c.set_source_rgba(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), 0.1)
                c.arc(x, y, raadius - i, 0, 2 * math.pi)
                c.stroke()

###########################################################################################################################
# Indreku mustrid algavad siit

def siksakiline(c, laius, kõrgus):
    # abifunktsioonid
    def hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius): # loob hulknurga punktid
        θ = (2*math.pi)/nurgad
        x = keskpunkt_x
        y = keskpunkt_y
        kujund = []
        for i in range(nurgad+1):
            nurga_x = x + raadius*math.cos(i*θ)
            nurga_y = y + raadius*math.sin(i*θ)
            kujund.append((nurga_x, nurga_y))
        return kujund

    def deform(kujund, muut): # lisab iga punkti vahele juhuslikult uue punkti
        for i in range(len(kujund)-1, 0, -2):
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        return kujund

    # põhifunktsioon
    for i in range(int((laius*0.126)//(laius*0.01))):
        kujund = hulknurk(random.randint(5, 12), random.randint(laius//10, 8*(laius//10)), random.randint(kõrgus//10, 8*(kõrgus//10)), kõrgus//random.randint(2, 5))
        
        for i in range(8):
            kujund = deform(kujund, laius // 60)
        
        c.move_to(kujund[0][0], kujund[0][1])
        for e in range(len(kujund)):
            c.line_to(kujund[e][0], kujund[e][1])
        fikseeritud_värv = random.uniform(0.5, 0.8)
        c.set_source_rgba(fikseeritud_värv, fikseeritud_värv, fikseeritud_värv, random.uniform(0.1, 0.5))
        c.fill()
    

def tupsud(c, laius, kõrgus):
    # abifunktsioonid
    def hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius): # moodustab hulknurga
        θ = (2*math.pi)/nurgad
        x = keskpunkt_x
        y = keskpunkt_y
        kujund = []
        for i in range(nurgad+1):
            nurga_x = x + raadius*math.cos(i*θ)
            nurga_y = y + raadius*math.sin(i*θ)
            kujund.append((nurga_x, nurga_y))
        return kujund

    def deform(kujund, muut): # deformeerib hulknurka, lisades iga nurga vahele uue nurga suvaliselt
        for i in range(len(kujund)-1, 0, -2): # deformeeritakse küljed esimesest viimase nurgani.
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        # viimase ja esimese nurga vahelise külje deformeerimine
        keskpunkti_x = (kujund[0][0] + kujund[len(kujund)-1][0])/2
        keskpunkti_y = (kujund[0][1] + kujund[len(kujund)-1][1])/2
        juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
        kujund.insert(0, juhu_punkt)
        
        return kujund

    def tups(kontekst, kujund, baas_muut, baas_deform, udu_muut, udu_deform, kihtide_arv, R, G, B):
        # see funktsioon on kirjutatud kunstniku Tyler Hobbs juhiste järgi, mida on võimalik leida aadressilt: https://tylerxhobbs.com/essays/2017/a-generative-approach-to-simulating-watercolor-paints
        # saadud tulemust ei tasu Hobbsi versiooniga võrrelda. Arenemisruumi on veel palju. ;)
        for a in range(baas_deform): # aluseks võetakse deformeeritud hulknurk
            baas = deform(kujund, baas_muut)
        for b in range(kihtide_arv): # seda hulknurka deformeeritakse veel mitu korda ja tehakse läbipaistvad kihid üksteise peale
            udu = copy.deepcopy(baas)
            for d in range(udu_deform):
                udu = deform(udu, udu_muut)
            kontekst.move_to(udu[0][0], udu[0][1])
            for e in range(len(udu)):
                kontekst.line_to(udu[e][0], udu[e][1])
            kontekst.line_to(udu[0][0], udu[0][1])
            kontekst.set_source_rgba(R, G, B, 0.04)
            kontekst.fill()
    
    # põhifunktsioon    
    if laius < kõrgus: # pildi proportsioonid sõltuvad valitud laiusest ja kõrgusest
        jagatav = kõrgus
    else:
        jagatav = laius
    
    for i in range(10): # loob kümme tupsu. suurus sõltub pildi mõõtmete valikust
        kujund = hulknurk(10, random.randint(0, laius), random.randint(0, kõrgus), random.randint(jagatav//8, jagatav//4))
        tups(c, kujund, baas_muut = jagatav//50, baas_deform = 7, udu_muut = jagatav//80, udu_deform = 5, kihtide_arv = 30, R = 1, G = random.uniform(0,0.7), B = 0)

def üksik_tups(c, laius, kõrgus):
    # abifunktsioonid
    def hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius):
        θ = (2*math.pi)/nurgad
        x = keskpunkt_x
        y = keskpunkt_y
        kujund = []
        for i in range(nurgad+1):
            nurga_x = x + raadius*math.cos(i*θ)
            nurga_y = y + raadius*math.sin(i*θ)
            kujund.append((nurga_x, nurga_y))
        return kujund

    def deform(kujund, muut):
        for i in range(len(kujund)-1, 0, -2): # deformeeritakse iga külg - ettevaatust! väga koormav arvutile!
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        # viimase ja esimese nurga vahelise külje deformeerimine
        keskpunkti_x = (kujund[0][0] + kujund[len(kujund)-1][0])/2
        keskpunkti_y = (kujund[0][1] + kujund[len(kujund)-1][1])/2
        juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
        kujund.insert(0, juhu_punkt)
        
        return kujund

    def tups(kontekst, kujund, baas_muut, baas_deform, udu_muut, udu_deform, kihtide_arv, R, G, B):
        # see funktsioon on kirjutatud kunstniku Tyler Hobbs juhiste järgi, mida on võimalik leida aadressilt: https://tylerxhobbs.com/essays/2017/a-generative-approach-to-simulating-watercolor-paints
        # saadud tulemust ei tasu Hobbsi versiooniga võrrelda. Arenemisruumi on veel palju. ;)
        for a in range(baas_deform): # Aluseks võetakse deformeeritud hulknurk. See annab lõpptulemusele üldise kuju.
            baas = deform(kujund, baas_muut)
        for b in range(kihtide_arv): # Baas hulknurka deformeeritakse veel mitu korda ja tehakse läbipaistvad kihid üksteise peale
            udu = copy.deepcopy(baas) # Koopia on vajalik, kuna iga järgnev deformeerimine peab lähtuma samast baasist.
            for d in range(udu_deform):
                udu = deform(udu, udu_muut)
            kontekst.move_to(udu[0][0], udu[0][1]) # Saadud hulknurk joonistatakse üles.
            for e in range(len(udu)):
                kontekst.line_to(udu[e][0], udu[e][1])
            kontekst.line_to(udu[0][0], udu[0][1])
            kontekst.set_source_rgba(R, G, B, 0.06) # veidi vähem läbipaistvust kui mitme tupsuga mustril
            kontekst.fill()
    
    # põhifunktsioon
    if laius < kõrgus: # pildi proportsioonid sõltuvad valitud laiusest ja kõrgusest
        jagatav = laius
    else:
        jagatav = kõrgus
    # Argumendid on valitud selle järgi, et kujund valitud mõõtmetega pildile ära mahuks aga samas ka hea välja näeks.
    # See on saavutatud katse-eksituse meetodil.
    kujund = hulknurk(nurgad = 10, keskpunkt_x = laius//2, keskpunkt_y = kõrgus//2, raadius = 1)
    tups(c, kujund, baas_muut = jagatav//20, baas_deform = 2, udu_muut = jagatav//12, udu_deform = 7, kihtide_arv = 80, R = 1, G = 1, B = 1)


def võrknurkne(c, laius, kõrgus):
    # abifunktsioon
    def hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius):
        θ = (2*math.pi)/nurgad
        x = keskpunkt_x
        y = keskpunkt_y
        kujund = []
        for i in range(nurgad+1):
            nurga_x = x + raadius*math.cos(i*θ)
            nurga_y = y + raadius*math.sin(i*θ)
            kujund.append((nurga_x, nurga_y))
        return kujund
    # põhifunktsioon
    for i in range(int((laius*1.679)//(laius*0.0015))):
        keskpunkt_x, keskpunkt_y = random.randint(0, laius), random.randint(0, kõrgus)
        nurgad = random.randint(3, 12)
        raadius = random.randint(30, kõrgus//2)
        kujund = hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius)
        for j in range(len(kujund)-1, 0, -1):
            c.move_to(kujund[j][0], kujund[j][1])
            c.line_to(kujund[j-1][0], kujund[j-1][1])
            värv_hall = random.uniform(0, 1)
            c.set_source_rgb(värv_hall, värv_hall, värv_hall)
            joone_laius = (max(laius, kõrgus) * 0.03367) / 100 # et joone laius oleks proportsioonis valitud laiuse ja kõrgusega
            c.set_line_width(joone_laius)
        c.stroke()

def jooneline(c, laius, kõrgus):
    # põhifunktsioon
    for i in range(int(laius*3.367)//int(laius*0.0015)): # et joonte arv kasvaks sobivalt
        algus_x = random.randint(-(laius*0.25), laius + (laius*0.25)) # üle ääre
        algus_y = random.randint(-(kõrgus*0.25), kõrgus + (kõrgus*0.25))
        lõpp_x = random.randint(-(laius*0.25), laius + (laius*0.25))
        lõpp_y = random.randint(-(kõrgus*0.25), kõrgus + (kõrgus*0.25))
        joone_värv = random.uniform(0, 1)
        c.set_source_rgb(joone_värv, joone_värv, joone_värv)
        c.move_to(algus_x, algus_y)
        c.line_to(lõpp_x, lõpp_y)
        joone_laius = (max(laius, kõrgus) * 0.03367) / 100        
        c.set_line_width(joone_laius)
        c.stroke()        

def natuke_sassis(c, laius, kõrgus):
    # abifunktsioon
    def hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius):
        θ = (2*math.pi)/nurgad
        x = keskpunkt_x
        y = keskpunkt_y
        kujund = []
        for i in range(nurgad+1):
            nurga_x = x + raadius*math.cos(i*θ)
            nurga_y = y + raadius*math.sin(i*θ)
            kujund.append((nurga_x, nurga_y))
        return kujund
    
    # põhifunktsioon
    for i in range(2, 30):
        nurgad = random.randint(5,20)
        raadius = i**2
        kujund = hulknurk(nurgad, 0, 0, raadius//4)
        pööre = random.uniform(0, 4)
        c.save()
        c.translate(random.gauss(laius//2, 10), random.gauss(kõrgus//2, 10))
        c.rotate(math.pi*pööre)
        for j in range(len(kujund)-1, 0, -1):
            c.move_to(kujund[j][0], kujund[j][1])
            c.line_to(kujund[j-1][0], kujund[j-1][1])
        c.set_source_rgb(1, 1, 1)
        c.set_line_width(1)
        c.stroke()
        c.restore()

def paberlennukid(c, laius, kõrgus):
    # abifunktsioon
    def deform(kujund, muut):
        for i in range(len(kujund)-1, 0, -2):
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        return kujund
    
    # põhifunktsioon
    for i in range(kõrgus):
        # igas tsükli käigus tekib üks juhuslik nelinurk
        nurk_1 = (random.randint(0, laius), random.randint(0, kõrgus))
        nurk_2 = (random.randint(0, laius), random.randint(0, kõrgus))
        nurk_3 = (random.randint(0, laius), random.randint(0, kõrgus))
        nurk_4 = (random.randint(0, laius), random.randint(0, kõrgus))
        ristkülik = [nurk_1, nurk_2, nurk_3, nurk_4]
        # seejärel deformeeritakse külgi
        for j in range(5):
            kujund = deform(ristkülik, 5)
        c.move_to(kujund[0][0], kujund[0][1])
        for k in range(len(kujund)):
            c.line_to(kujund[k][0], kujund[k][1])
        
        # värvi valik
        värv = random.uniform(0.4, 1)
        c.set_source_rgba(värv, värv, 0.8, 1)
        c.fill() # üks kujund valmis

def võõp(c, laius, kõrgus):
    # põhifunktsioon
    tsükli_pikkus = laius*30//int(laius*0.002) # sobitab tsükli pikkuse pildi mõõtmetega, et tulemus näeks hea välja. katse-eksituse meetodil saadud
    for i in range(tsükli_pikkus): # pind kaetakse väga paljude juhuslikult paigutatud läbipaistvate ristkülikutega
        värv = random.uniform(0.5, 0.8) # et G ja B väärtused tuleksid samad - värv: rohekas sinine
        c.set_source_rgba(0.3, värv, värv, 0.05)
        x = random.randint(laius//kõrgus, laius - laius//45) # kõik väärtused sõltuvad laiusest ja kõrgusest
        y = random.randint(0, kõrgus - kõrgus//9)
        ristkülik_laius = random.randint(0, laius//40)
        ristkülik_kõrgus = random.randint(0, int(random.gauss(kõrgus//5, laius//50)))
        c.rectangle(x, y, ristkülik_laius, ristkülik_kõrgus)
        c.fill()

def ühe_kliki_rothko(c, laius, kõrgus):
    # abifunktsioon
    def deform(kujund, muut): # liigendab hulknurga kõik küljed, lisades iga kahe nurga vahele uue nurga
        # kuni eelviimase küljeni
        for i in range(len(kujund)-1, 0, -1):
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        # viimase külje liigendamine
        keskpunkti_x = (kujund[0][0] + kujund[len(kujund)-1][0])/2
        keskpunkti_y = (kujund[0][1] + kujund[len(kujund)-1][1])/2
        juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
        kujund.insert(0, juhu_punkt)
        return kujund

    # põhifunktsioon
    muut = laius//100 # kui suured sakid on ristkülikul
    udu = 8 # kui mitu korda deformeeritakse
    kihid = 80 # mitu deformeeritud kihti üksteise peale laotakse
    
    ühikud = 17 # mitmeks ühikuks pilti saab jaotada
    l = laius // ühikud # laiuse ühik
    k = kõrgus // ühikud # kõrguse ühik
    
    tsüklid = random.randint(1, 6)
    h = 0 # sellest tuleb ristküliku kõrgus
    n = 0 # salvestab kui kaugele tsüklis jõuti
    for i in range(tsüklid):
        n += 1
        α = random.randint(1, 2) # vasaku/ülemise ääre laius
        β = ühikud - α # parema/alumise ääre laius
        
        eelmise_lõpp = min(h + α*k, β*k) # esimese ristküliku puhul on eelmise lõpuks välimine ääris
        if eelmise_lõpp == β*k:
            break        
        
        # ristküliku loomine
        h = k + random.randint(eelmise_lõpp, β*k) # ristküliku kõrgus
        ristkülik = [(α*l, eelmise_lõpp), (β*l, eelmise_lõpp), (β*l, h), (α*l, h)]
        eelmise_lõpp = h + α*k
        
        # udutamine
        c.set_source_rgba(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 0.06)
        for j in range(kihid):
            rothko_ristkülik = copy.deepcopy(ristkülik)
            for d in range(udu):
                rothko_ristkülik = deform(rothko_ristkülik, muut)
            c.move_to(rothko_ristkülik[0][0], rothko_ristkülik[0][1])
            for e in range(len(rothko_ristkülik)):
                c.line_to(rothko_ristkülik[e][0], rothko_ristkülik[e][1])
            c.fill()
    
    # kui on ühe ristküliku jaoks veel ruumi, luuakse üks, mis ulatub lõpuni
    if n == tsüklid and eelmise_lõpp + 2*α*k < β*k:
        α = random.randint(1, 2)
        β = ühikud - α
        
        ristkülik = [(α*l, eelmise_lõpp), (β*l, eelmise_lõpp), (β*l, β*k), (α*l, β*k)]
        
        c.set_source_rgba(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 0.06)
        for j in range(kihid):
            rothko_ristkülik = copy.deepcopy(ristkülik)
            for d in range(udu):
                rothko_ristkülik = deform(rothko_ristkülik, muut)
            c.move_to(rothko_ristkülik[0][0], rothko_ristkülik[0][1])
            for e in range(len(rothko_ristkülik)):
                c.line_to(rothko_ristkülik[e][0], rothko_ristkülik[e][1])
            c.fill()


# # # # # # # # # # # # # # # # # # # # # # 
#Aleksei koodiosa algab siit!!!

#juhuslike värvide kogu
list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
(197, 239, 247), (190, 144, 212),(221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188),
 (41, 241, 195), (243, 156, 18), (189, 195, 199), (101, 198, 187), (255, 246, 143), (243, 241, 239)]


#mustrifuntksioonid
def tähed(ctx,WIDTH,HEIGHT):
    #skaleerimissuhe x ja y telje jaoks
    x_telje_suhe = WIDTH / (3*1980)
    y_telje_suhe = HEIGHT / (3*1020)
    #juhuslikud arvud muutujatele,hiljem tsükliarvudena kasutuses
    a = random.randint(100,3000)
    b = random.randint(10,50)
    for j in range(a):
        algus_x = random.randint(int(-2000 * x_telje_suhe), int(7000 * x_telje_suhe)) #juhuslikud alguspunktidele
        algus_y = random.randint(int(-2000 * x_telje_suhe), int(10000 * y_telje_suhe)) #juhuslikud alguspunktidele
        ctx.move_to(algus_x, algus_y) #liigub x,y pidi
        line_color = random.choice(list_of_colors) #juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0 #juhuvärvide kogust määratud rgb
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(random.uniform(1,2)) #joone laius
        for i in range(b): #lisatsüklid täinedavate joonte tekitamiseks nö star effektiks, kus muutb joonte randomiseerimisulats
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(-10,10),random.randrange(-10,10))
            for k in range(b):
                ctx.line_to(algus_x,algus_y)
                ctx.rel_line_to(random.randrange(-5,5),random.randrange(-5,5))
            ctx.stroke() #kannab kanvasele         
            
def raadiolained(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = random.randint(100,3000) #juhuslikud arvud muutujatele,hiljem tsükliarvudena kasutuses
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(int(-2000 * x_telje_suhe), int(7000 * x_telje_suhe)) #juhuslikud alguspunktidele
        algus_y = random.randint(int(-2000 * y_telje_suhe), int(10000 * y_telje_suhe))
        ctx.move_to(algus_x, algus_y) #liigub x,y pidi
        line_color = random.choice(list_of_colors) #juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,3)) 
        for k in range(b):
            ctx.move_to(algus_x, algus_y) #liigub x,y pidi
            ctx.rel_line_to(algus_x,random.randrange(int(-50* x_telje_suhe),int(50* x_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-50* y_telje_suhe),int(50* y_telje_suhe)),algus_y)
            ctx.stroke()#kannab kanvasele
           
def ruudustik(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = random.randint(100,3000)#juhuslikud arvud muutujatele,hiljem tsükliarvudena kasutuses
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(7000* x_telje_suhe)) #juhuslikud alguspunktidele
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe)) #juhuslikud alguspunktidele
        ctx.move_to(algus_x, algus_y)#liigub alguskoordinaatidele
        line_color = random.choice(list_of_colors) #juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,1))
        ctx.stroke()#kannab kanvasele
        for k in range(b):#lisajooned
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(algus_x,random.randrange(int(-50* x_telje_suhe),int(50* x_telje_suhe)))
            ctx.stroke()
        for k in range(b):#lisajooned
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(random.randrange(int(-50* y_telje_suhe),int(50* y_telje_suhe)),algus_y)
            ctx.stroke()
       
def paljujoonivasemal(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(1500 * x_telje_suhe/y_telje_suhe) #tsüklite arv
    for i in range(a):
        ctx.line_to(random.randrange(int(3000* x_telje_suhe)), random.randrange(int(3000* x_telje_suhe))) #põhijoone koordinaadid
        ctx.rel_line_to(random.randrange(int(1000* y_telje_suhe)), random.randrange(int(1000* y_telje_suhe))) #relatiivselt põhikoordinaatidele tekkiva joone koordinaadid
        ctx.set_source_rgb(1, 1, 1)#joone värv must
        ctx.set_line_width(2*x_telje_suhe)#joone laius
        ctx.stroke()#kannab kanvasele
    
def hexagonid_värvilised(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(2000 * x_telje_suhe/y_telje_suhe) #juhuslik arv muutujatele,hiljem tsükliarvuna kasutuses
    for i in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe)) #juhuslikud alguspunktidele
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe)) #juhuslikud alguspunktidele
        suvaarv = random.randrange(0, 300, 5)
        HEX_W, HEX_H = (suvaarv, suvaarv) #hexagoni suurus
        ctx.move_to(algus_x, algus_y)#algkoha nihe
        line_color = random.choice(list_of_colors)#juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(2*x_telje_suhe) #joone laius 
        ctx.rel_move_to(HEX_W/3.0, 0) #relatiivse koordinaadi osas nihe
        ctx.rel_line_to(HEX_W/3.0, 0) #relatiivse koordinaadi osas joon
        ctx.rel_line_to(HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, 0)
        ctx.rel_line_to(-HEX_W/3.0, -HEX_H/3.0)
        ctx.rel_line_to(0, -HEX_H/3.0)
        ctx.rel_line_to(HEX_W/3.0, -HEX_H/3.0)
        ctx.close_path () #kulg kinni
        ctx.stroke ()#kannab kanvasele

def hexagonid_must_valge(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(2000 * x_telje_suhe/y_telje_suhe) #juhuslik arv muutujatele,hiljem tsükliarvuna kasutuses
    for i in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe)) #juhuslikud alguspunktidele
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe)) #juhuslikud alguspunktidele
        suvaarv = random.randrange(0, 300, 5)
        HEX_W, HEX_H = (suvaarv, suvaarv) #hexagoni suurus
        ctx.move_to(algus_x, algus_y) #algkoha nihe
        ctx.set_source_rgb(1, 1, 1)#Joone värv must
        ctx.set_line_width(2*x_telje_suhe)#joone laius
        ctx.rel_move_to(HEX_W/3.0, 0) #relatiivse koordinaadi osas nihe
        ctx.rel_line_to(HEX_W/3.0, 0) #relatiivse koordinaadi osas joon
        ctx.rel_line_to(HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, 0)
        ctx.rel_line_to(-HEX_W/3.0, -HEX_H/3.0)
        ctx.rel_line_to(0, -HEX_H/3.0)
        ctx.rel_line_to(HEX_W/3.0, -HEX_H/3.0)
        ctx.close_path ()#kulg kinni
        ctx.stroke ()#kannab kanvasele

def jooned_nurgast(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    algus_x = random.randint(0, int(2000* x_telje_suhe)) #juhuslikud alguspunktidele
    algus_y = random.randint(0, int(2000* y_telje_suhe)) #juhuslikud alguspunktidele
    l6pp_x = random.randint(0, int(5000* x_telje_suhe)) #juhuslikud lõpppunktidele
    l6pp_y = random.randint(0, int(5000* y_telje_suhe))  #juhuslikud lõpppunktidele
    for i in range(200):
        ctx.line_to(algus_x, algus_y) #jooned algkoordinaatideni
        ctx.rel_line_to(l6pp_x, l6pp_y) #jooned relatiivsest punktist lõppkoordinaatidesse
        line_color = random.choice(list_of_colors)#juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(4*x_telje_suhe)
        algus_x = l6pp_x #lõppkoordinaadid alguseks
        algus_y = l6pp_y 
        l6pp_x = random.randint(int(-2000* x_telje_suhe), int(3000* x_telje_suhe)) #uued random lõppkoordinaadid
        l6pp_y = random.randint(int(-2000* y_telje_suhe), int(2000* y_telje_suhe))
    ctx.close_path()  
    ctx.stroke()#kannab kanvasele

def joonedkeskelt(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(int(150*x_telje_suhe)):
        ctx.line_to(WIDTH/2,HEIGHT/2) #jooned algkoordinaatideni
        ctx.rel_line_to(random.randint(int(-3000* x_telje_suhe),int(3000* x_telje_suhe)),random.randint(int(-3000* y_telje_suhe),int(3000* y_telje_suhe)))
        line_color = random.choice(list_of_colors)#juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(6*x_telje_suhe) #joone laius
        ctx.stroke()#kannab kanvasele

def ringid_valged(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(int(20* x_telje_suhe)):
        r = int(10* x_telje_suhe) #algraadius
        x = random.randint(1,int(3*1980* x_telje_suhe)) #juhuslikud alguspunktidele, korrutatud skaleerimisuhtega
        y = random.randint(1,int(3*1020* y_telje_suhe)) #juhuslikud alguspunktidele , korrutatud skaleerimisuhtega
        for l in range(int(100* x_telje_suhe/y_telje_suhe)):
            ctx.set_source_rgb(1, 1, 1)
            ctx.arc(x, y, r, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
            ctx.set_line_width(2) #joone laius
            ctx.stroke()#kannab kanvasele
            r += int(6* x_telje_suhe/y_telje_suhe)
            x += random.randint(int(-50* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)) #juhuslikud nihe algpunktidele
            y += random.randint(int(-50* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)) #juhuslikud nihe algpunktidele
            
def ringid_värvilised(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(int(20* x_telje_suhe)):
        r = int(10* x_telje_suhe/y_telje_suhe) #algraadius
        x = random.randint(1,int(HEIGHT)) #juhuslikud alguspunktidele
        y = random.randint(1,int(WIDTH)) #juhuslikud alguspunktidele
        for i in range(int(100* x_telje_suhe/y_telje_suhe)):
            line_color = random.choice(list_of_colors) #juhuvärvide kogust värvi määramine
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgb(line_r, line_g, line_b)
            ctx.arc(x, y, r, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
            ctx.set_line_width(2) #joone laius
            ctx.stroke()#kannab kanvasele
            r += int(6* x_telje_suhe/y_telje_suhe) #raadiusemuut
            x += random.randint(int(-50 * x_telje_suhe/y_telje_suhe),int(50 * x_telje_suhe/y_telje_suhe)) #juhuslikud nihe algpunktidele
            y += random.randint(int(-50 * x_telje_suhe/y_telje_suhe),int(50 * x_telje_suhe/y_telje_suhe))  #juhuslikud nihe algpunktidele          
            
def spiderpuff(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(50* x_telje_suhe/y_telje_suhe) #põhimustri algjätekte random arv
    b = 5 #lisajätkete tsüklide arv
    for j in range(a):
        algus_x = WIDTH/2 #algus canvase keskelt
        algus_y = HEIGHT/2 #algus canvase keskelt
        ctx.move_to(algus_x, algus_y)#algkoordinaatidesse nihe
        for i in range(b):
            ctx.line_to(algus_x,algus_y) #joon algkoordinaatidesse ning edaspidi relatiivse koordinaadi järgi juhusliku arvu järgi
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.set_source_rgb(1, 1, 1) #joone värv
            ctx.set_line_width(random.uniform(0,4))
            ctx.stroke() #kannab kanvasele 

def spiderpuffs(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(100* x_telje_suhe/y_telje_suhe)#põhimustri algjätekte random arv
    b = int(50* x_telje_suhe/y_telje_suhe) #lisajätkete tsüklide arv
    for j in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
        ctx.move_to(algus_x, algus_y)#algkoordinaatidesse nihe
        for i in range(b):
            ctx.line_to(algus_x,algus_y) #joon algkoordinaatidesse ning edaspidi relatiivse koordinaadi järgi juhusliku arvu järgi
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.uniform(0,4))#joone paksus juhuarv
            ctx.stroke()    #kannab kanvasele

def susser(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(random.randint(5,int(50* x_telje_suhe/y_telje_suhe))):
        x, y, x1, y1 = WIDTH/2, HEIGHT/2, random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))#randomiseeritud koordinaatkogumi loomine 
        x2, y2, x3, y3 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x4, y4, x5, y5 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x6, y6 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        ctx.set_source_rgb(1, 1, 1)#joone värv
        ctx.set_line_width(random.uniform(0,4)) #joone laius
        ctx.move_to(x, y)
        for j in range(random.randint(0,int(50* x_telje_suhe/y_telje_suhe))):
            ctx.curve_to(x1, y1, x2, y2, x3, y3) #kaare koordinaadid
            ctx.curve_to(x4, y4, x5, y5, x6, y6) #kaare koordinaadid
        ctx.stroke()#kannab kanvasele

def sussernurgast(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(random.randint(int(5* x_telje_suhe/y_telje_suhe),int(30* x_telje_suhe/y_telje_suhe))):
        x, y, x1, y1 = 0, 0, random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))#randomiseeritud koordinaatkogumi loomine 
        x2, y2, x3, y3 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x4, y4, x5, y5 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x6, y6 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        ctx.set_source_rgb(1, 1, 1) #joone värv
        ctx.set_line_width(random.uniform(0,5))#joone laius
        ctx.move_to(x, y)# nihe x,y koordinaatidesse
        for j in range(random.randint(0,10)):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)#kaare koordinaadid
            ctx.curve_to(x4, y4, x5, y5, x6, y6)#kaare koordinaadid
        ctx.stroke()

def magnetlained1(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
        r,t,u,i,o = random.randint(1,int(30* x_telje_suhe/y_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,200),random.randint(0,100)#randomiseeritud koordinaatkogumi loomine 
        x = random.randint(0,5) #randomiseeritud koordinaatkogumi loomine 
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, r)#skaleerimine
        ctx.arc(t, u, i, x, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()
        ctx.stroke()#kannab kanvasele

def magnetlained2(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2) #konstantse kaugsele viib punktid
    r,t,u,i = random.randint(1,int(30* x_telje_suhe/y_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,200)#randomiseeritud koordinaatkogumi loomine 
    for i in range(random.randint(int(50* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
        line_color = random.choice(list_of_colors)#värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.01,0.7))
        ctx.set_line_width(random.uniform(0,3)) #joone laius
        ctx.save() #salvestab punkti
        ctx.rotate(i*math.pi/36) 
        ctx.scale(0.3, r) #skaleerimine
        ctx.arc(t, u, i, 0, 2*math.pi)  #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele

def magnetlained3(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    r,t,u,i = random.randint(1,int(30* x_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,int(200* x_telje_suhe))#randomiseeritud koordinaatkogumi loomine 
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()#salvestab punkti
        ctx.rotate(i*math.pi/36) # rotatsiooni määr
        ctx.scale(0.3, r)#skaleerimine
        ctx.arc(t, u, i, 0, 2*math.pi)  #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele


# järgmised on sama funktsiooni erinevad seadistused,võimalik,et on koodis jäänud kasutamata erinevaid juhuslike muutujaid(neid kustutan tulevikus, kui on kindel, et ei arenda edasi seda osa)kuid endeiselt on väga palju voimalusi ning vajalik katsetada tulevikus

def kiired1(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(50000* x_telje_suhe/y_telje_suhe))):
        line_color = random.choice(list_of_colors)#värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,0.2)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36) #rotatsiooni määr
        ctx.scale(0.3, 1)#skaleerimine
        ctx.arc(i, i, 120, 0, 2*math.pi)  #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.fill()
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele

def kiired2(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
        a = random.randint(0,130)#raadiuse muutjuja
        line_color = random.choice(list_of_colors)#värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,0.2)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)# rotatsiooni määr
        ctx.scale(0.3, 1)#skaleerimine
        ctx.arc(i, i, a, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.fill()
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele

def kiired3(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
        a,d = random.randint(0,int(130* x_telje_suhe/y_telje_suhe)),random.randint(1,int(30* x_telje_suhe/y_telje_suhe))
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,0.2)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)# rotatsiooni määr
        ctx.scale(0.3, d)#skaleerimine
        ctx.arc(i, i, a, a, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.fill()
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele

def kiired4(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
        a = random.randint(0,int(130* x_telje_suhe/y_telje_suhe))
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,0.2)
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)# rotatsiooni määr
        ctx.scale(0.3, 1)#skaleerimine
        ctx.arc(i, i, a, a, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.fill()
        ctx.restore()
        ctx.stroke()#kannab kanvasele

def kiired5(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)#konstantse kaugsele viib punktid
    u,i= random.randint(1,int(100* x_telje_suhe/y_telje_suhe)),random.randint(0,int(2000* x_telje_suhe/y_telje_suhe))
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
        a,d = random.randint(0,int(130* x_telje_suhe/y_telje_suhe)),random.randint(1,int(30* x_telje_suhe/y_telje_suhe))
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.01,0.7))
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)# rotatsiooni määr
        ctx.scale(0.3, d)#skaleerimine
        ctx.arc(i, i, a, a, u*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.fill()
        ctx.restore()
        ctx.stroke()#kannab kanvasele

def kiired6(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980) #skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
        ctx.move_to(algus_x, algus_y)
        x = random.randint(0,int(1000* x_telje_suhe/y_telje_suhe))
        line_color = random.choice(list_of_colors)#värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.05,0.4))
        ctx.set_line_width(random.uniform(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)# rotatsiooni määr
        ctx.scale(0.3, 1)#skaleerimine
        ctx.arc(x, x, 120, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()#taastab punkti
        ctx.stroke()#kannab kanvasele