from vconnector.core import VConnector

client = VConnector(
     user='root',
     pwd='pwd',
     #host='host51.br.rdlabs.hpecorp.net'
     host='IP'
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