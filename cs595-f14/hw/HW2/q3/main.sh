#! /bin/bash 

grep  "^[^0]" cnt.csv | grep -o '"[^"]\+"' | grep -o '[^"]*[^"]'> temp

while read -r line 
do 
    line=$line
    python local.py line | 
    
done < temp
