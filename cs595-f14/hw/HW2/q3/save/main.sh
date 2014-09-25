#! /bin/bash 

grep  "^[^0]" cnt.csv | grep -o '"[^"]\+"' | grep -o '[^"]*[^"]'> temp

rm ts
c=0
while read -r line 
do 
    c=$((c+1))	
    echo $c	
    s=$(python local.py $line | ./code.py)
    echo $s  $line
    echo $s  $line >> ts
done < temp
