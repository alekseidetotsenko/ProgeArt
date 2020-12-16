from opensimplex import OpenSimplex
import cairo, random, math, copy

def kõverik(cr, laius, kõrgus):
    joone_laius = 2*max(laius, kõrgus)/594
    os = OpenSimplex(random.randint(0, 2**20))
    cr.set_line_width(joone_laius)
    cr.set_source_rgb(0, 0, 0)
    cr.translate(laius/2, kõrgus/2)
    z1 = math.pi/180
    z = 0.5
    j = math.pi/90
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
        cr.rotate(j)
        a+=j
        
    cr.stroke()
    
def joonestik(cr, laius, kõrgus):
    os = OpenSimplex(random.randint(0, 2**20))
    zoom = .002
    zoom1 = .006
    zoom2 = .009
    
    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(2)
    for i in range(round(kõrgus/15), kõrgus, round(kõrgus/15)):
        müra = (os.noise2d(0*zoom,i*zoom)*2+os.noise2d(0*zoom1,i*zoom1)/2+os.noise2d(0*zoom2,i*zoom2)/4)*100
        cr.move_to(0, i + müra)
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
    
    cr.set_line_width(10)
    
    paigal = random.randint(0, 2)
    rgb = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    
    for i in range(0, kõrgus, round(kõrgus/15)):
        os = OpenSimplex(random.randint(0, 2**20))
        if paigal == 0:
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
        cr.line_to(laius, i+müra)
        cr.line_to(laius, kõrgus)
        cr.line_to(0, kõrgus)
        cr.fill()

def punkt_ringis(cr, os, a, i):
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
    
def ringid(cr, laius, kõrgus):
    
    os = OpenSimplex(random.randint(0, 2**20))
    
    cr.set_line_width(2)
    cr.set_source_rgb(.4, .4, .4)
    cr.translate(laius/2, kõrgus/2)
    j = 0.1
    for i in range(8):
        r = i * min(laius, kõrgus)/20
        a=0
        while a <= 2*math.pi:
            punkt_ringis(cr, os, a, r)
            cr.rotate(j)
            a+=j
        cr.rotate(2*math.pi-a)
        punkt_ringis(cr, os, 0, r)
        cr.stroke()

def pusa(cr, laius, kõrgus):
    
    os = OpenSimplex(random.randint(0, 2**20))
    cr.set_line_width(2)
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
            for x in range(1, 20):
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
    c.set_line_width(10)
    for i in range(0, random.randint(10,20)):
        x = random.randint(0, laius)
        y = random.randint(0, kõrgus)
        raadius = random.randint(3, round(min(laius,kõrgus)/4))
        for i in range(0,raadius,7):
            for i in range(0,raadius,7):
                c.set_source_rgba(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), 0.1)
                c.arc(x, y, raadius - i, 0, 2 * math.pi)
                c.stroke()

# indreku mustrid ... tututuuu pikk jutt et ma pärast üles leiaks, kus nad on ... peaks 'tututuuu' panema ühe mustri nimeks ... Hea mõte :)

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

