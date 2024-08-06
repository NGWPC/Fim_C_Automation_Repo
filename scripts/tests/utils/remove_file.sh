#!/bin/bash

chmod +x /home/jyoti.mikkilineni/pw/auto/scripts/tests/utils/remove_file.sh
FILE=$1
echo $FILE
sudo rm -r "$FILE"
echo "Deleted file"
