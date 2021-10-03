# PDF
from com.vmware.appliance.recovery.backup_client import Job
import time

# Function to bakcup Vcenter
def BackUpVcenter():

    req = Job.BackupRequest()

    # Include optional backup part for Statistics, Events, and Tasks.
    req.parts = ['seat']
    req.location_type = Job.LocationType.SCP
    req.comment = 'On-demand backup'
    req.location = my_storage_server + ':/home/scpuser/' + my_backup_folder + '/' + time.strftime('%Y-%m-%d-%H-%M-%S')
    req.location_user = my_scp_user
    req.location_password = my_scp_password

    # Issue a request to start the backup operation.
    backup_job = Job( my_stub_config )
    job_status = backup_job.create( req )
    job_id = job_status.id

    # Monitor progress of the job until it is complete.
    while (job_status.state == Job.BackupRestoreProcessState.INPROGRESS) :
        print( 'Backup job state: {} ({}%)'.format( job_status.state, job_status.progress ) )
    time.sleep( 10 )
    job_status = backup_job.get( job_id )

    # Report job completion.
    print( 'Backup job completion status: {}'.format( job_status.state) )