#!/usr/bin/env python3

import shutil 
import os
import javaobj.v2 as javaobj
import sys
import re

#Global dictionaries

Def_serv = {
    5000:"6/80" #http
}

# ISO 3166-1 country number to 2 letter codes
Country_ISO = {
    "4":"AF",
    "8":"AL",
    "12":"DZ",
    "16":"AS",
    "20":"AD",
    "24":"AO",
    "660":"AI",
    "10":"AQ",
    "28":"AG",
    "32":"AR",
    "51":"AM",
    "533":"AW",
    "36":"AU",
    "40":"AT",
    "31":"AZ",
    "44":"BS",
    "48":"BH",
    "50":"BD",
    "52":"BB",
    "112":"BY",
    "56":"BE",
    "84":"BZ",
    "204":"BJ",
    "60":"BM",
    "64":"BT",
    "68":"BO",
    "535":"BQ",
    "70":"BA",
    "72":"BW",
    "74":"BV",
    "76":"BR",
    "86":"IO",
    "96":"BN",
    "100":"BG",
    "854":"BF",
    "108":"BI",
    "132":"CV",
    "116":"KH",
    "120":"CM",
    "124":"CA",
    "136":"KY",
    "140":"CF",
    "148":"TD",
    "152":"CL",
    "156":"CN",
    "162":"CX",
    "166":"CC",
    "170":"CO",
    "174":"KM",
    "180":"CD",
    "178":"CG",
    "184":"CK",
    "188":"CR",
    "191":"HR",
    "192":"CU",
    "531":"CW",
    "196":"CY",
    "203":"CZ",
    "384":"CI",
    "208":"DK",
    "262":"DJ",
    "212":"DM",
    "214":"DO",
    "218":"EC",
    "818":"EG",
    "222":"SV",
    "226":"GQ",
    "232":"ER",
    "233":"EE",
    "748":"SZ",
    "231":"ET",
    "238":"FK",
    "234":"FO",
    "242":"FJ",
    "246":"FI",
    "250":"FR",
    "254":"GF",
    "258":"PF",
    "260":"TF",
    "266":"GA",
    "270":"GM",
    "268":"GE",
    "276":"DE",
    "288":"GH",
    "292":"GI",
    "300":"GR",
    "304":"GL",
    "308":"GD",
    "312":"GP",
    "316":"GU",
    "320":"GT",
    "831":"GG",
    "324":"GN",
    "624":"GW",
    "328":"GY",
    "332":"HT",
    "334":"HM",
    "336":"VA",
    "340":"HN",
    "344":"HK",
    "348":"HU",
    "352":"IS",
    "356":"IN",
    "360":"ID",
    "364":"IR",
    "368":"IQ",
    "372":"IE",
    "833":"IM",
    "376":"IL",
    "380":"IT",
    "388":"JM",
    "392":"JP",
    "832":"JE",
    "400":"JO",
    "398":"KZ",
    "404":"KE",
    "296":"KI",
    "408":"KP",
    "410":"KR",
    "414":"KW",
    "417":"KG",
    "418":"LA",
    "428":"LV",
    "422":"LB",
    "426":"LS",
    "430":"LR",
    "434":"LY",
    "438":"LI",
    "440":"LT",
    "442":"LU",
    "446":"MO",
    "450":"MG",
    "454":"MW",
    "458":"MY",
    "462":"MV",
    "466":"ML",
    "470":"MT",
    "584":"MH",
    "474":"MQ",
    "478":"MR",
    "480":"MU",
    "175":"YT",
    "484":"MX",
    "583":"FM",
    "498":"MD",
    "492":"MC",
    "496":"MN",
    "499":"ME",
    "500":"MS",
    "504":"MA",
    "508":"MZ",
    "104":"MM",
    "516":"NA",
    "520":"NR",
    "524":"NP",
    "528":"NL",
    "540":"NC",
    "554":"NZ",
    "558":"NI",
    "562":"NE",
    "566":"NG",
    "570":"NU",
    "574":"NF",
    "807":"MK",
    "580":"MP",
    "578":"NO",
    "512":"OM",
    "586":"PK",
    "585":"PW",
    "275":"PS",
    "591":"PA",
    "598":"PG",
    "600":"PY",
    "604":"PE",
    "608":"PH",
    "612":"PN",
    "616":"PL",
    "620":"PT",
    "630":"PR",
    "634":"QA",
    "642":"RO",
    "643":"RU",
    "646":"RW",
    "638":"RE",
    "652":"BL",
    "654":"SH",
    "659":"KN",
    "662":"LC",
    "663":"MF",
    "666":"PM",
    "670":"VC",
    "882":"WS",
    "674":"SM",
    "678":"ST",
    "682":"SA",
    "686":"SN",
    "688":"RS",
    "690":"SC",
    "694":"SL",
    "702":"SG",
    "534":"SX",
    "703":"SK",
    "705":"SI",
    "90":"SB",
    "706":"SO",
    "710":"ZA",
    "239":"GS",
    "728":"SS",
    "724":"ES",
    "144":"LK",
    "729":"SD",
    "740":"SR",
    "744":"SJ",
    "752":"SE",
    "756":"CH",
    "760":"SY",
    "158":"TW",
    "762":"TJ",
    "834":"TZ",
    "764":"TH",
    "626":"TL",
    "768":"TG",
    "772":"TK",
    "776":"TO",
    "780":"TT",
    "788":"TN",
    "792":"TR",
    "795":"TM",
    "796":"TC",
    "798":"TV",
    "800":"UG",
    "804":"UA",
    "784":"AE",
    "826":"GB",
    "581":"UM",
    "840":"US",
    "858":"UY",
    "860":"UZ",
    "548":"VU",
    "862":"VE",
    "704":"VN",
    "92":"VG",
    "850":"VI",
    "876":"WF",
    "732":"EH",
    "887":"YE",
    "894":"ZM",
    "716":"ZW",
    "248":"AX",
}

