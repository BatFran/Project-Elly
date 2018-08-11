#!/bin/bash

echo 'grepping for months'

grep -n -i 'january\|february\|march\|april\|may\|june\|july\|august\|september\|october\|november\|december' raw*txt > lines_months.txt

line=$(cut -d":" -f1 lines_months.txt)

echo ${line}

cp raw_gutenberg_tolstoy_1895.txt raw_gutenberg_tolstoy_1895.txt.original


for i in ${line}
 	 do
sed -i "${i} s/^/\\\n/" raw*txt
	 done


echo END
