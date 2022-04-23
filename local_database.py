from tkinter import *
import sys
import os
import json

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
            elif 'web_url=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setweburl(packer)
                new_website.append_command(new_website.getweburl())
                """procedure_step += 1
                x += 1"""
            elif 'addcart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setaddcart(packer)
                new_website.append_command(new_website.getaddcart())
                """procedure_step += 1
                x += 1"""
            elif 'checkout=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setcheckout(packer)
                new_website.append_command(new_website.getcheckout())
                """procedure_step += 1
                x += 1"""
            elif 'gocart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setgotocart(packer)
                new_website.append_command(new_website.getgocart())
                """procedure_step += 1
                x += 1"""
            elif "send_key=" in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                needclear = True if holder[-1] == 'true' else False
                holder = holder[0:-1]
                obj_txt.pop(0)
                keys = holder[1:-1]
                space = " "
                keys = space.join(keys)
                packer = website_element(holder[0], keys, holder[-1])
                packer.need_clear = needclear
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

"""given a dictionary and a website object"""   
def convert_dict_to_obj(dict, new_website):
    print('dict')
    for i in dict:
        print(i)
        if 'webname' in i:
                holder = dict.get(i).split()
                packer = website_element(holder[0], holder[0], "webname")
                
                new_website.setwebname(packer)
                #after the equal, will increment by one to read actual text information
                #new_website.procedure.append(new_website.getwebname())
                """procedure_step += 1
                x += 1"""
        elif 'web_url' in i:
                holder = dict.get(i).split()
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setweburl(packer)
                new_website.append_command(new_website.getweburl())
                """procedure_step += 1
                x += 1"""
        elif 'addcart' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setaddcart(packer)
            new_website.append_command(new_website.getaddcart())
            """procedure_step += 1
            x += 1"""
        elif 'checkout' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setcheckout(packer)
            new_website.append_command(new_website.getcheckout())
            """procedure_step += 1
            x += 1"""
        elif 'gocart' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setgotocart(packer)
            new_website.append_command(new_website.getgocart())
            """procedure_step += 1
            x += 1"""
        elif "send_key" in i:
            holder = dict.get(i).split()
            needclear = True if holder[-1] == 'true' else False
            holder = holder[0:-1]
            
            keys = holder[1:-1]
            space = " "
            keys = space.join(keys)
            packer = website_element(holder[0], keys, holder[-1])
            packer.need_clear = needclear
            new_website.append_command(packer)
        
        else:
            holder = dict.get(i).split()
            print(holder)
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.append_command(packer)
            """procedure_step += 1"""
    return new_website
        
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
        
        # file path of text file
        self._file_path = file_path
        # mode to open text file in (a, w, r, r+)
        self._handler = handler 
        # reference to text file
        self._saves = open(self._file_path, self._handler)
        # turns next file into list a strings line by line
        self._text = self.saves.readlines()
        # creates dictionary of website objects from _text
        self.collect_websites()
        #self.assertion()
        
    def get_file(self):
        #self.assertion()
        return self.saves
    def get_text(self):
        
        return self._text
    
    "loads website objs into dictionary"
    def collect_websites(self):
        self.set_website_objs(convertalltoobj(self.get_text()))
        
    """write my current dictionary of all website objs to a JSON file"""  
    def write_to_json(self, json_file):
        self.assertion()
        with open(json_file, 'w') as f:
            print('[', file = f)
        for i in [self.get_website_objs().get(i) for i in self.get_website_objs()]:
            with open(json_file, 'a') as f:
                
                json.dump(i.to_json_dict(), f, indent = 4)
                print(",\n", end = '', file = f)
        with open(json_file, 'a') as f:
            #0 is first of char in doc, 2 is end of document
            f.seek(0, 2)
            #f.tell tells where the cursor is currently at
            f.seek(f.tell() - 3, os.SEEK_SET)
            f.truncate()
            print('\n]', file = f)
            
    """open a json file to load json website objs into my dictionary"""
    def json_to_obj(self, json_file):
        with open(json_file) as f:
            x = json.load(f)
            d = {}
            for i in x:
                temp_website_holder = convert_dict_to_obj(i, website_dataobj())
                d[temp_website_holder.getwebname().name] = temp_website_holder
            self.set_website_objs(d)
            
        
            
    def close(self):
        self.saves = open(os.path.dirname(__file__) + r"/test_saves.txt", 'r+')
        """self._handler = "r+"
        self.saves = None
        self.assertion()
        self.saves.truncate(0)"""
        
        
        
        for i in self.get_website_objs():
            self.saves.write('#\n')
            self.saves.write('webname=' + i + '\n')
            print('closing')
            print([i.name for i in self.get_website_objs()[i].getprocedure()])
            for y in self.get_website_objs()[i].getprocedure():
                if y.name in self.get_website_objs()[i].track_variables:
                    self.saves.write(y.name + "=" + y.write_self() + '\n')
                elif y.type == 'xpath_sendkey':
                    self.saves.write("send_key" + "=" + y.write_self() + ' ' + y.need_clear_to_str() + '\n')
                else:
                    self.saves.write(y.write_self()+'\n')
        self.saves.close()
        self.saves = None
        self._text = None
        self._websites = None
    def open(self):
        self.assertion()
    def assertion(self):
        if self.saves is None or []:
            self.saves = open(self._file_path, self._handler) 
        if self._text == None or []:
            self._text = self.saves.readlines()
        if self.get_website_objs() is None or []:
            self.collect_websites()
    def get_website_objs(self):
        
        return self._websites
    def set_website_objs(self, websites):
        self._websites = websites
    @property
    def saves(self): 
        return self._saves
    @saves.setter 
    def saves(self, saver):
        self._saves = saver
    
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
    """glorified xpath, allows us to differentiate between 
    xpaths so our code knows what to do for each given xpath"""
    def __init__(self, element = '', name = '', type = '', need_clear = False):
        # element is xpath
        self._element = element
        # name of xpath and name can be used by send_key if element is a xpath_sendkey
        self._name = name
        # type of xpath; is it a send key or a regular xpath
        self._type = type 
        # if im an xpath_sendkey do i need to clear text box before inputting text?                      222
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
    def need_clear_to_str(self):
        return 'true' if self.need_clear == True else 'false'
    def write_self(self):
        return ' '.join([self.element, self.name, self.type])


