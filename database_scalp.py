from tkinter import *
import sys

global linesperobj
linesperobj = 3





def converttoobj(new_website, obj_txt):
    #x = index
    obj_txt
    x = 0
    print("phase 1")
    
    if obj_txt[x].split()[0] == '#': 
        print("phase 2")
        obj_txt.pop(0)#init variable to start parsing through website info sets which are lines of text to be used as website objects
        print(obj_txt)
        """to_delete = 0
        procedure_step = 0"""
            #x += 1 # x is line indicator of text files obj, obj_txt
            
        while obj_txt[x].split()[0] != '#': 
            print('repeat phase')
            #skips over 'x', indicating new website info set
            if 'webname=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                holder = " ".join(holder)
                obj_txt.pop(0)
                packer = website_element(holder, holder, "webname")
                
                new_website.setwebname(packer)
                #after the equal, will increment by one to read actual text information
                #new_website.procedure.append(new_website.getwebname())
                """procedure_step += 1
                x += 1"""
            if 'web_url=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setweburl(packer)
                new_website.append_command(new_website.getweburl())
                """procedure_step += 1
                x += 1"""
            if 'addcart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setaddcart(packer)
                new_website.append_command(new_website.getaddcart())
                """procedure_step += 1
                x += 1"""
            if 'checkout=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setcheckout(packer)
                new_website.append_command(new_website.getcheckout())
                """procedure_step += 1
                x += 1"""
            if 'gocart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setgotocart(packer)
                new_website.append_command(new_website.getgocart())
                """procedure_step += 1
                x += 1"""
            if "send_key=" in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                need_clear = True if holder[-1] == 'true' else False
                holder = holder[0:-1]
                obj_txt.pop(0)
                keys = holder[1:-1]
                space = " "
                keys = space.join(keys)
                packer = website_element(holder[0], keys, holder[-1])
                new_website.append_command(packer)
            
            else:
                holder = obj_txt[x].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.append_command(packer)
                """procedure_step += 1"""
            try:
                if len(obj_txt[x].split()[0].split()) <= 0:
                    break
            except:
                break
                
            
        #return [new_website, x]
        #index = x
        #wobj_txt = obj_txt
        print('leftover ', obj_txt, "\n", [i.name for i in new_website.getprocedure()])
        return new_website
#def saveobj(website):
   
    
        
def convertalltoobj(obj_txt):
    """obj_txt is list of strings taken from gui for new website"""
    copy_obj_txt = obj_txt[:]
    print('copy ', copy_obj_txt)
    print('og ', obj_txt)
    websites = {}
    while len(copy_obj_txt) > 0 and len(copy_obj_txt[0].split()) > 0:
        print("convert all loop")
        new_website = website_dataobj()
        new_website = converttoobj(new_website, copy_obj_txt)
        websites[new_website.getwebname().name] = new_website 
        print("done with loop")
    print("done")
    print('copyf ', copy_obj_txt)
    print('ogf ', obj_txt) 
    return websites
        
        #will use '#' in line by itself to mark beginning and end of new website obj to write
       
       
class local_database():
    def __init__(self, file_path = "", handler = ""):
        
        
        self._file_path = file_path
        self._handler = handler
        self._saves = open(self._file_path, self._handler)
        self._text = self.saves.readlines()
        self.collect_websites()
        #self.assertion()
        
    def get_file(self):
        #self.assertion()
        return self.saves
    def get_text(self):
        
        return self._text
    def collect_websites(self):
        self._websites = convertalltoobj(self.get_text())
    def close(self):
        
        self._handler = "r+"
        self.saves = None
        self.assertion()
        self.saves.truncate(0)
        
        
        for i in self.get_website_objs():
            self.saves.write('#\n')
            for y in i.getprocedure():
                if y.name in i.track_variables:
                    self.saves.write(y.name + "=" + y.write_self() + '\n')
                elif y.type == 'xpath_sendkey':
                    self.saves.write(y.type + "=" + y.write_self() + y.need_clear + '\n')
                else:
                    self.saves.write(y.write_self()+'\n')
        self.saves.close()
        self.saves = None
        self._text = None
        self._websites = None
    def open(self):
        self.assertion()
    def assertion(self):
        if self.saves is None:
            self.saves = open(self._file_path, self._handler) 
        if self._text == None or []:
            self._text = self.get_text()
        if self._websites is None:
            self.collect_websites()
    def get_website_objs(self):
        self.assertion()
        return self._websites
    @property
    def saves(self):
        return self._saves
    @saves.setter
    def saves(self, saver):
        self.saves = saver
    
    """need to fix write for rewriting file from scratch when 
    saving current websites and how to delete website from txt"""
    def write(self, website_obj):
        
        self._handler = "r+"
        self.saves = None
        self.assertion()
        self.get_website_objs()[website_obj.getwebname()] = website_obj
        self.close()
        self.open()
        
        
        
        
        
#saves = local_database("website_info.txt", "r+")

class website_element():
    def __init__(self, element = '', name = '', type = '', need_clear = False):
        self._element = element
        self._name = name
        self._type = type 
        self._need_clear = need_clear
    
    @property
    def element(self):
        return self._element
    @element.setter
    def element(self, element):
        self._element = element
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type
    @property
    def need_clear(self):
        return self._need_clear
    @need_clear.setter
    def need_clear(self, bool):
        self._need_clear = bool
    def write_self(self):
        return self.element + self.name + self.type
class website_dataobj():
    webname = ""
    weburl = ""
    addcart = ""
    checkout = ""
    gocart = ""
    procedure = []
    
    
    def __init__(self, webname = '', weburl = '', addcart = '', gocart = '', checkout = ''):
        self._track_variables = []
        self._weburl = website_element(weburl, "weburl", "url") 
        self._track_variables.append(self.getweburl().name)
        self._webname = website_element(webname, "webname", "name")
        
        self._addcart = website_element(addcart, "addcart", "xpath")
        self._track_variables.append(self.getaddcart().name)
        self._checkout = website_element(checkout, "checkout", "xpath")
        self._track_variables.append(self.getcheckout().name)
        self._gocart = website_element(gocart, "gocart", "xpath")
        self._track_variables.append(self.getgocart().name)
        self._procedure = []
        
            
    def custom_command(self, lst_website_elements):
        """for websites that differ from the default, input commands of website elements based on order from lst_website_elements, selenium will then iterate 
        through self.procedure and do a comman procedure based on website elements type, be it xpath, url, keys for send_keys, etc"""
        self.getprocedure().clear()
        for i in lst_website_elements:
            self.getprocedure()[i] = lst_website_elements[i]
    def append_command(self, website_element):
        self.getprocedure().append(website_element)
            
    def setweburl(self, weburl):
        self._weburl = weburl    
    def setaddcart(self, addcart):
        self._addcart = addcart
    def setcheckout(self, checkout):
        self._checkout = checkout
    def setwebname(self, webname):
        self._webname = webname
    def setgotocart(self, gocart):
        self._gocart = gocart

    def getaddcart(self):
        return self._addcart
    def getcheckout(self):
        return self._checkout
    def getwebname(self):
        return self._webname
    def getweburl(self):
        return self._weburl
    def getgocart(self):
        return self._gocart
    def getprocedure(self):
        return self._procedure
    def setprocedure(self, procedure):
        self._procedure = procedure
    @property
    def track_variables(self):
        return self._track_variables
    @track_variables.setter
    def track_variables(self, lst):
        self._track_variables = lst
    
        
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
"""beta = open(r"local_saves.txt", "r+")


gamma = beta.readlines()
dict = convertalltoobj(gamma)
print(dict)"""