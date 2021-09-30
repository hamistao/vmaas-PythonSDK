# The options can be divided as follows:

## Create session

A less used method but proved to be the most efficient.

### createSessionREST.py

It is the only one that works for me and uses the REST api to connect to vcenter.
You can test it by running mainTest.py with your vcenter id, user and password.

### createSession.py

Taken mostly from VMware's 'VMware vCenter Server Management Programming Guide'.

## pyVim.SmartConnect

By far the most used method to connect to vCenter, however in my case it proved itself ineffective.

### smartConnect.py

The first example is the most standard was mostly taken from VMware's free course 'VMware Hands-on Labs - HOL-SDC-1422'.

### vConnector.py

As for the second it uses the vconnector library, that in turn uses SmartConnect underneath.

