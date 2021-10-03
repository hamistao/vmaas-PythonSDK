from vconnector.core import VConnector
import pyVmomi

client = VConnector(
     user='user',
     pwd='pwd',
     host='ip'
)

client.connect()

vms = client.get_vm_view()
print(vms.view)

host = client.get_object_by_property(
     property_name='name',
     property_value='esxi01.example.org',
     obj_type=pyVmomi.vim.HostSystem
    )

print(host.name)

client.disconnect()