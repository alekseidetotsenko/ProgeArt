import cairo
import random
import math

list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
(197, 239, 247), (190, 144, 212),(221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188),
 (41, 241, 195), (243, 156, 18), (189, 195, 199), (101, 198, 187), (255, 246, 143), (243, 241, 239)]


WIDTH = 2000
HEIGHT = 3000 
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)

ctx = cairo.Context(surface)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

x_telje_suhe = WIDTH / (3*1980)
y_telje_suhe = HEIGHT / (3*1020)

def dontknowyet(ctx,WIDTH,HEIGHT):
    a = random.randint(100,3000)
    b = random.randint(10,50)
    for j in range(a):
        algus_x = random.randint(int(-2000 * x_telje_suhe), int(7000 * x_telje_suhe))
        algus_y = random.randint(int(-2000 * x_telje_suhe), int(10000 * y_telje_suhe))
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
            
def dontknowyet2(ctx,WIDTH,HEIGHT):
    a = random.randint(100,3000)
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(int(-2000 * x_telje_suhe), int(7000 * x_telje_suhe))
        algus_y = random.randint(int(-2000 * y_telje_suhe), int(10000 * y_telje_suhe))
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,1))
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.rel_line_to(algus_x,random.randrange(int(-50* x_telje_suhe),int(50* x_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-50* y_telje_suhe),int(50* y_telje_suhe)),algus_y)
            ctx.stroke()
           
def dontknowyet3(ctx,WIDTH,HEIGHT):
    a = random.randint(100,3000)
    b = random.randint(2,50)
    for j in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(7000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
        ctx.move_to(algus_x, algus_y)
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgba(line_r, line_g, line_b, random.uniform(0.1,0.5))
        ctx.set_line_width(random.uniform(0.01,1))
        ctx.stroke()
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(algus_x,random.randrange(int(-50* x_telje_suhe),int(50* x_telje_suhe)))
            ctx.stroke()
        for k in range(b):
            ctx.move_to(algus_x, algus_y)
            ctx.line_to(random.randrange(int(-50* y_telje_suhe),int(50* y_telje_suhe)),algus_y)
            ctx.stroke()
       
def jooned(ctx,WIDTH,HEIGHT):
    a = int(1500 * x_telje_suhe/y_telje_suhe)
    for i in range(a):
        ctx.line_to(random.randrange(int(3000* x_telje_suhe)), random.randrange(int(3000* x_telje_suhe)))
        ctx.rel_line_to(random.randrange(int(1000* y_telje_suhe)), random.randrange(int(1000* y_telje_suhe)))
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(2)
        ctx.stroke()
    
def hexagonid_värvilised(ctx,WIDTH,HEIGHT):
    a = int(2000 * x_telje_suhe/y_telje_suhe)
    for i in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
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

def hexagonid_must_valge(ctx,WIDTH,HEIGHT):
    a = 2000
    for i in range(1000):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
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

def jooned_nurgast(ctx,WIDTH,HEIGHT):
    algus_x = random.randint(0, int(2000* x_telje_suhe))
    algus_y = random.randint(0, int(2000* y_telje_suhe))
    l6pp_x = random.randint(0, int(5000* x_telje_suhe))
    l6pp_y = random.randint(0, int(5000* y_telje_suhe))  
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
        l6pp_x = random.randint(int(-2000* x_telje_suhe), int(3000* x_telje_suhe))
        l6pp_y = random.randint(int(-2000* y_telje_suhe), int(2000* y_telje_suhe))
    ctx.close_path()    
    ctx.stroke()

def joonedkeskelt(ctx,WIDTH,HEIGHT):
    a = 150
    for i in range(a):
        ctx.line_to(WIDTH/2,HEIGHT/2)
        ctx.rel_line_to(random.randint(int(-3000* x_telje_suhe),int(3000* x_telje_suhe)),random.randint(int(-3000* y_telje_suhe),int(3000* y_telje_suhe)))
        line_color = random.choice(list_of_colors)
        line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
        ctx.set_source_rgb(line_r, line_g, line_b)
        ctx.set_line_width(2)
        ctx.stroke()

def ringid_valged(ctx,WIDTH,HEIGHT):
    for i in range(int(20* x_telje_suhe/y_telje_suhe)):
        r = int(10* x_telje_suhe/y_telje_suhe)
        x = random.randint(1,int(3*1980* x_telje_suhe))
        y = random.randint(1,int(3*1980* y_telje_suhe))
        for i in range(int(100* x_telje_suhe/y_telje_suhe)):
            ctx.set_source_rgb(1, 1, 1)
            ctx.arc(x, y, r, 0, 2*math.pi)
            ctx.set_line_width(2)
            ctx.stroke()
            r += int(6* x_telje_suhe/y_telje_suhe)
            x += random.randint(int(-50* x_telje_suhe),int(50* x_telje_suhe))
            y += random.randint(int(-50* y_telje_suhe),int(50* y_telje_suhe))
            
def ringid_värvilised(ctx,WIDTH,HEIGHT):
    for i in range(int(20* x_telje_suhe/y_telje_suhe)):
        r = int(10* x_telje_suhe/y_telje_suhe)
        x = random.randint(1,int(HEIGHT))
        y = random.randint(1,int(WIDTH))
        for i in range(int(100* x_telje_suhe/y_telje_suhe)):
            line_color = random.choice(list_of_colors)
            line_r, line_g, line_b = line_color[0]/255.0, line_color[1]/255.0, line_color[2]/255.0
            ctx.set_source_rgb(line_r, line_g, line_b)
            ctx.arc(x, y, r, 0, 2*math.pi)
            ctx.set_line_width(2)
            ctx.stroke()
            r += int(6* x_telje_suhe/y_telje_suhe)
            x += random.randint(int(-50 * x_telje_suhe/y_telje_suhe),int(50 * x_telje_suhe/y_telje_suhe))
            y += random.randint(int(-50 * x_telje_suhe/y_telje_suhe),int(50 * x_telje_suhe/y_telje_suhe))           
            
def spiderpuff(ctx,WIDTH,HEIGHT):
    a = int(50* x_telje_suhe/y_telje_suhe)
    b = 5
    for j in range(a):
        algus_x = WIDTH/2
        algus_y = HEIGHT/2
        ctx.move_to(algus_x, algus_y)
        for i in range(b):
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randint(0,2))
            ctx.stroke()  

