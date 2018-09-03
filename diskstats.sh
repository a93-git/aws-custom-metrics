#! /bin/bash
a=$(df | grep -vi Use | awk '{print $5 $6}')
for i in $a; do echo $i | sed -e 's/%/\t/g'; done
