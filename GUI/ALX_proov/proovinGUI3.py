from tkinter import *
# from tkinter.ttk import *
from PIL import ImageTk, Image

window = Tk()
window.title('ProgeArt')
# window.geometry("1280x1024")

#siin funktsioon generate nupust, ei ole veel asjalikuks tehtud, esialgse mõte järgi kogub sisestusi kokku
#vastandab muutujatele ning käivitab siis põhifunktsiooni(mis võiks kasutada canvase funktsiooni+stiili_funktsiooni), mille peame kirjutama, mis teeb pildi ära.
def generate():
    file_name  = fail_name_1.get()
    file_type = selected.get()
    
    canvas_height = input_canvas_height_input.get()
    canvas_width = input_canvas_width_input.get()
    joonistamine()
    print(file_name)
    print(file_type)
    print(canvas_height)
    print(canvas_width)
    
    
#     põhifunktsioon(laius, kõrgus, file_type, failinimi, kunstistiil)
    #canvase funktsioon
    ##võtab failinimi, canvas suurused, failitüüp
    #kunstisiiili muutuja määramine
    
    #mingi main funktsiooni aktiveerimine.
    
#edasi nuppu funktsioon    
def forward(image_number):
    global art_style_label
    global button_forward
    global button_back
    
    art_style_label.grid_forget()
    art_style_label = Label(image = image_list[image_number-1])
    button_forward = Button(window, text = '>>', command = lambda:forward(image_number+1))
    button_back = Button(window, text = '<<', command = lambda:back(image_number-1))
    
    if image_number == len(image_list):
        button_forward = Button(window, text = '>>', state = DISABLED)
    
    art_style_label.grid(column = 0, row = 6, columnspan = 3)
    button_back.grid(column=0, row=15)
    button_forward.grid(column=1, row=15)
#tagasi nuppu funktsioon      
def back(image_number):
    global art_style_label
    global button_forward
    global button_back
    
    art_style_label.grid_forget()
    art_style_label = Label(image = image_list[image_number-1])
    button_forward = Button(window, text = '>>', command = lambda:forward(image_number+1))
    button_back = Button(window, text = '<<', command = lambda:back(image_number-1))

    if image_number == 1:
        button_back = Button(window, text = '<<', state = DISABLED)
    
    art_style_label.grid(column = 0, row = 6, columnspan = 3)
    button_back.grid(column=0, row=15)
    button_forward.grid(column=1, row=15)
 
 
#siia v]iks tekitada funktsiooni piltide tootluseks, muidu proge laadimine v6tab hullult aega
# def risizepicture(failinimi):
    
#piltide sektsioon,resize-ga    
raw_sart_style_img1 = Image.open("midagit6.png")
resized_art_style_img1 = raw_sart_style_img1.resize((594,306), Image.ANTIALIAS)
art_style_img1 = ImageTk.PhotoImage(resized_art_style_img1)

raw_sart_style_img2 = Image.open('dontknowyet.png')
resized_art_style_img2 = raw_sart_style_img2.resize((594,306), Image.ANTIALIAS)
art_style_img2 = ImageTk.PhotoImage(resized_art_style_img2)

raw_sart_style_img3 = Image.open('dontknowyet2.png')
resized_art_style_img3 = raw_sart_style_img3.resize((594,306), Image.ANTIALIAS)
art_style_img3 = ImageTk.PhotoImage(resized_art_style_img3)

raw_sart_style_img4 = Image.open('dontknowyet3.png')
resized_art_style_img4 = raw_sart_style_img4.resize((594,306), Image.ANTIALIAS)
art_style_img4 = ImageTk.PhotoImage(resized_art_style_img4)

raw_sart_style_img5 = Image.open("jooned.png")
resized_art_style_img5 = raw_sart_style_img5.resize((594,306), Image.ANTIALIAS)
art_style_img5 = ImageTk.PhotoImage(resized_art_style_img5)

raw_sart_style_img6 = Image.open("hexagonid_värvilised.png")
resized_art_style_img6 = raw_sart_style_img6.resize((594,306), Image.ANTIALIAS)
art_style_img6 = ImageTk.PhotoImage(resized_art_style_img6)

raw_sart_style_img7 = Image.open("hexagonid_must_valge.png")
resized_art_style_img7 = raw_sart_style_img7.resize((594,306), Image.ANTIALIAS)
art_style_img7 = ImageTk.PhotoImage(resized_art_style_img7)

raw_sart_style_img8 = Image.open("jooned_nurgast.png")
resized_art_style_img8 = raw_sart_style_img8.resize((594,306), Image.ANTIALIAS)
art_style_img8 = ImageTk.PhotoImage(resized_art_style_img8)

raw_sart_style_img9 = Image.open("joonedkeskelt.png")
resized_art_style_img9 = raw_sart_style_img9.resize((594,306), Image.ANTIALIAS)
art_style_img9 = ImageTk.PhotoImage(resized_art_style_img9)

raw_sart_style_img10 = Image.open("ringid_valged.png")
resized_art_style_img10 = raw_sart_style_img10.resize((594,306), Image.ANTIALIAS)
art_style_img10 = ImageTk.PhotoImage(resized_art_style_img10)

raw_sart_style_img11 = Image.open("ringid_värvilised.png")
resized_art_style_img11 = raw_sart_style_img11.resize((594,306), Image.ANTIALIAS)
art_style_img11 = ImageTk.PhotoImage(resized_art_style_img11)