class website_dataobj():
    """an object that hold a website information, has the url, name, and xpath query for shopping process"""
    webname = ""
    weburl = ""
    addcart = ""
    checkout = ""
    gocart = ""
    procedure = []
    
    
    def __init__(self, webname = '', weburl = '', addcart = '', gocart = '', checkout = ''):
        self._track_variables = ['web_url', 'addcart', 'gocart', 'webname', 'checkout']
        self._weburl = website_element(weburl, "web_url", "url") 
        self._track_variables.append(self.getweburl().name)
        self._webname = website_element(webname, "webname", "name")
        
        self._addcart = website_element(addcart, "addcart", "xpath")
        self._track_variables.append(self.getaddcart().name)
        self._checkout = website_element(checkout, "checkout", "xpath")
        self._track_variables.append(self.getcheckout().name)
        self._gocart = website_element(gocart, "gocart", "xpath")
        self._track_variables.append(self.getgocart().name)
        # array to hold query of website elements
        self._procedure = []
        
            
    def custom_command(self, lst_website_elements):
        """for websites that differ from the default, input commands of website elements based on order from lst_website_elements, selenium will then iterate 
        through self.procedure and do a command procedure based on website elements type, be it xpath, url, keys for send_keys, etc"""
        self.getprocedure().clear()
        for i in lst_website_elements:
            self.getprocedure()[i] = lst_website_elements[i]
    def append_command(self, website_element):
        self.getprocedure().append(website_element)
    def to_json_dict(self):
        data = {}
        data['webname='] = self.getwebname().name
        print('json dict time *******')
        print(self.getprocedure())
        for y in self.getprocedure():
                if y.name in self.track_variables:
                    data[y.name + "="] = y.write_self() + '\n'
                elif y.type == 'xpath_sendkey':
                    data[y.name+'send_key='] = y.write_self() + ' ' + y.need_clear_to_str() + '\n'
                else:
                    data[y.name] = y.write_self()+'\n'
        print(data)
        return data 
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
        

    
"""possibly a class to use for login information to keep it separate from text saves"""
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