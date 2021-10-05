import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.vcenter_client import VM
from samples.vsphere.vcenter.helper.vm_helper import get_vm
from com.vmware.vcenter.vm_client import Power
from samples.vsphere.vcenter.helper import vm_placement_helper

session = requests.session()

# Disable cert verification.
session.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='vcip', username='user', password='pwd', session=session)

print(type(vsphere_client))

# List all VMs inside the cluster
print(vsphere_client.vcenter.VM.list())

# Setting parameters for vm creation
vm_name = 'vm-name'
guest_os='guest-os'
datacenter_name='datacenter_name'
vm_folder_name='vm_folder_name'
datastore_name='datastore_name'

# Create VM
placement=vm_placement_helper.get_placement_spec_for_resource_pool(
                vsphere_client,
                datacenter_name,
                vm_folder_name,
                datastore_name)

vm_create_spec = VM.CreateSpec( name=vm_name,
                                guest_os=guest_os,
                                placement=placement)

vm = vsphere_client.vcenter.VM.create(vm_create_spec)

vm = get_vm(vsphere_client, vm_name)

# Turning VM on
if vm:
    state = vsphere_client.vcenter.vm.Power.get(vm)
    if state == Power.Info(state=Power.State.POWERED_ON):
        vsphere_client.vcenter.vm.Power.stop(vm)
    elif state == Power.Info(state=Power.State.SUSPENDED):
        vsphere_client.vcenter.vm.Power.start(vm)
        vsphere_client.vcenter.vm.Power.stop(vm)
    vsphere_client.vcenter.VM.delete(vm) # Deleting created VM
