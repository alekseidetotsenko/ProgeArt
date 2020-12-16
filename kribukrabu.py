import cairo
import random
import math



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
        ctx.set_line_width(random.randint(1,2)) #joone laius
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
        ctx.set_line_width(random.uniform(0.01,1)) 
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
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(algus_x,random.randrange(int(-50* x_telje_suhe),int(50* x_telje_suhe)))
            ctx.stroke()
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(random.randrange(int(-50* y_telje_suhe),int(50* y_telje_suhe)),algus_y)
            ctx.stroke()
       
def karvanekast(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    a = int(1500 * x_telje_suhe/y_telje_suhe) #tsüklite arv
    for i in range(a):
        ctx.line_to(random.randrange(int(3000* x_telje_suhe)), random.randrange(int(3000* x_telje_suhe))) #põhijoone koordinaadid
        ctx.rel_line_to(random.randrange(int(1000* y_telje_suhe)), random.randrange(int(1000* y_telje_suhe))) #relatiivselt põhikoordinaatidele tekkiva joone koordinaadid
        ctx.set_source_rgb(1, 1, 1)#joone värv must
        ctx.set_line_width(2)#joone laius
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
        ctx.set_line_width(2) #joone laius 
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
        ctx.set_line_width(2)#joone laius
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
        ctx.set_line_width(1)
        algus_x = l6pp_x #lõppkoordinaadid alguseks
        algus_y = l6pp_y 
        l6pp_x = random.randint(int(-2000* x_telje_suhe), int(3000* x_telje_suhe))
        l6pp_y = random.randint(int(-2000* y_telje_suhe), int(2000* y_telje_suhe))
    ctx.close_path()    
    ctx.stroke()#kannab kanvasele

def joonedkeskelt(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(int(150*x_telje_suhe)):
        ctx.line_to(WIDTH/2,HEIGHT/2)
        ctx.rel_line_to(random.randint(int(-3000* x_telje_suhe),int(3000* x_telje_suhe)),random.randint(int(-3000* y_telje_suhe),int(3000* y_telje_suhe)))
        line_color = random.choice(list_of_colors)#juhuvärvide kogust värvi määramine
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(2)
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
            ctx.set_line_width(2)
            ctx.stroke()#kannab kanvasele
            r += int(6* x_telje_suhe/y_telje_suhe)
            x += random.randint(int(-50* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)) #juhuslikud nihe algpunktidele
            y += random.randint(int(-50* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)) #juhuslikud nihe algpunktidele
            
def ringid_värvilised(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    for i in range(int(20* x_telje_suhe/y_telje_suhe)):
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
            ctx.set_line_width(random.randint(0,2))
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
            ctx.set_line_width(random.randint(0,2))#joone paksus juhuarv
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
        ctx.set_line_width(random.randrange(0,4)) #joone laius
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
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,5))#joone laius
        ctx.move_to(x, y)
        for j in range(random.randint(0,10)):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)#kaare koordinaadid
            ctx.curve_to(x4, y4, x5, y5, x6, y6)#kaare koordinaadid
        ctx.stroke()

def magnetlained1(ctx,WIDTH,HEIGHT):
    x_telje_suhe = WIDTH / (3*1980)#skaleerimissuhe x ja y telje jaoks
    y_telje_suhe = HEIGHT / (3*1020)
    ctx.translate(WIDTH/2, HEIGHT/2)
    for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
        r,t,u,i,o = random.randint(1,int(30* x_telje_suhe/y_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,200),random.randint(0,100)
        x = random.randint(0,5)
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,3))
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
        ctx.set_line_width(random.randrange(0,3)) #joone laius
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()#salvestab punkti
        ctx.rotate(i*math.pi/36)
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
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b,0.2)
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, 1)
        ctx.arc(i, i, 120, 0, 2*math.pi)  #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, 1)
        ctx.arc(i, i, a, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, d)
        ctx.arc(i, i, a, a, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, 1)
        ctx.arc(i, i, a, a, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, d)
        ctx.arc(i, i, a, a, u*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
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
        ctx.set_line_width(random.randrange(0,3))
        ctx.save()
        ctx.rotate(i*math.pi/36)
        ctx.scale(0.3, 1)
        ctx.arc(x, x, 120, 0, 2*math.pi) #kaare koordinaadid(x,y koordinaat, raaidus, nurk 1 ja nurk 2)
        ctx.restore()
        ctx.stroke()#kannab kanvasele
