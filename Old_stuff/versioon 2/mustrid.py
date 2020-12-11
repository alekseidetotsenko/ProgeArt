# siin on minu need mustrid, mis ma esimese versiooni jaoks esitasin. panen juurde siia varsti.
# svg ja png raamid on ära võetud
# kõik impordid panin ka praegu põhiprogrammi. ei tea kas see on hea mõte või kuidas seda paremini teha

def värvimuster(c, laius, kõrgus):
    
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
        for i in range(len(kujund)-1, 0, -2):
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        return kujund

    def tups(kontekst, kujund, baas_muut, baas_deform, udu_muut, udu_deform, kihtide_arv, R, G, B):
        for a in range(baas_deform):
            baas = deform(kujund, baas_muut)
        for b in range(kihtide_arv):
            udu = copy.deepcopy(baas)
            for d in range(udu_deform):
                udu = deform(udu, udu_muut)
            kontekst.move_to(udu[0][0], udu[0][1])
            for e in range(len(udu)):
                kontekst.line_to(udu[e][0], udu[e][1])
            kontekst.set_source_rgba(R, G, B, 0.04)
            kontekst.fill()
    
    # põhifunktsioon
    c.set_source_rgba(0, 0, 0, 1)
    c.paint()
    for f in range(10):
        kujund = hulknurk(10, random.randint(0, laius), random.randint(0, kõrgus), random.randint(100, 200))
        tups(c, kujund, 10, 6, 5, 7, 30, 1, random.uniform(0,1), 0)

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
        for i in range(len(kujund)-1, 0, -2):
            keskpunkti_x = (kujund[i][0] + kujund[i-1][0])/2
            keskpunkti_y = (kujund[i][1] + kujund[i-1][1])/2
            juhu_punkt = (random.gauss(keskpunkti_x, muut), random.gauss(keskpunkti_y, muut))
            kujund.insert(i, juhu_punkt)
        return kujund

    def tups(kontekst, kujund, baas_muut, baas_deform, udu_muut, udu_deform, kihtide_arv, R, G, B):
        for a in range(baas_deform):
            baas = deform(kujund, baas_muut)
        for b in range(kihtide_arv):
            udu = copy.deepcopy(baas)
            for d in range(udu_deform):
                udu = deform(udu, udu_muut)
            kontekst.move_to(udu[0][0], udu[0][1])
            for e in range(len(udu)):
                kontekst.line_to(udu[e][0], udu[e][1])
            kontekst.set_source_rgba(R, G, B, 0.04)
            kontekst.fill()
    
    # põhifunktsioon
    c.set_source_rgba(0, 0, 0, 1)
    c.paint()
    kujund = hulknurk(10, laius/2, kõrgus/2, 200)
    tups(c, kujund, 10, 6, 5, 7, 30, 1, 1, 1)

def nurkmuster(c, laius, kõrgus):

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
    tsüklite_arv = 1000
    c.set_source_rgb(0,0,0)
    c.paint()
    for i in range(tsüklite_arv):
        keskpunkt_x, keskpunkt_y = random.randint(0, laius), random.randint(0, kõrgus)
        nurgad = random.randint(3, 12)
        raadius = random.randint(30, kõrgus/2)
        kujund = hulknurk(nurgad, keskpunkt_x, keskpunkt_y, raadius)
        for j in range(len(kujund)-1, 0, -1):
            c.move_to(kujund[j][0], kujund[j][1])
            c.line_to(kujund[j-1][0], kujund[j-1][1])
            värv_hall = random.uniform(0, 1)
            c.set_source_rgb(värv_hall, värv_hall, värv_hall)
            c.set_line_width(0.2)
        c.stroke()

def sirgjooneline_taustaga(c, laius, kõrgus):
    
    # põhifunktsioon. abifunktsioone ei ole sellel
    # algab tausta värvi juhusliku valikuga. seda võiks saada ise valida
    R = random.uniform(0.20, 0.50)
    G = random.uniform(0.20, 0.50)
    B = random.uniform(0.20, 0.50)
    c.set_source_rgb(R, G, B)
    c.paint()
    for i in range(2000):
        algus_x = random.randint(-100, laius + 100) # üle ääre
        algus_y = random.randint(-100, kõrgus + 100)
        lõpp_x = random.randint(-100, laius + 100)
        lõpp_y = random.randint(-100, kõrgus + 100)
        joone_värv = random.uniform(0, 1)
        c.set_source_rgb(joone_värv, joone_värv, joone_värv)
        c.move_to(algus_x, algus_y)
        c.line_to(lõpp_x, lõpp_y)
        c.set_line_width(0.2)
        c.stroke()        

def hulknurgamuster(c, laius, kõrgus):
    
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
    c.set_source_rgba(0, 0, 0, 1)
    c.paint()
    for i in range(2, 30):
        nurgad = random.randint(5,20)
        raadius = i**2
        kujund = hulknurk(nurgad, 0, 0, raadius/4)
        pööre = random.uniform(0, 4)
        c.save()
        c.translate(random.gauss(laius/2, 10), random.gauss(kõrgus/2, 10))
        c.rotate(math.pi*pööre)
        for j in range(len(kujund)-1, 0, -1):
            c.move_to(kujund[j][0], kujund[j][1])
            c.line_to(kujund[j-1][0], kujund[j-1][1])
        c.set_source_rgb(1, 1, 1)
        c.set_line_width(1)
        c.stroke()
        c.restore()
