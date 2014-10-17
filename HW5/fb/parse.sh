#! /bin/bash

grep -E '^ *name*' $1 | cut -d ' ' -f18- > temp
grep -E '^ *friend_count*' $1 | cut -d ' ' -f10-  > cnts

rm names

while read  line 
do 
	echo "\"$line\" , " >> names
done < temp 

echo "names,  count" 
paste names cnts 


rm temp cnts names 

