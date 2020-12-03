import cairo
import random
import math

list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
(197, 239, 247), (190, 144, 212),(221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188),
 (41, 241, 195), (243, 156, 18), (189, 195, 199), (101, 198, 187), (255, 246, 143), (243, 241, 239)]

WIDTH = 3*1980
HEIGHT = 3*1020
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)

ctx = cairo.Context(surface)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()


def dontknowyet():
    a = random.randint(100,3000)
    b = random.randint(10,50)
    for j in range(a):
        algus_x = random.randint(-2000, 7000)
        algus_y = random.randint(-2000, 10000)
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(random.randint(1,2))
        for i in range(b):
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(-10,10),random.randrange(-10,10))
            for k in range(b):
                ctx.line_to(algus_x,algus_y)
                ctx.rel_line_to(random.randrange(-5,5),random.randrange(-5,5))
            ctx.stroke()
            
def dontknowyet2():
    a = random.randint(100,3000)
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(-2000, 7000)
        algus_y = random.randint(-2000, 10000)
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,1))
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.rel_line_to(algus_x,random.randrange(-50,50))
            ctx.rel_line_to(random.randrange(-50,50),algus_y)
            ctx.stroke()
           
def dontknowyet3():
    a = random.randint(100,3000)
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(-2000, 7000)
        algus_y = random.randint(-2000, 10000)
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,1))
        ctx.stroke()
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(algus_x,random.randrange(-50,50))
            ctx.stroke()
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(random.randrange(-50,50),algus_y)
            ctx.stroke()
       
def jooned():
    a = 3000
    for i in range(a):
        ctx.line_to(random.randrange(3000), random.randrange(3000))
        ctx.rel_line_to(random.randrange(1000), random.randrange(1000))
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(2)
        ctx.stroke()
    
def hexagonid_värvilised():
    a = 2000
    for i in range(a):
        algus_x = random.randint(-2000, 10000)
        algus_y = random.randint(-2000, 10000)
        suvaarv = random.randrange(0, 300, 5)
        HEX_W, HEX_H = (suvaarv, suvaarv)
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(2)
        ctx.rel_move_to(HEX_W/3.0, 0)
        ctx.rel_line_to(HEX_W/3.0, 0)
        ctx.rel_line_to(HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, 0)
        ctx.rel_line_to(-HEX_W/3.0, -HEX_H/3.0)
        ctx.rel_line_to(0, -HEX_H/3.0)
        ctx.rel_line_to(HEX_W/3.0, -HEX_H/3.0)
        ctx.close_path ()
        ctx.stroke ()

def hexagonid_must_valge():
    a = 2000
    for i in range(1000):
        algus_x = random.randint(-2000, 10000)
        algus_y = random.randint(-2000, 10000)
        suvaarv = random.randrange(0, 300, 5)
        HEX_W, HEX_H = (suvaarv, suvaarv)
        ctx.move_to(algus_x, algus_y)
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(2)
        ctx.rel_move_to(HEX_W/3.0, 0)
        ctx.rel_line_to(HEX_W/3.0, 0)
        ctx.rel_line_to(HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, HEX_H/3.0)
        ctx.rel_line_to(-HEX_W/3.0, 0)
        ctx.rel_line_to(-HEX_W/3.0, -HEX_H/3.0)
        ctx.rel_line_to(0, -HEX_H/3.0)
        ctx.rel_line_to(HEX_W/3.0, -HEX_H/3.0)
        ctx.close_path ()
        ctx.stroke ()

def jooned_nurgast():
    algus_x = random.randint(0, 2000)
    algus_y = random.randint(0, 2000)
    l6pp_x = random.randint(0, 5000)
    l6pp_y = random.randint(0, 5000)
    
    for i in range(200):
        ctx.line_to(algus_x, algus_y)
        ctx.rel_line_to(l6pp_x, l6pp_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(1)
        algus_x = l6pp_x 
        algus_y = l6pp_y 
        i -= 1
        l6pp_x = random.randint(-2000, 3000)
        l6pp_y = random.randint(-2000, 2000)
    ctx.close_path()    
    ctx.stroke()

def joonedkeskelt():
    a = 150

    for i in range(a):
        ctx.line_to(WIDTH/2,HEIGHT/2)
        ctx.rel_line_to(random.randint(-3000,3000),random.randint(-3000,3000))
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(2)
        ctx.stroke()

def ringid_valged():
    for i in range(20):
        r = 10
        x = random.randint(1,3*1980)
        y = random.randint(1,3*1980)
        for i in range(100):
            ctx.set_source_rgb(1, 1, 1)
            ctx.arc(x, y, r, 0, 2*math.pi)
            ctx.set_line_width(2)
            ctx.stroke()
            r += 6
            x += random.randint(-50,50)
            y += random.randint(-50,50)
            
def ringid_värvilised():
    for i in range(20):
        r = 10
        x = random.randint(0,3*1980)
        y = random.randint(0,3*1980)
        for i in range(100):
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgb(line_r, line_g, line_b)
            ctx.arc(x, y, r, 0, 2*math.pi)
            ctx.set_line_width(2)
            ctx.stroke()
            r += 6
            x += random.randint(-50,50)
            y += random.randint(-50,50)            
            
def spiderpuff():
    a = 50
    b = 5
    for j in range(a):
        algus_x = WIDTH/2
        algus_y = HEIGHT/2
        ctx.move_to(algus_x, algus_y)
        for i in range(b):
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randint(0,2))
            ctx.stroke()  