raw_sart_style_img12 = Image.open("spiderpuff.png")
resized_art_style_img12 = raw_sart_style_img12.resize((594,306), Image.ANTIALIAS)
art_style_img12 = ImageTk.PhotoImage(resized_art_style_img12)

raw_sart_style_img13 = Image.open("spiderpuffs.png")
resized_art_style_img13 = raw_sart_style_img13.resize((594,306), Image.ANTIALIAS)
art_style_img13 = ImageTk.PhotoImage(resized_art_style_img13)

raw_sart_style_img14 = Image.open("susser.png")
resized_art_style_img14 = raw_sart_style_img14.resize((594,306), Image.ANTIALIAS)
art_style_img14 = ImageTk.PhotoImage(resized_art_style_img14)

raw_sart_style_img15 = Image.open("sussernurgast.png")
resized_art_style_img15 = raw_sart_style_img15.resize((594,306), Image.ANTIALIAS)
art_style_img15 = ImageTk.PhotoImage(resized_art_style_img15)

raw_sart_style_img16 = Image.open("magnetlained.png")
resized_art_style_img16 = raw_sart_style_img16.resize((594,306), Image.ANTIALIAS)
art_style_img16 = ImageTk.PhotoImage(resized_art_style_img16)

raw_sart_style_img17 = Image.open("areyousure.png")
resized_art_style_img17 = raw_sart_style_img17.resize((594,306), Image.ANTIALIAS)
art_style_img17 = ImageTk.PhotoImage(resized_art_style_img17)

raw_sart_style_img18 = Image.open("v2garandomasi.png")
resized_art_style_img18 = raw_sart_style_img18.resize((594,306), Image.ANTIALIAS)
art_style_img18 = ImageTk.PhotoImage(resized_art_style_img18)

raw_sart_style_img19 = Image.open("midagit1.png")
resized_art_style_img19 = raw_sart_style_img19.resize((594,306), Image.ANTIALIAS)
art_style_img19 = ImageTk.PhotoImage(resized_art_style_img19)

raw_sart_style_img20 = Image.open("midagit2.png")
resized_art_style_img20 = raw_sart_style_img20.resize((594,306), Image.ANTIALIAS)
art_style_img20 = ImageTk.PhotoImage(resized_art_style_img20)

raw_sart_style_img21 = Image.open("midagit3.png")
resized_art_style_img21 = raw_sart_style_img21.resize((594,306), Image.ANTIALIAS)
art_style_img21 = ImageTk.PhotoImage(resized_art_style_img21)

raw_sart_style_img22 = Image.open("midagit4.png")
resized_art_style_img22 = raw_sart_style_img22.resize((594,306), Image.ANTIALIAS)
art_style_img22 = ImageTk.PhotoImage(resized_art_style_img22)

raw_sart_style_img23 = Image.open("midagit5.png")
resized_art_style_img23 = raw_sart_style_img23.resize((594,306), Image.ANTIALIAS)
art_style_img23 = ImageTk.PhotoImage(resized_art_style_img23)












image_list = [art_style_img1, art_style_img2, art_style_img3, art_style_img4,
              art_style_img5, art_style_img6, art_style_img7, art_style_img8,
              art_style_img9, art_style_img10, art_style_img11, art_style_img12,
              art_style_img13, art_style_img14, art_style_img15, art_style_img16,
              art_style_img17, art_style_img18, art_style_img19, art_style_img20,
              art_style_img21, art_style_img22, art_style_img23]

#failitüübi nupude seaded
selected = IntVar()
fail_type_svg = Radiobutton(window,text='.svg', value='.svg', variable=selected)
fail_type_png = Radiobutton(window,text='.png', value='.png', variable=selected)

#labelite seaded
input_fail_label = Label(window, text = 'Enter file name:')
input_fail_type = Label(window, text = 'Select file type:')
available_art_styles = Label(window, text = 'Available art styles below:')
art_style_label = Label(image = art_style_img1)

input_canvas_height = Label(window, text = 'Enter canvas height:')
input_canvas_width = Label(window, text = 'Enter canvas width:')

#sisendlabeli seaded
fail_name_1 = Entry(window, width = 50)
input_canvas_height_input = Entry(window, width = 20)
input_canvas_width_input = Entry(window, width = 20)



#nupude seaded
button_back = Button(window, text = '<<', command = back, state = DISABLED)
button_forward = Button(window, text = '>>', command = lambda:forward(2))
generate_button = Button(window, text='Generate art', command=generate, fg="white", bg="green")





#see osa ilmutab ekraanile


input_fail_label.grid(column = 0, row = 0)
input_fail_type.grid(column = 0, row = 1)
art_style_label.grid(column = 0, row = 6, columnspan = 3)
available_art_styles.grid(column = 0, row = 5)
input_canvas_height.grid(column = 0, row = 3)
input_canvas_width.grid(column = 0, row = 4)



fail_type_svg.grid(column=1, row=1)
fail_type_png.grid(column=2, row=1)

fail_name_1.grid(column = 1, row = 0)
input_canvas_height_input.grid(column = 1, row = 3)
input_canvas_width_input.grid(column = 1, row = 4)



button_back.grid(column=0, row=15)
button_forward.grid(column=1, row=15)
generate_button.grid(column=5, row=15)

#paneb luubi tööle
window.mainloop()