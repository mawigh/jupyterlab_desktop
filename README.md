# JupyterLab Desktop (noVNC) Server Proxy

## Installation

### Requirements

```bash
python3 -m pip install jupyter-server-proxy
```

You may want to install JupyterLab.

### Build Singularity container

```bash
singularity build /opt/jh_desktop.sif Singularity
```

#### Local (User) Installation

Attention: You may do not want to overwrite an existing version of jupyter_notebook_config.py inside your home-directory ~/.jupyter/

```bash
cp jupyter_notebook_config.py ~/.jupyter/
```

#### Global Installation

Attention: You may do not want to overwrite an existing version of jupyter_notebook_config.py inside your global jupyter config directory /usr/local/etc/jupyter/

```bash
cp jupyter_notebook_config.py /usr/local/etc/jupyter/
```
