from tkinter import *
import sys
global saves
global linesperobj
linesperobj=3

class website_dataobj():
    webname=""
    weburl=""
    addcart=""
    checkout=""
    gocart = ""
    
    def __init__(self ):
        self.startup()
    def __init__(self, webname, weburl, addcart, gocart, checkout):
        self.weburl = weburl
        self.webname = webname
        self.addcart = addcart
        self.checkout = checkout
        self.gocart = gocart
        self.startup()

    def setweburl(self, weburl):
        self.weburl = weburl    
    def setaddcart(self, addcart):
        self.addcart = addcart
    def setcheckout(self, checkout):
        self.checkout = checkout
    def setwebsite(self, webname):
        self.webname = webname
    def setgotocart(self, gocart):
        self.gocart = gocart

    def getaddcart(self):
        return self.addcart
    def getcheckout(self):
        return self.checkout
    def getwebname(self):
        return self.webname
    def getweburl(self):
        return self.weburl
    def getgocart(self):
        return self.gocart
    def getdatabase(self):
        return self.database
    def startup(self):
        global saves
        self.database=open("scalper_website_info", "r+")
        

    

class login_info():
    first_name= ""
    last_name= ""
    date_of_birth = ""
    address = ""
    city = ""
    state = ""
    zipcode = ""
    phone = ""
    email = ""

class global_variables():
    global saves
    global linesperobj
    g_saves=saves
    g_linesperobj=linesperobj
    def __init__(self, save, lines):
        self.setsaves(save)
        self.setlinesperobj(lines)
        
    def getsaves(self):
        return self.g_saves
    def getlinesperobj(self):
        return self.g_linesperobj
    def setsaves(self, save):
        self.saves=save
    def setlinesperobj(self, lines):
        self.g_linesperobj=lines
        
    

def getsaves(saves):
    listobj=saves.readlines()
    return listobj
def addnewwebsite(website):
    #add new lines of text using write txt function
    #website list contains all string content for new website obj, init it and add to map of website obj
#convert string material from list txt doc to obj
def converttoobj(obj_txt, x):
    """obj_txt is list of strings taken from gui for new website"""
    new_website=website_dataobj()
    
    while x<len(obj_txt):
        #will use '#' in line by itself to mark beginning and end of new website obj to write
        if obj_txt[x]=='#':
            to_delete=0
            x+=1
            
            while obj_txt[x]!='#':
                if 'webname=' in obj_txt[x]:
                    new_website.setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'web_url=' in linesperobj[x]:
                    new_website.setweburl(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'addcart=' in linesperobj[x]:
                    new_website.setaddcart(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'checkout=' in linesperobj[x]:
                    new_website.setcheckout(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'gocart=' in linesperobj[x]:
                    new_website.setgotocart(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                
            return [new_website, x]
def saveobj(website):
    
        
        
    #obj_data_send=[]
    """for s in range(num_start, num_start+linesperobj):
        
        obj_data_send.append(stuff[s])"""
def initconnverttoobj(stuff):
    
    obj_data_send=[]
    obj_txt=getsaves(startup())
    
    
    """s=0
    while s < len(stuff):
        obj_data_send.append(converttoobj(stuff, s))
        s+linesperobj
    return obj_data_send"""
    #^ used this loop back when we thought only 3 items needed per website
    x=0
    while len(obj_txt)!=0:
        obj_tuple=converttoobj(obj_txt, x)
        x=obj_tuple[1]
        
        #will use '#' in line by itself to mark beginning and end of new website obj to write
        """ if obj_txt[x]=='#':
            to_delete=0
            x+=1
            obj_data_send.append(website_dataobj())
            while obj_txt[x]!='#':
                if 'webname=' in obj_txt[x]:
                    obj_data_send[len(obj_data_send)-1].setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'web_url=' in linesperobj[x]:
                    obj_data_send[len(obj_data_send)-1].setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'addcart=' in linesperobj[x]:
                    obj_data_send[len(obj_data_send)-1].setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'checkout=' in linesperobj[x]:
                    obj_data_send[len(obj_data_send)-1].setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1
                if 'gocart=' in linesperobj[x]:
                    obj_data_send[len(obj_data_send)-1].setwebsite(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    x+=1"""
    
        
                    