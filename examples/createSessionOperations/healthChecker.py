from com.vmware.appliance import health_client

# Function to request the overall system health indicator for vCenter Server and the overall health indicator for management services.
def healthChecker(my_stub_config):
    System_stub = health_client.System( my_stub_config )
    health = System_stub.get()
    print( 'Overall system health: %s' % health )

    # Issue request for applmgmt services health.
    Applmgmt_stub = health_client.Applmgmt( my_stub_config )
    health = Applmgmt_stub.get()
    print( 'Applmgmt services health: %s' % health )