from pyVim.connect import SmartConnect, Disconnect
import ssl

# Connecting to vCenter
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE
si = SmartConnect(host='IP', user='USER', pwd='PWD', sslContext=context)
# si = SmartConnect(host='IP', user='USER', pwd='PWD')
# si = SmartConnect(host='IP', user='USER', pwd='PWD', port=443, sslContext=context)

datacenter = si.content.rootFolder.childEntity[0]
# datacenter = si.RetrieveContent().rootFolder.childEntity[0]

# Getting information about specific vm
vmList = datacenter.vmFolder.childEntity
vm = vmList[0] # May not be the first item on the list, try 'vm = vmList[1]'

print(vmList.summary)

# turning vm on
assert vm.runtime.powerState == 'poweredOff'
t = vm.PowerOn()
assert t.info.state == 'success'
assert vm.runtime.powerState == 'poweredOn'

Disconnect(si)