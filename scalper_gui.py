from tkinter import *
import sys
counter=1

def main():
    global counter
    """if counter<=1:
        line=textentry.get(1.0 , END)
    else:"""
   
    
    ##repeat=True
    ##while(repeat == True):
    ##line=input("What should I translate? : "  )
   
    ##print(list)
    ##loop=input("translate again? : ")
        
    ##if loop == "yes":
        ## repeat=True
    ##else:
        ##repeat=False
    repeat=True
    
    textentry.insert(INSERT,"\n"+ list)
    
    label.config(text=list+'\n'+'counter: ')
    
    
    ##var.set(list)
    ##label = Message( root, text=var, relief=RAISED, justify=LEFT )
    ##label=Label(root, text=list)
    ##label.grid(row=65, column=5)
    ##label.pack()

def buttstate():
    if repeat==True:
        repeatbutton['state']=NORMAL
    else:
        repeatbutton['state']=DISABLED
def clear_text():
    global counter
    textentry.delete(1.0, END)
    counter=1
    label['text']="Counter: "+counter
"""def headlabel__init__():
    headlabel=Label(root, text="Piglatin Translator")
    headlabel.grid(row=6, column=5)"""
    
"""def repeatbutton_loop():
    repeatbutton=Button(root, text="Translate: ", command=main(textentry.get(1.0, END)), state=buttstate())
    repeatbutton.grid(row=10, column=5)"""
    
"""def cleartext_loop():
    cleartext=Button(root, text='Clear')
    cleartext.grid(row=7, column=5)"""
 #showing frame
def show_frame(frame):
    global List_frame
    global current_frame
    global past_frame
    
        
    frame.tkraise()
    past_frame=current_frame
    current_frame=frame
    
    """for frame in not List_frame:
        frame.grid_remove()
    frame.grid(row=0, column=0, sticky="nsew")"""
def init_frame():
    global List_frame
    for frame in List_frame:
        
        frame.grid(row=0, column=0, sticky="nsew")
def show_side():
    global side_menu
    global current_frame
    global past_frame
    if current_frame!=side_menu:
        side_menu.tkraise()
        past_frame=current_frame
        current_frame=side_menu
        
    else:
        past_frame.tkraise()
        current_frame=past_frame
        past_frame=side_menu
        
        
        

        


window=Tk()
root=Frame(window)
#root.state('zoomed')
global past_frame
global current_frame
current_frame=root
global side_menu
root.configure(bg='#2c2f33')
window.attributes('-fullscreen',False)

window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title('Ubihard: ScalperScape')
try:
    window.iconbitmap("C:/Users/chowm/Desktop/scalper_repo_test/tree_of_life.ico")
except:
    pass

main_menu=Frame(window)
frame1=Frame(window)
global List_frame
List_frame=[root, frame1, main_menu]
#side menu
side_menu=Frame(window)
side_State=False
side_menu['bg']='#666666'
window.bind('<s>', lambda: show_side())
side_menu_label=Label(side_menu,text="Side Menu", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=15, height=3 )
side_menu_label.pack()
side_menu.grid(row=0, column=0, sticky='wn', padx=20)



#main menu frame 
main_menu.configure(bg='#2c2f33')
mainheadlabel=Label(main_menu, text="Monopoly Bot", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3)
mainheadlabel.pack()
add_website=Button(main_menu, text="Add Website", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3,command= lambda: show_frame(root))
add_website.pack(ipadx=30, ipady=20, side=TOP)
website_monitor=Button(main_menu, text="Website Monitor", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3,command= lambda: show_frame(frame1))
website_monitor.pack(ipadx=30, ipady=20, side=TOP)
exit_out=Button(main_menu, text="Exit",bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3,command=window.quit )
exit_out.pack(side=BOTTOM)
#Frame 1 for website information
frame1_title=Label(frame1, text="Website Monitor", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3)

frame1.configure(bg='#2c2f33')
frame1_title.pack()

init_frame();
#menu
my_menu=Menu(window)
window.config(menu=my_menu)
file_menu=Menu(my_menu)
file_menu2=Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Website info monitor", command=lambda: show_frame(frame1))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_command(label="Side Menu:", command=lambda: show_side())
file_menu.add_command(label="Main", command=lambda: show_frame(main_menu))
file_menu.add_command(label="Add Website", command=lambda: show_frame(root) )
my_menu.add_cascade(label='View', menu=file_menu2)
file_menu2.add_command(label="Exit Fullscreen", command=lambda: window.attributes('-fullscreen',False))
file_menu2.add_command(label="Fullscreen", command=lambda: window.attributes('-fullscreen',True))


repeat=True

"""root stuff"""
##headlabel__init__()
headlabel=Label(root, text="Add Website", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3)
##headlabel.grid(row=6, column=5)
headlabel.pack()
##text entry init
textentry=Text(root, width=60, height=20, font=('Courier', 16), bg='#99aab5', fg='#ffffff')
##textentry.grid(row=0, column=0, pady=20)
textentry.pack(pady=15)
##message background
#button for going to frame1
frame1_transition=Button(root, text="Go to website monitor", command=show_frame(frame1), state=NORMAL, bg='#7289da', fg='#ffffff')
label = Label( root, text="Answer Box: ",  width=60, height=5, bg='#7289da', font=('Courier', 12), fg='#ffffff')
label.pack(pady=20)
##repeatbutton_loop()
repeatbutton=Button(root, text="Translate: ", command=main, state=NORMAL, bg='#7289da', fg='#ffffff')
##repeatbutton.grid(row=10, column=5)
buttstate()
repeatbutton.pack()

##cleartext_loop()
buttonframe=Frame(root)
buttonframe.pack()
cleartext=Button(buttonframe, text='Clear', command=clear_text, bg='#7289da', fg='#ffffff')
cleartext.grid(row=7, column=5)
show_frame(main_menu)
current_frame=main_menu
root.mainloop()