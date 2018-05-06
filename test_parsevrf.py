#utility library for get data from ios config
from ciscoconfparse import CiscoConfParse#Function check ios

VRF_NAME = "name";
RD = "rd";
RT_EXPORT = "rt-export";

#function get list of match line
def get_match_lines():
 return 0
#standard vrf attributes
def ios_vrf_default_attrib():
 return {VRF_NAME:'',RD:'',RT_EXPORT:[],'rt-import':[],'ex-map':[],'im-map':[]}

#function check ios config file has vrf config
def ios_has_vrf(conf_file):
 if not CiscoConfParse(conf_file).find_parents_w_child("^ip\svrf\s", "rd"):
  #print parse.ioscfg
  return False 
 return True

#function get list vrf on ios config
def ios_get_list_vrf(conf_file):
 def_list = []
 if ios_has_vrf(conf_file):
  return {x.replace('ip vrf ', '')for x in CiscoConfParse(conf_file).find_parents_w_child("^ip vrf ", "rd")}
 return []

#function get route rd of specific vrf on ios config
def ios_get_rd_vrf(config_file,vrf_name):
 if ios_has_vrf(conf_file):
  buff = CiscoConfParse(CiscoConfParse(conf_file).find_all_children("ip vrf "+vrf_name), factory=True)
  obj = buff.find_objects('ip vrf ')[0]
  if CiscoConfParse(obj.ioscfg).find_objects('rd'):
  buff_vrf_attrib['rd'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'rd')[0].ioscfg).strip("'[]'").strip().replace('rd ','')
return False
 
def ios_get_vrf_config(conf_file,vrf_name):
 #return CiscoConfParse(conf_file).find_all_children("ip vrf " + vrf_name)
 buff_vrf_attrib = ios_vrf_default_attrib()
 buff = CiscoConfParse(CiscoConfParse(conf_file).find_all_children("ip vrf "+vrf_name), factory=True)
 obj = buff.find_objects('ip vrf ')[0]
 #print obj.ioscfg
 #save name
 buff_vrf_attrib['name'] = vrf_name
 #check rd if rd configured save rd
 if CiscoConfParse(obj.ioscfg).find_objects('rd'):
  buff_vrf_attrib['rd'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'rd')[0].ioscfg).strip("'[]'").strip().replace('rd ','')
 #check export-map if configured save export-map
 if CiscoConfParse(obj.ioscfg).find_objects('export\smap'):
  #print "ada ex map"
  for x in CiscoConfParse(obj.ioscfg).find_objects('export\smap'):
   #print x.ioscfg
   buff_vrf_attrib['ex-map'].append(str(x.ioscfg).strip("'[]'").strip().replace('export map ',''))
  #check import-map if configured save import-map
 if CiscoConfParse(obj.ioscfg).find_objects('import\smap'):
  print "ada imp map"
  for x in CiscoConfParse(obj.ioscfg).find_objects('import\smap'):
   #print x.ioscfg
   buff_vrf_attrib['im-map'].append(str(x.ioscfg).strip("'[]'").strip().replace('import map ',''))
 if CiscoConfParse(obj.ioscfg).find_objects('import\smap'):
  print "ada imp map"
  for x in CiscoConfParse(obj.ioscfg).find_objects('route-target\smap'):
   #print x.ioscfg
   buff_vrf_attrib['im-map'].append(str(x.ioscfg).strip("'[]'").strip().replace('import map ',''))
 return buff_vrf_attrib
 
 


 
#print ios_has_vrf("before_vrf.txt")
a = ios_get_list_vrf("before_vrf.txt")

config_file = "before_vrf.txt"



print ios_get_vrf_config(config_file,"AIRASIA")