def spiderpuffs(ctx,WIDTH,HEIGHT):
    a = int(100* x_telje_suhe/y_telje_suhe)
    b = int(50* x_telje_suhe/y_telje_suhe)
    for j in range(a):
        algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
        algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
        ctx.move_to(algus_x, algus_y)
        for i in range(b):
            ctx.line_to(algus_x,algus_y)
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.rel_line_to(random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)),random.randrange(int(-200* x_telje_suhe/y_telje_suhe),int(200* x_telje_suhe/y_telje_suhe),int(50* x_telje_suhe/y_telje_suhe)))
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randint(0,2))
            ctx.stroke()    

def susser(ctx,WIDTH,HEIGHT):
    for i in range(random.randint(5,int(50* x_telje_suhe/y_telje_suhe))):
        x, y, x1, y1 = WIDTH/2, HEIGHT/2, random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x2, y2, x3, y3 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x4, y4, x5, y5 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x6, y6 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,4))
        ctx.move_to(x, y)
        for j in range(random.randint(0,int(50* x_telje_suhe/y_telje_suhe))):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)
            ctx.curve_to(x4, y4, x5, y5, x6, y6)
        ctx.stroke()

def sussernurgast(ctx,WIDTH,HEIGHT):
    for i in range(random.randint(int(5* x_telje_suhe/y_telje_suhe),int(30* x_telje_suhe/y_telje_suhe))):
        x, y, x1, y1 = 0, 0, random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x2, y2, x3, y3 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x4, y4, x5, y5 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe)), random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        x6, y6 = random.randint(0,int(6000* x_telje_suhe)), random.randint(0,int(3000* y_telje_suhe))
        ctx.set_source_rgb(1, 1, 1)
        ctx.set_line_width(random.randrange(0,5))
        ctx.move_to(x, y)
        for j in range(random.randint(0,10)):
            ctx.curve_to(x1, y1, x2, y2, x3, y3)
            ctx.curve_to(x4, y4, x5, y5, x6, y6)
        ctx.stroke()

def magnetlained(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
            r,t,u,i,o = random.randint(1,int(30* x_telje_suhe/y_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,200),random.randint(0,100)
            x = random.randint(0,5)
            ctx.set_source_rgb(1, 1, 1)
            ctx.set_line_width(random.randrange(0,3))
            ctx.save()
            ctx.rotate(i*math.pi/36)
            ctx.scale(0.3, r)
            ctx.arc(t, u, i, x, 2*math.pi)
            ctx.restore()
            ctx.stroke()

def areyousure(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        r,t,u,i = random.randint(1,int(30* x_telje_suhe/y_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,200)
        for i in range(random.randint(int(50* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
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

def v2garandomasi(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        r,t,u,i = random.randint(1,int(30* x_telje_suhe)),random.randint(0,int(100* x_telje_suhe)),random.randint(0,int(100* y_telje_suhe)),random.randint(0,int(200* x_telje_suhe))
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(500* x_telje_suhe/y_telje_suhe))):
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

def midagit1(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(50000* x_telje_suhe/y_telje_suhe))):
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

def midagit2(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
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

def midagit3(ctx,WIDTH,HEIGHT):
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
            a,d = random.randint(0,int(130* x_telje_suhe/y_telje_suhe)),random.randint(1,int(30* x_telje_suhe/y_telje_suhe))
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

def midagit4(ctx,WIDTH,HEIGHT):        
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
            a = random.randint(0,int(130* x_telje_suhe/y_telje_suhe))
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

def midagit5(ctx,WIDTH,HEIGHT):  
    for k in range(1):
        ctx.translate(WIDTH/2, HEIGHT/2)
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
            ctx.arc(i, i, a, a, u*math.pi)
            ctx.fill()
            ctx.restore()
            ctx.stroke()

def midagit6(ctx,WIDTH,HEIGHT):  
    for k in range(1):
        for i in range(random.randint(int(36* x_telje_suhe/y_telje_suhe),int(10000* x_telje_suhe/y_telje_suhe))):
            algus_x = random.randint(int(-2000* x_telje_suhe), int(10000* x_telje_suhe))
            algus_y = random.randint(int(-2000* y_telje_suhe), int(10000* y_telje_suhe))
            ctx.move_to(algus_x, algus_y)
            x = random.randint(0,int(1000* x_telje_suhe/y_telje_suhe))
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
            
ringid_valged(ctx, WIDTH, HEIGHT)

surface.write_to_png('xxx.png')