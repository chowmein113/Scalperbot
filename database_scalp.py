from tkinter import *
import sys
global saves
global linesperobj
linesperobj=3

class website_dataobj():
    website_name=""
    addcartbutton=""
    checkoutbutton=""
    def __init__(self, x, y, z):
        self.setwebsite(x)
        self.setaddcart(y)
        self.setcheckout(z)
        
    def setaddcart(self, x):
        self.addcartbutton=x
    def setcheckout(self, x):
        self.checkoutbutton=x
    def setwebsite(self, x):
        self.website_name=x
    def getaddcart(self):
        return self.addcartbutton
    def getcheckout(self):
        return self.checkoutbutton
    def getwebsite(self):
        return self.website_name
class login_info():
    first_name=""
    last_name=""
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
        
    
def startup():
    global saves
    saves=open("scalper_website_info", "r+")
    return saves
def getsaves(saves):
    listobj=saves.readlines()
    return listobj
def addnewwebsite(website_list):
    global saves
    saves=saves+website_list
    #website list contains all string content for new website obj, init it and add to map of website obj
#convert string material from list txt doc to obj
def converttoobj(stuff, num_start, linesperobj):
    
    obj=website_dataobj(stuff[num_start], stuff[num_start+1], stuff[num_start+2])
    return obj
    #obj_data_send=[]
    """for s in range(num_start, num_start+linesperobj):
        
        obj_data_send.append(stuff[s])"""
def initconnverttoobj(stuff):
    global linesperobj
    obj_data_send=[]
    s=0
    while s < len(stuff):
        obj_data_send.append(converttoobj(stuff, s))
        s+linesperobj
    return obj_data_send