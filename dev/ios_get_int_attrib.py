#utility library for get data from ios config

from ciscoconfparse import CiscoConfParse#Function check ios
#
def ios_has_vrf(conf_file):
 parse = CiscoConfParse("before.txt")

#function get interface attribute
def ios_get_int_attrib(conf_file,int):
 int_dict = {'name': '', 'desc': '', 'encap': '', 'ip': '', 'mask': '', 'ser_in' : '', 'ser_out' : '', 'mtu' : '', 'shut': True, 'vrf':'default'}
 int_regex = '^interface '+int
 buff = CiscoConfParse(CiscoConfParse(conf_file).find_all_children(int_regex), factory=True)
 obj = buff.find_objects('^interface')[0]
 int_dict['ip'] = obj.ipv4_addr
 int_dict['mask'] = obj.ipv4_netmask
 int_dict['name'] = obj.name
 int_dict['mtu'] = obj.manual_mtu
 int_dict['desc'] = obj.description
 if CiscoConfParse(obj.ioscfg).find_objects(r'ip\svrf'):
  int_dict['vrf'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'ip\svrf')[0].ioscfg).strip("'[]'").replace(' ip vrf forwarding ','')
 if CiscoConfParse(obj.ioscfg).find_objects(r'service-policy\sinput'):
  int_dict['ser_in'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'service-policy\sinput')[0].ioscfg).strip("'[]'").replace(' service-policy input ','')
 if CiscoConfParse(obj.ioscfg).find_objects(r'service-policy\soutput'):
  int_dict['ser_out'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'service-policy\soutput')[0].ioscfg).strip("'[]'").replace(' service-policy output ','')
 if not CiscoConfParse(obj.ioscfg).find_objects(r'shutdown'):
  int_dict['shut'] = False
 if CiscoConfParse(obj.ioscfg).find_objects(r'encapsulation\sdot1Q'):
  int_dict['encap'] = str(CiscoConfParse(obj.ioscfg).find_objects(r'encapsulation\sdot1Q')[0].ioscfg).strip("'[]'").strip().replace('encapsulation dot1Q ','')
 int_dict['desc'] = obj.description
 print (int_dict)

ios_get_int_attrib("before.txt","GigabitEthernet0/1.504")
