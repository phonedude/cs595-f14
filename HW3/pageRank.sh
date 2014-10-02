#! /bin/bash 

rm prRes

while read -r line 
do 
 a="http://"
	s=$(./page.pl $a$line)

	s=$(echo "scale=1; $s/10" | bc -l)
	echo $s, $line >> prRes 
done < "urlsRes"

sort -nr -k1 -t,  prRes > PR.txt
