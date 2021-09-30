# from createSession import createSession
# from listStorageConsumption import listStorageConsumption
# from healthChecker import healthChecker
# from checkDatabase import checkDatabase

from createSessionREST import *

vcip = 'ip'
user = 'user'
pwd = 'pwd'

session = get_vc_session(vcip, user, pwd)

r = get_vms(vcip)

vms = json.loads(r.text)

print(vms)

vms_data = vms['value']
for vm in vms_data:
    print(vm.get('name') +  "::" + vm.get('vm'))

print(vms)
