#! /bin/bash 

grep http* output.txt > urls.txt
awk '{print "http://mementoweb.org/timemap/link/"$0}' urls.txt > mement.txt

rm -f cnt.csv
echo "num , site" >> cnt.csv
filename=$mement
while read -r line
do
    line=$line
    num=$(curl -X GET $line | grep http* | wc -l)
    if  [ $num -gt 0 ]; then     
    	echo "$(($num-1)) ,"\""$line"\" >> cnt.csv
    fi
done < mement.txt