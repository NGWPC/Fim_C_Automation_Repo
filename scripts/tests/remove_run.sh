#!/bin/bash

chmod +x /home/jyoti.mikkilineni/pw/auto/scripts/tests/remove_run.sh
FILE=$1
echo $FILE
sudo rm -r "$FILE"
echo "Deleted file"
