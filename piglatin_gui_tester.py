from tkinter import *
import sys
counter=1
def engtopig(x):
    
    list=x.split()
    for char in list:
        og=char
        if char[0] in "1234567890!@#$%^&*()-_+=:;{[}]|\<,>.?/}":
            char=char
        elif char[0] in "AEIOUaeiou":
            char=char+"yay"
        else:
            ##repeat=true
            ##while(repeat):
            counter=0
            while char[counter] not in "AEIOUaeiou":
                counter=counter+1
            constant=""
            for x in range(int(counter)):
                constant=constant+char[x]
                    
            final = char.replace(constant, '')
            char=final
                
            char=char+constant+"ay"
        i=list.index(og)
        list[i]=char
    total=''
    for word in list:
        total=total+' '+word
    return total
                
                
                    
                

def main():
    global counter
    """if counter<=1:
        line=textentry.get(1.0 , END)
    else:"""
    line=textentry.get(floattotextline() , END)
    repeat=False
    
    ##repeat=True
    ##while(repeat == True):
    ##line=input("What should I translate? : "  )
    list=engtopig(line)
    ##print(list)
    ##loop=input("translate again? : ")
        
    ##if loop == "yes":
        ## repeat=True
    ##else:
        ##repeat=False
    repeat=True
    
    textentry.insert(INSERT,"\n"+ list)
    
    label.config(text=list+'\n'+'counter: '+floattotextline())
    
    counterstat()
    ##var.set(list)
    ##label = Message( root, text=var, relief=RAISED, justify=LEFT )
    ##label=Label(root, text=list)
    ##label.grid(row=65, column=5)
    ##label.pack()
def floattotextline():
    global counter
    y=int(counter)
    char=str(y)+'.0'
    return char
def counterstat():
    global counter
    delta=float(textentry.index(INSERT))
    counter+=delta+1
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
    

root=Tk()
root.configure(bg='#2c2f33')

root.geometry('760x760')
root.title('Piglatin Translator')
#root.iconbitmap("C:/Users/chowm/Desktop/scalper_repo_test.ico")

repeat=True
##headlabel__init__()
headlabel=Label(root, text="Piglatin Translator", bg='#7289da', fg='#ffffff', font=('Times New Roman', 16), width=60, height=3)
##headlabel.grid(row=6, column=5)
headlabel.pack()
##text entry init
textentry=Text(root, width=60, height=20, font=('Courier', 16), bg='#99aab5', fg='#ffffff')
##textentry.grid(row=0, column=0, pady=20)
textentry.pack(pady=15)
##message background

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

root.mainloop()