class Objs:
    def __init__(self, id, name):
        self._id = id
        if isinstance(name,str): 
            self._name = name
        else:
            self._name = str(name)
        self._members = []
        self._IsGroup = False

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def members(self):
        return self._members
    
    @members.setter
    def members(self, new_value):
        self._members = new_value

    def append(self, add):
        self._members.append(add)

    @property
    def IsGroup(self):
        return self._IsGroup
    
    @IsGroup.setter
    def IsGroup(self, new_value):
        self._IsGroup = new_value

class sec_Pol:
    def __init__(self, name, action, src, dst,comment):
        #Removing special characters
        self._name = re.sub('[^A-Za-z0-9\s\.]+', '', str(name))
        self._action = action
        self._src = src
        self._dst = dst
        self._src_zone = []
        self._dst_zone = []
        self._src_country = []
        self._dst_country = []
        self._apps = []
        self._srv = []
        self._comment = comment

    @property
    def name(self):
        return self._name

    @property
    def src_zone(self):
        return self._src_zone

    @src_zone.setter
    def src_zone(self, new_value):
        self._src_zone = new_value

    @property
    def dst_zone(self):
        return self._dst_zone

    @dst_zone.setter
    def dst_zone(self, new_value):
        self._dst_zone = new_value

    @property
    def src_country(self):
        return self._src_country

    @property
    def dst_country(self):
        return self._dst_country

    @property
    def apps(self):
        return self._apps

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, new_value):
        self._dst = new_value

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, new_value):
        self._src = new_value

    @property
    def srv(self):
        return self._srv

    @srv.setter
    def srv(self, new_value):
        self._srv = new_value

    @property
    def action(self):
        return self._action

    @property
    def comment(self):
        return self._comment

    def add_L7(self, srv, app, src_country, dst_country):
        self._srv = srv
        self._src_country =src_country
        self._dst_country =dst_country
        self._apps = app     

def sfo_Decompress():
    #Initial file is a .tar.gz with .sfo extention
    fnames = os.listdir()
    src = ""
    for name in fnames:
        if "sfo" in name:
            src = name
    if src == "":
        print("Please include the backup file with .sfo extention in the same folder as the script")
        return
    fname = "EMC_ACP_export_20200803165901"
    dst = fname+".tar.gz"
    os.rename(src, dst)
    shutil.unpack_archive(dst, "export")

    #The configuration is inside a zip file
    fname = "export/CSMExportFile"
    src= fname+".pol"
    dst = fname+".zip"
    os.rename(src, dst)
    shutil.unpack_archive(dst, "config")

