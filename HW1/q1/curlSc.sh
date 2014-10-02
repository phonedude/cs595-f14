#! /bin/bash
rm -f *.htm
#curl -v -X POST -d "name=george" -d @gmicrosTest.txt http://www.posttestserver.com/post.php > postTest.htm
#curl -v -X POST -d "name=george" -d @gmicrosTest.txt http://httpbin.org/post > httpBin.htm
curl -v -X POST -d "name=george" -d @gmicrosTest.txt http://greensuisse.zzl.org/product/dump/dump.php > green.htm


