#! /bin/bash 

grep http* temp > urls.txt
awk '{print "http://mementoweb.org/timemap/link/"$0}' urls.txt > mement.txt

echo "WORKING ON THIS FOR YOU"

rm -f cnt.csv
echo "num , site" >> cnt.csv
while read -r line
do
    line=$line
    new=$(echo $line | sed 's/http\?:\/\/mementoweb.org\/timemap\/link\///')
    num=$(curl -X GET $line | grep http* | wc -l)
    if  [ $num -gt 0 ]; then     
    	echo "$(($num-1)) ,"\""$new"\" >> cnt.csv
    fi
done < mement.txt

rm mement.txt urls.txt
