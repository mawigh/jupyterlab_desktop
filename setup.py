import setuptools;
from setuptools.command.develop import develop;
from setuptools.command.install import install;
from subprocess import check_call;
from jupyter_core import paths;
import shutil;

class setupDevelop (develop):

    def run (self):

        # (PRE) Build Singularity container
        import subprocess;
        import os;
        print("Build Singularity container for Remote Desktop");
        #os.system("singularity build --force ./src/files/jh_desktop.sif Singularity");

        develop.run(self);

        # (POST) Copy Jupyter Config file
        jupyter_config_dir = paths.jupyter_config_dir();
        shutil.copy(os.path.dirname(__file__)+'/src/files/jupyter_notebook_config.py', jupyter_config_dir);

class setupInstall (install):

    def run (self):
        install.run(self);

        # build singularity container
        import subprocess;
        subprocess.run('singularity build /opt/jh_desktop.sif Singularity', shell=True);


with open('README.md', 'r', encoding='utf-8') as fh:
    long_desc = fh.read();

setuptools.setup(
    name="JupyterLabDesktop",
    version="1.0",
    author="Paderborn Center for Parallel Computing",
    author_email="pc2-support@uni-paderborn.de",
    description="Remote Desktop (noVNC) inside JupyterLab using a Singularity container (Server Proxy)",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://https://github.com/mawigh/jupyterlab_desktop/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "jupyter-server-proxy"
    ],
    cmdclass={
        "develop": setupDevelop,
        "install": setupInstall,
    },
)


