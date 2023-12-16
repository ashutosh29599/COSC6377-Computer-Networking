#!/bin/bash

PYTHON_SCRIPT="monitor.py"

while true; do
    if ! pgrep -f "$PYTHON_SCRIPT" > /dev/null; then
        echo "Uptime Monitor is not running. Restarting $PYTHON_SCRIPT in 5 seconds..."
        sleep 5
        python "$PYTHON_SCRIPT"
    fi
    sleep 1
done
