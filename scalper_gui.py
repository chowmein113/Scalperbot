from tkinter import *
import sys
import ctypes
from pygame import mixer



#increases resolution of window 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
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
    #initialize all frames with paramters chosen
    global List_frame
    side_btn_per_frame=[]
    x=0
    for frame in List_frame:
        
        frame.grid(row=0, column=0, sticky="nsew")
        #in case we wont side button to return
        """side_btn_per_frame.append(Button(frame, text="Side Menu", command=lambda: show_side(), state=NORMAL, bg='#7289da', fg='#ffffff', width=20, height= 5))
        side_btn_per_frame[x].pack(side=LEFT, pady=0,padx=0)
        
        x=x+1"""
        
    
def show_side():
    #bring up side menu with toggling capability
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
        
# ESCAPE KEY SETUP
def press (event):
    show_side()
    



        
#variable declaration        
global past_frame
global current_frame      
global side_menu
global List_frame

        

#window setup
window=Tk()
window.attributes('-fullscreen',False)
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title('Ubihard: ScalperScape')
window.bind("<Escape>",press)
try:
    window.iconbitmap("H:/python/python_repos/scalper_github_repository/tree_of_life.ico")
except:
    pass

"""frame init"""
startup_frame=Frame(window)

main_menu=Frame(window)
website_info=Frame(window)



"""startup_frame"""
current_frame=startup_frame
startup_frame.configure(bg='#2c2f33')
headlabel=Label(startup_frame, text="Add Website", bg='#2c2f33', fg='#ffffff', font=('Times New Roman', 50), width=60, height=2)
##headlabel.grid(row=6, column=5)
headlabel.pack()
##text entry init
textentry=Text(startup_frame, width=60, height=20, font=('Courier', 16), bg='#99aab5', fg='#ffffff')
##textentry.grid(row=0, column=0, pady=20)
textentry.pack(pady=0)
##message background
#button for going to frame1
website_info_transition=Button(startup_frame, text="Go to website monitor", command=lambda: show_frame(website_info), state=NORMAL, bg='#7289da', fg='#ffffff')
website_info_transition.pack(pady=10)
label = Label( startup_frame, text="Answer Box: ",  width=60, height=5, bg='#7289da', font=('Courier', 12), fg='#ffffff')
label.pack(pady=5)
##repeatbutton_loop()
repeatbutton=Button(startup_frame, text="Translate: ", command=main, state=NORMAL, bg='#7289da', fg='#ffffff')
##repeatbutton.grid(row=10, column=5)
#buttstate()
repeatbutton.pack()

##cleartext_loop()
buttonframe=Frame(startup_frame)
buttonframe.pack()
cleartext=Button(buttonframe, text='Clear', command=clear_text, bg='#7289da', fg='#ffffff')
cleartext.grid(row=7, column=5)








#add all frames to list ot bew init
List_frame=[startup_frame, website_info, main_menu]


"""side menu"""
side_menu=Frame(window)
side_State=False
side_menu['bg']='#666666'

side_menu_label=Label(side_menu,text="Side Menu", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=15, height=3 )
side_menu_label.pack()
side_menu.grid(row=0, column=0, sticky='wn', padx=0)
Main_btn=Button(side_menu, text="Main",font=('Times New Roman', 14), command=lambda: show_frame(main_menu), state=NORMAL, bg='#99aab5', fg='#ffffff', width=15, height=0)
Main_btn.pack(padx=40, pady=15, fill=Y)
Website_trackbtn=Button(side_menu, text="Web & Prod Track",font=('Times New Roman', 14), command=lambda: show_frame(website_info), state=NORMAL, bg='#99aab5', fg='#ffffff', width=15, height=0)
Website_trackbtn.pack(padx=40, pady=15, fill=Y)
Add_websitebtn=Button(side_menu, text="Add a Website",font=('Times New Roman', 14), command=lambda: show_frame(startup_frame), state=NORMAL, bg='#99aab5', fg='#ffffff', width=15, height=0)
Add_websitebtn.pack(padx=40, pady=15, fill=Y)


"""main menu frame """
main_menu['bg']='#2c2f33'
#main_menu['bg']=PhotoImage(file='H:/python/python_repos/scalper_github_repository/python_logo.png')
headline = Label(main_menu, text="Scallibrini Bot", bg='#2c2f33', fg='#ffffff', font=('Times New Roman', 50), height=5)
headline.pack(pady=5)
button1 = Button(main_menu, text="Add Websites", bg='#7289da', fg='#ffffff', font=('Times New Roman', 25), width=20, command= lambda: show_frame(startup_frame))
button1.pack(pady=5)
button2 = Button(main_menu, text="Website Monitor", bg='#7289da', fg='#ffffff', font=('Times New Roman', 25), width=20, command=lambda: show_frame(website_info))
button2.pack(pady=5)
button3 = Button(main_menu, text="Exit", bg='#7289da', fg='#ffffff', font=('Times New Roman', 25), width=20,command=window.quit)
button3.pack(pady=5)


"""website_info"""
website_info_title=Label(website_info, text="Website Monitor", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3)

website_info.configure(bg='#2c2f33')
website_info_title.pack()




"""task menu"""
my_menu=Menu(window)
window.config(menu=my_menu)
file_menu=Menu(my_menu)
file_menu2=Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Website info monitor", command=lambda: show_frame(website_info))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_command(label="Side Menu:", command=lambda: show_side())
file_menu.add_command(label="Main", command=lambda: show_frame(main_menu))
file_menu.add_command(label="Add Website", command=lambda: show_frame(startup_frame) )
my_menu.add_cascade(label='View', menu=file_menu2)
file_menu2.add_command(label="Exit Fullscreen", command=lambda: window.attributes('-fullscreen',False))
file_menu2.add_command(label="Fullscreen", command=lambda: window.attributes('-fullscreen',True))


repeat=True
#CREATE AND PUSH AL FRAMES
init_frame();
"""try:
    mixer.init()
    mixer.music.load('H:/python/python_repos/scalper_github_repository/scallibrini_theme.wav')
    mixer.music.play()
except:
    pass"""
mixer.init()
mixer.music.load('H:/python/python_repos/scalper_github_repository/scallibrini_theme.mp3')
mixer.music.play()
#make main_menu visible at start
show_frame(main_menu)
current_frame=main_menu
window.mainloop()