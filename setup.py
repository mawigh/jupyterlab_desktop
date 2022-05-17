import setuptools;
from subprocess import check_call;
from jupyter_core import paths;
import shutil;

with open('README.md', 'r', encoding='utf-8') as fh:
    long_desc = fh.read();

setuptools.setup(
    name="jupyterlab_desktop",
    version="0.1",
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
    packages=setuptools.find_packages(where='src'),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "jupyter-server-proxy"
    ],
    entry_points = {
        'jupyter_serverproxy_servers': [
            'vnc = jupyterlab_desktop:initVNCServer'
        ]
    },
)