def obj_Extract():
    #Creating dictionarry where the key is the .sfo ID and the content is the object itself
    AddGrp = dict()
    Zones = dict()
    Port = dict()
    Srvs = dict()
    with open("config/policy_data_objects_2.obj", "rb") as fd:
        pobj = javaobj.load(fd)
    for a in pobj:
        for b in a.items():
            #print (b[0],b[1].classdesc.name,b[1].name)
            if b[1]:
                if b[1].classdesc.name == "com.cisco.nm.vms.buildingblock.network.NetworkBuildingBlock":
                    obj_id = str(b[0])
                    name = str(b[1].name)
                    #creating object entry
                    AddGrp[obj_id] = Objs(obj_id,name)
                    #print ("set address-group " + str(b[1].name) + " static [ ", end="")
                    for c in b[1].field_data.items():
                        field_names = []
                        if c[0].name== 'com.cisco.nm.vms.buildingblock.BuildingBlock':
                            field_names =c[0].fields_names
                            data = field_names.index("data")
                            reflist = field_names.index("referenceList")
                            k = 0 
                            for e,f in c[1].items():
                                #groups containing addresses or fqdns
                                if k == data:
                                    for g,h in f.field_data.items():
                                        net =g.fields_names.index("networks")
                                        c1 = 0
                                        for i,j in h.items():
                                            if c1 == net:
                                                for l in range(len(j)):
                                                    m = j.pop()
                                                    for n, o in m.field_data.items():
                                                        info = []
                                                        for p,q in o.items():
                                                            info.append(q)
                                                        r = n.fields_names 
                                                        add = str(info[r.index("address")]) 
                                                        mask =  str(info[r.index("mask")])
                                                        if mask == ' ':
                                                            #print("h_" + add, end=" ")
                                                            #print("set address h_" + add +" ip-netmask " + add)
                                                            #adding members to object
                                                            AddGrp[obj_id].append(add)
                                                        else:    
                                                            #print("net_" + add +"_"+mask , end=" ")
                                                            #print("set address net_" + add +"_"+mask+" ip-netmask " + add + '/' + mask )
                                                            #adding members to object
                                                            AddGrp[obj_id].append(add+ '/' + mask )
                                                    pass
                                            c1+=1
                                #Groups containing objects
                                if k == reflist and f!=None:
                                    for g in range(len(f)):
                                        for h in f[g].field_data.items():
                                            for i in h:
                                                if isinstance(i,dict):
                                                    for j, l in i.items():
                                                        if isinstance(l,int):
                                                            AddGrp[obj_id].append(l)
                                k +=1
                #looking for zone names, FilePolicy names, 
                if b[1].classdesc.name == "com.cisco.nm.vms.buildingblock.proxy.EoProxyBuildingBlock":
                    obj_id = str(b[0])
                    for k,v in b[1].field_data.items():
                        if k.name == "com.cisco.nm.vms.buildingblock.BuildingBlock":
                            t = k.fields_names.index("type")
                            n = k.fields_names.index("name")
                            count =0
                            for item in v.items():
                                #if count == t:
                                #    print(item[-1])
                                if count == n:
                                    Zones[obj_id]= item[-1]
                                count +=1
                            pass
                #Extracting services        
                if b[1].classdesc.name == 'com.cisco.nm.vms.buildingblock.port.PortBuildingBlock':
                    obj_id = str(b[0])
                    #creating object entry
                    for k,v in b[1].field_data.items():
                        if k.name == "com.cisco.nm.vms.buildingblock.BuildingBlock":
                            d = k.fields_names.index("data")
                            t = k.fields_names.index("type")
                            s = k.fields_names.index("subtype")
                            na = k.fields_names.index("name")
                            ref = k.fields_names.index("referenceList")
                            l = DicToList(v)
                            #print("")
                            #print(f"data: {l[d]}")
                            #print(f"type: {l[t]}")
                            #print(f"Subtype: {l[s]}")
                            #print(f"Name: {l[na]}")
                            count =0
                            #Case 1: single port object, type: PortObject and subtype: ProtocolPort
                            if l[t] == "PortObject" and l[s] == "ProtocolPort":
                                if l[d].classdesc.name == 'com.cisco.nm.vms.buildingblock.port.PortBuildingBlockData':
                                    for k,v in l[d].field_data.items():
                                        for m, n in v.items():
                                            if n[0].classdesc.name =="com.cisco.nm.vms.buildingblock.port.PortObjectType":
                                                prt = n[0].classdesc.fields_names.index("port")
                                                protocol = n[0].classdesc.fields_names.index("protocol")
                                                for o, p in n[0].field_data.items():
                                                    if o.name ==  "com.cisco.nm.vms.buildingblock.port.PortObjectType":
                                                        values = DicToList(p)
                                                        #print (f"Port: {values[prt]}")
                                                        #print (f"Protocol: {values[protocol]}")
                                                        tmp = str(values[protocol])+"/"+str(values[prt])
                                                        #Adding port/protocol, name and Id  to the service object diict
                                                        Srvs[obj_id] = Objs(obj_id,l[na])
                                                        Srvs[obj_id].append(tmp)
                            elif l[t] == "PortObject" and l[s] == "Group":
                                Srvs[obj_id] = Objs(obj_id,l[na])
                                Srvs[obj_id].IsGroup=True
                                for k in DicToList(l[ref]):
                                    i= 0
                                    for j in k.field_data:
                                        if j.name == 'com.cisco.nm.vms.common.VmsBaseObject':
                                            members = DicToList(DicToList(k.field_data)[i])[0]
                                            Srvs[obj_id].append(members)
                                        i +=1
                            elif l[t] == "PortObject" and l[s] == "ICMPV4":
                                Srvs[obj_id] = Objs(obj_id,"icmp")
                            else:
                                print(f"Warning: Can't translate type: {l[t]}, Subtype: {l[s]},Name: {l[na]}")
                            #Case 3: port/protocol
                            #for item in v.items():
                            #    if count == s:
                            #        Port[obj_id]= item[-1]
                            #    count +=1    
    return AddGrp, Zones, Srvs

