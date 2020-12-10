from opensimplex import OpenSimplex
import cairo, random, math

def kõverik(cr, laius, kõrgus):
    joon = 2
    os = OpenSimplex(random.randint(0, 2**20))
    cr.set_line_width(joon)
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
    for i in range(0, kõrgus, round(kõrgus/15)):
        os = OpenSimplex(random.randint(0, 2**20))
        cr.set_source_rgba(0.7, 1-(0.4*i)/kõrgus, 1-(0.9*i)/kõrgus, 1)
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
def müra_ringid(cr, laius, kõrgus):
    
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
    
    
    for i in range(round(kõrgus/15), kõrgus, round(kõrgus/15)):
        cr.set_source_rgba(0.5, (0.5*i)/kõrgus, (1*i)/kõrgus, (1*i)/kõrgus)
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