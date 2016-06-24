#coding:utf-8
import xmlparser
class group_info:
    def __init__(self):
        self.group_num = 0
        self.service_set = []
    def set_num(self, num):
        self.group_num = num
    def allinclude(self):
        for node in xmlparser.getallnode():
            self.service_set.append(node)
    def include(self, node):
        self.service_set.append(node)
    def exclude(self, node):
        self.service_set.remove(node)

def getfile():
    gpfile = open("groupinfo",'r')
    gpfileread = []
    line = gpfile.readline()
    while(line != ""):
        if line[0]!='#':
            gpfileread.append(line)
        line = gpfile.readline()
    return gpfileread
    
def get_group_info(l_getfile):
    l_group_info = []
    new_gi = group_info()
    while(l_getfile):        
        line = l_getfile.pop(0)
        entry = line.split('=')[0]
        value = line.split('=')[1][:-1:]
        if entry == 'group':
            if(new_gi.service_set.__len__()!=0):
                l_group_info.append(new_gi)
            new_gi = group_info()
            new_gi.group_num = int(value)
        elif entry == 'include':
            if value == "all":
                new_gi.allinclude()
            else:
                l_nodes = value.split(',')
                for node in l_nodes:
                    new_gi.include(node)
        elif entry == 'exclude':
            new_gi.allinclude()
            l_nodes = value.split(',')
            for node in l_nodes:
                new_gi.exclude(node)
        else:
            print "ERROR NAME"
    l_group_info.append(new_gi)          
    return l_group_info

l_group_info = get_group_info(getfile())
