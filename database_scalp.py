from tkinter import *
import sys

global linesperobj
linesperobj = 3





def converttoobj(new_website, obj_txt, index):
    x = index
    
    
    
    if obj_txt[x] == '#': #init variable to start parsing through website info sets which are lines of text to be used as website objects
            to_delete = 0
            procedure_step = 0
            x += 1 # x is line indicator of text files obj, obj_txt
            
            while obj_txt[x]!='#': #skips over 'x', indicating new website info set
                if 'webname=' in obj_txt[x]:
                    new_website.setwebname(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    #after the equal, will increment by one to read actual text information
                    new_website.procedure[procedure_step] = new_website.getwebname()
                    procedure_step += 1
                    x += 1
                if 'web_url=' in obj_txt[x]:
                    new_website.setweburl(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    new_website.procedure[procedure_step] = new_website.getweburl()
                    procedure_step += 1
                    x += 1
                if 'addcart=' in obj_txt[x]:
                    new_website.setaddcart(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    new_website.procedure[procedure_step] = new_website.getaddcart()
                    procedure_step += 1
                    x += 1
                if 'checkout=' in obj_txt[x]:
                    new_website.setcheckout(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    new_website.procedure[procedure_step] = new_website.getcheckout()
                    procedure_step += 1
                    x += 1
                if 'gocart=' in obj_txt[x]:
                    new_website.setgotocart(obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])])
                    new_website.procedure[procedure_step] = new_website.getgocart()
                    procedure_step += 1
                    x += 1
                else:
                    new_website.procedure[procedure_step] = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])]
                    procedure_step += 1
                    
                
            #return [new_website, x]
            index = x
            return new_website
#def saveobj(website):
   
    
        
def convertalltoobj(obj_txt, x):
    """obj_txt is list of strings taken from gui for new website"""
    
    websites = {}
    while x  <len(obj_txt):
        try:
            obj_txt[x] 
        except:
            break
        new_website = converttoobj(website_dataobj(), obj_txt, x)
        websites[new_website.getwebname()] = new_website
    return websites
        
        #will use '#' in line by itself to mark beginning and end of new website obj to write
       
class local_database():
    def __init__(self, file_path = "", handler = ""):
        self.saves = None
        self.websites = None
        self.file_path = file_path
        self.handler = handler
        self.assertion()
        
    def get_file(self):
        self.assertion()
        return self.saves
    def get_text(self):
        self.assertion()
        return self.saves.readlines()
    def collect_websites(self):
        self.websites = convertalltoobj(self.get_text(), 0)
    def save(self):
        self.assertion()
        self.saves.close()
        self.saves = None
    def open(self):
        self.assertion()
    def assertion(self):
        if self.saves is None:
            self.saves = open(self.file_path, self.handler) 
        if self.websites is None:
            self.collect_websites()
    def get_website_objs(self):
        self.assertion()
        return self.websites
    def write(self, website_obj):
        self.handler = "r+"
        self.assertion()
        self.saves.write('\n#')
        procedure = website_obj.dump()
        for i in range(len(procedure)):
            self.saves.write('\n' + website_obj[i].name + "=" + website_obj[i].element)
        
        
        
saves = local_database("website_info.txt", "r+")

class website_element():
    def __init__(self, element = '', name = '', type = ''):
        self.element = element
        self.name = name
        self.type = type 
    @property
    def element(self):
        return self.element
    @element.setter
    def element(self, element):
        self.element = element
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name):
        self.name = name
    @property
    def type(self):
        return self.type
    @type.setter
    def type(self, type):
        self.type = type 
class website_dataobj():
    webname = ""
    weburl = ""
    addcart = ""
    checkout = ""
    gocart = ""
    procedure = []
    
    
    def __init__(self, webname = '', weburl = '', addcart = '', gocart = '', checkout = ''):
        self.weburl = website_element(weburl, "weburl", "url") 
        self.procedure.append(self.weburl)
        self.webname = website_element(webname, "webname", "name")
        self.procedure.append(self.webname)
        self.addcart = website_element(addcart, "addcart", "xpath")
        self.procedure.append(self.addcart)
        self.checkout = website_element(checkout, "checkout", "xpath")
        self.procedure.append(self.checkout)
        self.gocart = website_element(gocart, "gocart", "xpath")
        self.procedure.append(self.gocart)
        starter = self.procedure
        for i in range(len(starter)):
            self.procedure[i] = starter[i]
            
    def custom_command(self, lst_website_elements):
        """for websites that differ from the default, input commands of website elements based on order from lst_website_elements, selenium will then iterate 
        through self.procedure and do a comman procedure based on website elements type, be it xpath, url, keys for send_keys, etc"""
        self.procedure.clear()
        for i in lst_website_elements:
            self.procedure[i] = lst_website_elements[i]
    def insert_command(self, procedure_step, website_element):
        self.procedure.insert(procedure_step, website_element)
            
    def setweburl(self, weburl):
        self.weburl = weburl    
    def setaddcart(self, addcart):
        self.addcart = addcart
    def setcheckout(self, checkout):
        self.checkout = checkout
    def setwebname(self, webname):
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
    @property
    def procedure(self):
        return self.procedure
    @procedure.setter
    def procedure(self, index, value):
        self.procedure[index] = value
    
        
    """def getdatabase(self):
        return self.database"""
    """def startup(self):
        global saves
        self.database = open("scalper_website_info", "r+")"""
        

    

class login_info():
    first_name = ""
    last_name = ""
    date_of_birth = ""
    address = ""
    city = ""
    state = ""
    zipcode = ""
    phone = ""
    email = ""
    
    def __init__(self, first_name = "", last_name = "", date_of_birth = "", address = "", city = "", state = "", zipcode = "", phone = "", email = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.email = email
        

class global_variables():
    """global saves
    global linesperobj
    g_saves = saves
    g_linesperobj=linesperobj"""
    def __init__(self, save, lines):
        self.setsaves(save)
        self.setlinesperobj(lines)
        
    def getsaves(self):
        return self.saves
    def getlinesperobj(self):
        return self.g_linesperobj
    def setsaves(self, save):
        self.saves=save
    def setlinesperobj(self, lines):
        self.g_linesperobj=lines
        
    

def getsaves(saves):
    listobj = saves.readlines()
    return listobj
#def addnewwebsite(website):
    #add new lines of text using write txt function
    #website list contains all string content for new website obj, init it and add to map of website obj
#convert string material from list txt doc to obj
#def save_to_txt(website_obj, saves):