def spiderpuffs():
    a = 100
    b = 50
    for j in range(a):
        algus_x = random.randint(-2000, 10000)
        algus_y = random.randint(-2000, 10000)
        ctx.move_to(algus_x, algus_y)
        for i in range(b):
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.rel_line_to(random.randrange(-200,200,50),random.randrange(-200,200,50))
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randint(0,2))
            ctx.stroke()    

def susser():
    for i in range(random.randint(5,50)):
        x, y, x1, y1 = WIDTH/2, HEIGHT/2, random.randint(0,6000), random.randint(0,3000)
        x2, y2, x3, y3 = random.randint(0,6000), random.randint(0,3000), random.randint(0,6000), random.randint(0,3000)
        x4, y4, x5, y5 = random.randint(0,6000), random.randint(0,3000), random.randint(0,6000), random.randint(0,3000)
        x6, y6 = random.randint(0,6000), random.randint(0,3000)
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,4))
        ctx.move_to(x, y)
        for j in range(random.randint(0,50)):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)
            ctx.curve_to(x4, y4, x5, y5, x6, y6)
        ctx.stroke()

def sussernurgast():
    for i in range(random.randint(5,30)):
        x, y, x1, y1 = 0, 0, random.randint(0,6000), random.randint(0,3000)
        x2, y2, x3, y3 = random.randint(0,6000), random.randint(0,3000), random.randint(0,6000), random.randint(0,3000)
        x4, y4, x5, y5 = random.randint(0,6000), random.randint(0,3000), random.randint(0,6000), random.randint(0,3000)
        x6, y6 = random.randint(0,6000), random.randint(0,3000)
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,5))
        ctx.move_to(x, y)
        for j in range(random.randint(0,10)):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)
            ctx.curve_to(x4, y4, x5, y5, x6, y6)
        ctx.stroke()

def magnetlained():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(36,500)):
            r,t,u,i,o = random.randint(1,30),random.randint(0,100),random.randint(0,100),random.randint(0,200),random.randint(0,100)
            x = random.randint(0,5)
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, r)
            ctx.arc(t, u, i, x, 2*math.pi)
            ctx.restore()
            ctx.stroke()

def areyousure():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        r,t,u,i = random.randint(1,30),random.randint(0,100),random.randint(0,100),random.randint(0,200)
        for i in range(random.randint(36,500)):
            ctx.set_source_rgb(1, 1, 1)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.01,0.7))
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, r)
            ctx.arc(t, u, i, 0, 2*math.pi)
            ctx.restore()
            ctx.stroke()

def v2garandomasi():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        r,t,u,i = random.randint(1,30),random.randint(0,100),random.randint(0,100),random.randint(0,200)
        for i in range(random.randint(36,500)):
            ctx.set_source_rgb(1, 1, 1)
    # siin on ka juhuslike värvidega variant vajadusel
    #         line_color = random.choice(list_of_colors)
    #         line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
    #         ctx.set_source_rgb(line_r, line_g, line_b)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, r)
            ctx.arc(t, u, i, 0, 2*math.pi)
            ctx.restore()
            ctx.stroke()


# järgmised on sama funktsiooni erinevad seadistused,võimalik,et on koodis jäänud kasutamata erinevaid juhuslike muutujaid(neid kustutan tulevikus, kui on kindel, et ei arenda edasi seda osa)kuid endeiselt on väga palju voimalusi ning vajalik katsetada tulevikus

def midagit1():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(36,50000)):
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,0.2)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, 1)
            ctx.arc(i, i, 120, 0, 2*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit2():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(36,10000)):
            a = random.randint(0,130)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,0.2)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, 1)
            ctx.arc(i, i, a, 0, 2*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit3():
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(36,10000)):
            a,d = random.randint(0,130),random.randint(1,30)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,0.2)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, d)
            ctx.arc(i, i, a, a, 2*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit4():        
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(36,10000)):
            a = random.randint(0,130)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,0.2)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, 1)
            ctx.arc(i, i, a, a, 2*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit5():  
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        u,i= random.randint(1,100),random.randint(0,2000)
        for i in range(random.randint(36,10000)):
            a,d = random.randint(0,130),random.randint(1,30)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.01,0.7))
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, d)
            ctx.arc(i, i, a, a, u*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit6():  
    for k in range(1):
        for i in range(random.randint(36,10000)):
            algus_x = random.randint(-2000, 10000)
            algus_y = random.randint(-2000, 10000)
            ctx.move_to(algus_x, algus_y)
            x = random.randint(0,1000)
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgba(line_r, line_g, line_b,random.uniform(0.05,0.4))
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, 1)
            ctx.arc(x, x, 120, 0, 2*math.pi)
            ctx.restore()
            ctx.stroke()

surface.write_to_png('xxx.png')