def DicToList(d):
    l = []
    try:
        for i in d.items():
            l.append(i[-1])
    except:
        while len(d)>0 :
            l.append(d.pop())     
    return l

def iname(item):
    if item.name:
        return(item.name)
    if item.value:
        return(item.value)
    else:
        return ""

def rule_Extract():
    with open("config/policy_data_policies_3.obj", "rb") as fd:
        pobj = javaobj.load(fd)

    #adding an array that weill contains the objects sec_Pol
    rulebase = []
    for k, v in pobj.items():
            if "UnifiedNGFWRule" in v:
                for a,b in v["UnifiedNGFWRule"].field_data.items():
                    if a.name== "com.cisco.nm.vms.policy.BasePolicyContainer":
                        for c,d in b.items():
                            #print(d, type(d), d.__class__)
                            if isinstance(d, javaobj.beans.JavaArray):
                                for e in d:
                                    for f in e.field_data.items():
                                        if f[0].name == 'com.cisco.nm.vms.policy.BasePolicy':
                                            name = []
                                            field_names =f[0].fields_names
                                            nameindex = field_names.index("_name")
                                            for g,h in f[1].items():
                                                name.append(h)
                                            rulename = name[nameindex]
                                            #print("name : {}".format(rulename))    
                                        if f[0].name == 'com.cisco.nm.vms.fw.common.fwpolicies.rules.AbstractRule':
                                            fields = []
                                            for g,h in f[1].items():
                                                fields.append(h)
                                            #tags
                                            tag = fields[6]
                                            #print("tag : {}".format(tag))   
                                            if fields[6] is None:
                                                for i in fields[4].field_data.items():
                                                    #IPContition, looking for action, src and dst ip
                                                    if i[0].name == 'com.cisco.nm.vms.fw.common.fwpolicies.rules.IPCondition':
                                                        content =[]
                                                        s_index = i[0].fields_names.index("m_sources")
                                                        d_index = i[0].fields_names.index("m_destinations")
                                                        a_index = i[0].fields_names.index("m_ruleAction")
                                                        #f_index = i[0].fields_names.index("m_ifSources")
                                                        #t_index = i[0].fields_names.index("m_ifDestinations")
                                                        for j,l in i[1].items():
                                                            content.append(l)
                                                        #print (type(IPs[3])) 
                                                        source = JavalistToList(content[s_index])  
                                                        destination = JavalistToList(content[d_index])
                                                        #szone = JavalistToList(content[f_index])  
                                                        #dzone = JavalistToList(content[t_index])  
                                                        #print("Action : {}, Source : {}, Destination {}".format(IPs[1],source,destination,fields[3]))
                                                        rulebase.append(sec_Pol(rulename, content[a_index],source,destination,fields[3]))       
                                                    #UnifiedNGFWContion. looking for ports,apps and countries, 
                                                    if i[0].name == 'com.cisco.nm.vms.fwsvc.policy.ngfw.UnifiedNGFWCondition':
                                                        content =[]
                                                        #dport = []
                                                        a_index = i[0].fields_names.index("applications")
                                                        d_index = i[0].fields_names.index("destinationPorts")
                                                        sc_index = i[0].fields_names.index("geoSources")
                                                        dc_index = i[0].fields_names.index("geoDestinations")
                                                        for j,l in i[1].items():
                                                            content.append(l)  
                                                        apps = JavalistToList(content[a_index])
                                                        dport = JavalistToList(content[d_index])
                                                        s_country = JavalistToList(content[sc_index])
                                                        d_country = JavalistToList(content[dc_index])
                                                        #print("Dport : {}".format(dport))
                                                        #Adding service and remaining items to security policy object
                                                        rulebase[-1].add_L7(dport, apps, s_country,d_country)              
                                            #print("comments : {}".format(fields[3]))
                                            #rulebase[-1].add_comment(fields[3])     
                                        if f[0].name == 'com.cisco.nm.vms.fw.common.fwpolicies.rules.ZoneRule':
                                            if fields[6] is None:
                                                content =[]  
                                                szone_index = f[0].fields_names.index('fromZones') 
                                                dzone_index = f[0].fields_names.index('toZones')
                                                for j,l in f[1].items():
                                                    content.append(l)
                                                rulebase[-1].src_zone = JavalistToList(content[dzone_index])   
                                                rulebase[-1].dst_zone = JavalistToList(content[dzone_index]) 
    return rulebase

