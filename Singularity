Bootstrap: library
From: debian:bullseye

%post

    apt -y update
    export DEBIAN_FRONTEND=noninteractive
    apt install -y python3 python3-pip procps websockify xterm gcc dbus-x11 xfce4 xfce4-panel xfce4-session xfce4-settings xfce4-terminal xorg wget git vim-tiny vim-gtk3 zsh                                                      
    wget https://sourceforge.net/projects/turbovnc/files/2.2.5/turbovnc_2.2.5_amd64.deb/download -O turbovnc_2.2.5_amd64.deb                                                                                      
    apt install -y -q ./turbovnc_2.2.5_amd64.deb
    rm ./turbovnc_2.2.5_amd64.deb
    ln -s /opt/TurboVNC/bin/* /usr/local/bin/
