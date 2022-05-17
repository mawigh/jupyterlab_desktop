import os;
import subprocess;

class JupyterLabDesktop:

    def __init__ (self, loadsingularity=None):

            self.loadsingularity = loadsingularity;
            
            self.files = os.path.abspath(os.path.join(os.path.dirname(__file__), "../files"));
            self.vncStartup = self.files + '/runVNCServer.sh';
            self.xstartup  = self.files + '/xstartup';
            self.noVNC = self.files + '/noVNC/';

            self.singularity_cmd = 'singularity';
            if not self.loadsingularity == None:
                self.singularity_cmd = self.loadSingularity();

    def getCommand (self, vncPort=5001):

        env = {
            "SINGULARITY_BIND": self.vncStartup + ':/runVNCServer.sh,' + self.xstartup + ':/xstartup,' + self.noVNC + ':/noVNC/',
        };

        singularity_container = self.files + '/jh_desktop.sif';

        full_cmd = self.singularity_cmd + ' exec ' + singularity_container + ' /runVNCServer.sh ' + str(vncPort);
        
        print(full_cmd);

        return full_cmd;

    def loadSingularity (self):

        #import lmod;
        from shutil import which;
        #lmod.load(self.loadsingularity);
        singularity_exec = which('singularity');
        return singularity_exec or None;

    @staticmethod
    def getnoVNCLogo ():
        logo = os.path.abspath(os.path.join(os.path.dirname(__file__), "../files/noVNC.svg"));
        return logo;
