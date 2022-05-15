#!/bin/bash

websockify="/usr/bin/websockify"
vncserver="/usr/local/bin/vncserver"

noVNC="/noVNC"
xstartup="/xstartup"

noVNC_geometry="1680x1050"
noVNC_SecurityTypes="None"

port=$1;

if [[ -f $websockify ]] && [[ -f $vncserver ]]; then
    echo "noVNC Port: $port"
    $websockify -v --web $noVNC --heartbeat 30 $port -- $vncserver -verbose -rfbport $port -xstartup $xstartup -geometry $noVNC_geometry -SecurityTypes $noVNC_SecurityTypes -fg
else
    echo "Error: Could not found command websockify or vncserver" >&2
    exit 1
fi