def JavalistToList(obj):
    l = []
    if isinstance(obj, javaobj.transformers.JavaList):
        if len(obj)>0:
            for tmp in obj:
                l.append(tmp)
    return l

def PrintConfig(addr, zones, rules, serv):
    p = dict()
    #Addresses... renaming members i obj groups
    for k in addr:
        names = []
        for m in addr[k].members:
            #If the member is an int it refers to the ID
            if not isinstance(m, int):
                #networks
                if "/" in m:
                    name = "net_" + m.split("/")[0] + "_" +  m.split("/")[1]
                    names.append(name)
                    print ("set address " + name + " ip-netmask " + m)
                else:
                    name = "h_" + m
                    names.append(name)
                    print ("set address " + name + " ip-netmask " + m)
            #Replacing member d by member name      
            if isinstance(m, int):
                names.append(addr[str(m)].name)
        addr[k].members = names        

    #Address groups
    for k in addr:
        print ("set address-group " + addr[k].name +" static [", end="")
        for m in addr[k].members:
            print (" " +m + " ", end="")
        print("]")
    
    #Services
    for k in serv:
        if serv[k].IsGroup == False and serv[k].name != "icmp":
            prt= serv[k].members[0].split("/")
            name = ""
            if prt[0] == "6":
                name = "tcp_"+prt[1]
                print ("set service " + serv[k].name + " protocol tcp port "+ prt[1]) 
            elif prt[0] =="17":
                name = "udp_"+prt[1]
                print ("set service " + serv[k].name + " protocol udp port "+ prt[1])
    #Service Grups
    for k in serv:
        if serv[k].IsGroup == True:
            print ("set service-group "+serv[k].name+" members [ ", end="")
            for j in serv[k].members:
                print (tr_srv(j, serv), end=" ")
            print("]")
    #policies
    #for k in addr:
    #    print (k, addr[k].name, addr[k].members)
    for rule in rules:
        #replacing rreferences
        src =[]
        dst = []
        srv = []
        szone = []
        dzone =[]
        for v in rule.src:
            src.append(tr_add(v, addr))
        for v in rule.dst:
            dst.append(tr_add(v, addr))
        for v in rule.srv:
            srv.append(tr_srv(v.value, serv))
        for v in rule.src_zone:
            szone.append(zones[str(v)].value) #translating id to zone name
        for v in rule.dst_zone:
            dzone.append(zones[str(v)].value) #translating id to zone name
        rule.src= src
        rule.dst= dst
        rule.srv= srv
        rule.dst_zone = dzone
        rule.src_zone = szone
        #Printing warnings if there's apps
        if len(rule.apps)>0:
            print ("Warning! rule: {}. Contains applications. Manual fix requiered".format(rule.name))
        #Printing warnings if there's src or destination countris
        s_country = []
        d_country = []
        if len(rule.src_country)>0:
            s_country = tr_country(rule.src_country)
        if len(rule.dst_country)>0:
            d_country = tr_country(rule.dst_country)
        print ("set security rules \"" + rule.name +"\" action " +tr_action(rule.action)+ " source "+ replaceAny(rule.src + s_country)+ " destination "+ replaceAny(rule.dst +d_country) + " service " + replaceAny(rule.srv)+ " from "+replaceAny(rule.src_zone)+" to "+replaceAny(rule.dst_zone)+" application any" )
        #print ( rule.name, rule.action, rule.src, rule.dst, rule.srv, rule.comment, rule.apps, rule.src_country, rule.dst_country)

