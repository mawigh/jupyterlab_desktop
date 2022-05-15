def _setup_desktop ():

    from getpass import getuser;
    from shutil import which;

    username = getuser();
    singularity_container = '/opt/jh_desktop.sif';

    singularity_executable = which('singularity');
    if not singularity_executable == None:
        command = 'singularity exec ' + singularity_container + ' /opt/runVNCServer.sh {port}'
    else:
        return;
    
    return command.split();

c.ServerProxy.servers = {
    'vnc': {
        'command': _setup_desktop,
        'timeout' : 30,
        'mappath': {'/': '/vnc_lite.html'},
        'new_browser_tab': True,
        'environment': {
        },
        'launcher_entry' :  {
            'enabled': True,
            'title': 'Remote Desktop (VNC)'
        }
    }
}
