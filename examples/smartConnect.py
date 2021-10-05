from pyVim.connect import SmartConnect, Disconnect
import ssl

# Connecting to vCenter
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
si = SmartConnect(host='vcip', user='user', pwd='pwd', sslContext=ctx)
# si = SmartConnect(host='vcip', user='user', pwd='pwd', port=443, sslContext=ctx)

datacenter = si.content.rootFolder.childEntity[0]
# datacenter = si.RetrieveContent().rootFolder.childEntity[0]

# Getting information all vms
vmList = datacenter.vmFolder.childEntity

vm0 = vmList[0] # May not be the first item on the list, try 'vm = vmList[1]'

for vm in vmList:
    if isinstance(vm, type(vm0)):
        print(vm.summary)

# turning vm on
assert vm0.runtime.powerState == 'poweredOff'
t = vm0.PowerOn()
assert t.info.state == 'success'
assert vm0.runtime.powerState == 'poweredOn'

Disconnect(si)