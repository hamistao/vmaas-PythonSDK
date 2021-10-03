# Here are some options using PyVmomi or VMware's Python SDK to connect to a vcenter instance:

## Create session

A less used method but is suggested in the official SDK repository and in VMware's 'VMware vCenter Server Management Programming Guide'.

### createSessionRepo.py

Method based on the official sdk Github repository sugestion for connecting to a vcenter instance, plus some additional features.
Uses the create_vcenter_client function that returns a VsphereClient object that represents the vsphere client and has many operations avaliable.

### createSession.py

Taken mostly from VMware's 'VMware vCenter Server Management Programming Guide', can be used together with some functions inside createSessionOperations folder as shown with listStorageConsumption.

## pyVim.SmartConnect

Appears to be the most used method to connect to vCenter by the community.
Uses pyVim.connect.SmartConnect object and therefore does not necessarily uses Vmware's Python SDK, although they are often used together.
Is suggested by the pyvmomi official repository, VMware's free course 'VMware Hands-on Labs - HOL-SDC-1422' and some community posts.

### smartConnect.py

This example is the most standard was mostly taken from VMware's free course previously mentioned.

### vConnector.py

This is an alternative that uses the vconnector library, that in turn uses SmartConnect underneath.
