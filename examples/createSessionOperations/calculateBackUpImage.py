# PDF
from com.vmware.appliance.recovery.backup_client import Parts

# Function  to collect the information you need to calculate the size needed to store a backup image of the vCenter Server instance.
def calculateBackUpImage(my_stub_config):
    Parts_stub = Parts( my_stub_config )
    parts = Parts_stub.list()

    # Extract IDs of backup image parts.
    sizes = {}
    total = 0
    for part in parts :
        size = Parts_stub.get( part.id )
        sizes[part.id] = size
        total += size

    # Show the result.
    print( 'Backup image parts:' )
    for part_id in sizes.keys() :
        print( ' part {0} = {1}KB'.format( part_id, sizes[part_id] ) )
        print( 'Total size: {0}KB'.format( total ) )