def Enforcer():
    #Order dics where default in 3.7
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    else:
        #print("enforcing")
        if sys.version_info[0] == 3 and sys.version_info[1] < 7:
            raise Exception("Python 3.7 or a more recent version is required.")

def replaceAny(l):
    if len(l)==0:
        return "any"
    else: 
        return "[ "+ " ".join(l) + " ]"  

def tr_action(action):
    if action == 1 or  action == 2:
        return "allow"
    else:
        return "drop"
   
def tr_add(item, addr):
    if isinstance(item.value, int):
        try:
            return addr[str(item)].name
        except KeyError:
            print(f"Warning! Can't translate address:{item}. Using ANY")
            return "any" #
    else:
        v= str(item)
        name = ""
        if "/" in v:
            name = "net_" + v.split("/")[0] + "_" +  v.split("/")[1]
            print ("set address " + name + " ip-netmask " + v)
        else:
            name = "h_" + v
            print ("set address " + name + " ip-netmask " + v)
        return name

def tr_srv(item, srv):
    if isinstance(item, int):
        try:
            return srv[str(item)].name
        except KeyError:
            print("Warning! Can't translate port. Using ANY")
            return "" #
    else:
        prt= str(item).split("/")
        name = ""
        if prt[0] == "6":
            name = "tcp_"+prt[1]
            print ("set service " + name + " protocol tcp port "+ prt[1]) 
        elif prt[0] =="17":
            name = "udp_"+prt[1]
            print ("set service " + name + " protocol udp port "+ prt[1])
        #coverring "all" protocols which is tcp and udp
        elif prt[0] =="-9999": 
            n1 = "tcp_"+prt[1]
            n2 = "udp_"+prt[1]
            name = "tcp_udp_"+prt[1]
            print ("set service " + n1 + " protocol tcp port "+ prt[1])
            print ("set service " + n2 + " protocol udp port "+ prt[1])
            print ("set service-group " + name + " members [ "+ n1 +" " +n2 + " ]")     
        else: 
            print ("warning... couldn't translate protocol/port: {}. Add the service manually".format(prt))
        return name

def tr_country(countries):
    r = []
    for c in countries:
        country = c.value
        if isinstance(country, str) and country.startswith("c|"):
            cnum = country.split("|")[-1]
            if cnum in Country_ISO.keys():
                r.append(Country_ISO[cnum])
            else:
                print("Warning: can't translate country: {} , manual fix for the policy below is requiered".format(country) )     
        else:
            print("Warning: can't translate country: {} , manual fix for the policy below is requiered".format(country) )    
    return r

if __name__ == "__main__":
    Enforcer()
    sfo_Decompress()
    AddGrp, Zones, Port = obj_Extract()
    PrintConfig(AddGrp, Zones, rule_Extract(), Port)
