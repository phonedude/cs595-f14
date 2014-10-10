#! /bin/bash



echo "digraph G {" > graph.dot
#echo "center=true;" >> graph.dot
#echo "size=\"6,6\";" >> graph.dot
echo "ranksep=8;" >> graph.dot
echo "ratio=auto;" >> graph.dot
echo "overlap=false;" >> graph.dot
for file in lks/*
do
 #cnt=1
 #file="lks/001"
 echo $file 
 a=$(head -n 2 $file | tail -n 1)
 alab=$(echo $a | sed -e 's|^[^/]*//||' -e 's|^www\.||' -e 's|/.*$||')
 echo "\"$a\" [label=\"$alab\"]" >> graph.dot

 tail -n+4 $file |
 {
 while read  line 
 do 
  cnt=$((cnt + 1))
  #echo $cnt
  line=$line
  llab=$(echo $line| sed -e 's|^[^/]*//||' -e 's|^www\.||' -e 's|/.*$||')
  echo "\"$line\" [label=\"$llab\"]" >> graph.dot
  echo "\"$a\" -> \"$line\";" >> graph.dot
  
 done
 }
done

echo "}" >> graph.dot
