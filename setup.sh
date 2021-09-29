#cloning vmware's python sdk github repository
git clone https://github.com/vmware/vsphere-automation-sdk-python

#installing requirements
pushd vsphere-automation-sdk-python
export PYTHONPATH=${PWD}:$PYTHONPATH #exporting python path
pip3 install -r requirements.txt --extra-index-url file://'pwd'/lib
popd