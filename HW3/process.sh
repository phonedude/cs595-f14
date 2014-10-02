#! /bin/bash

rm -rf processd
mkdir processd

while read -r line 
do
	line=$line
	hash=$(echo $line | md5sum | awk '{print $1}')
	curl -X GET $line | lynx -stdin -dump -force_html -nolist > ./processd/$hash.proc
done < ./data/temp 
