#! /bin/bash

cnt=$(grep internet ./processd/* | awk -F: '{ print $1}' | uniq -c | awk '{ print $1}' | wc -l)
term=$(grep internet ./processd/* | awk -F: '{ print $1}' | uniq -c | awk '{ print $1}'> term.txt)
dwc=$(wc -w `grep internet ./processd/* | awk -F: '{print $1}' | uniq -c |awk '{ print$2}'` | awk '{print $1}' | head -n -1 > dwc.txt)
urls=$(grep internet ./processd/* |awk -F: '{print $1}' |uniq -c |  awk -F/ '{print $3}' | awk -F. '{print $1}' | grep -f - ./LUT | awk -F, '{print $2}'>urls.txt >urls.txt)
paste term.txt dwc.txt urls.txt > 5.txt
size=40000000000
idf=$(echo ";l($size/$cnt)/l(2)"| bc -l)

rm -f table
while read -r a b c
do
	res=$(echo "$a/$b" | bc -l) 
	num=$(echo "$res*$idf" | bc -l);
	#echo $res $c
	echo $num $res $idf $c >> table
done <5.txt

head -n 10 table | sort -r -k1 | xargs printf "%.8f, %.8f, %.8f, %s\n"  >tfidf
head -n 10 table | sort -r -k1 | awk '{print $4}' | awk -F/ '{print $3}' >  urlsRes
 

