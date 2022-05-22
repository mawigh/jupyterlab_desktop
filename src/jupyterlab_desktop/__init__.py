import os;
import subprocess;
from shutil import which;

def initVNCServer ():

    instance = JupyterLabDesktop();
    command = instance.getCommand('{port}');

    desktop_conf = {
        'command': command,
        'timeout' : 30,
        'mappath': {'/': '/vnc_lite.html'},
        'new_browser_tab': True,
        'environment': {
        },
        'launcher_entry' :  {
            'enabled': True,
            'title': 'Remote Desktop (VNC)',
            'icon_path': JupyterLabDesktop.getnoVNCLogo()
        }
    }

    environment = instance.getEnvironment();
    desktop_conf['environment'].update(environment);

    return desktop_conf;

class JupyterLabDesktop:

    def __init__ (self):

            self.files = os.path.abspath(os.path.join(os.path.dirname(__file__), "../files"));
            self.vncStartup = self.files + '/runVNCServer.sh';
            self.xstartup  = self.files + '/xstartup';
            self.noVNC = self.files + '/noVNC/';

            self.singularity_cmd = 'singularity';
            check_singularity = which(self.singularity_cmd);
            if check_singularity == None:
                self.singularity_cmd = self.loadSingularity();

    def getEnvironment (self):

        env = {
            "SINGULARITY_BIND": self.vncStartup + ':/runVNCServer.sh,' + self.xstartup + ':/xstartup,' + self.noVNC + ':/noVNC',
        };

        return env;

    def getCommand (self, vncPort=5001):

        singularity_container = self.files + '/jh_desktop.sif';

        full_cmd = self.singularity_cmd + ' exec ' + singularity_container + ' /runVNCServer.sh ' + str(vncPort);

        return full_cmd.split();

    def loadSingularity (self):

        existing_env = os.environ.copy();
        lmod_cmd = os.environ['LMOD_CMD'];
        load_cmd = subprocess.Popen(str(lmod_cmd) + ' load singularity | grep -w "^PATH" | cut -d "=" -f2 | cut -d ":" -f1', shell=True, env=ex, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL);
        out, err = load_cmd.communicate();
        singularity_cmd = out + '/singularity';

        if os.path.exists(singularity_cmd):
            return singularity_cmd;

    @staticmethod
    def getnoVNCLogo ():
        logo = os.path.abspath(os.path.join(os.path.dirname(__file__), "../files/noVNC.svg"));
        return logo;
