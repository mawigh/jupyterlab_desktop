# JupyterLab Desktop (noVNC) Server Proxy

![noVNC JupyterLab](imgs/noVNC_JupyterLab.png)

This package creates a JupyterLab Launcher icon which triggers a Singularity container to run a VNC Server (with websockify as a small webserver to noVNC)

If the command 'singularity' cannot be found in $PATH. It will be load using Lmod (module load singularity).

## Installation

### Using pip

```bash
python3 -m pip install git+https://github.com/mawigh/jupyterlab_desktop
```

### Build Singularity container

```bash
singularity build src/files/jh_desktop.sif Singularity

```

## Modify environment

You can modify the environment (add env vars into the container, mount additional file systems, ...) by editing the proxy configuration in src/jupyterlab_desktop/__init__.py (see environment: {})

## Modify vncserver attributes

vncserver will be called in src/files/runVNCServer.sh - You can add or modify parameters.
