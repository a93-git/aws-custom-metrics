#! /bin/bash
memTot=$(cat /proc/meminfo | grep 'MemTotal' | sed -e 's/ //g' -e 's/kB//g' | cut -f 2 -d ':')
memFree=$(cat /proc/meminfo| grep 'MemFree' | sed -e 's/ //g' -e 's/kB//g' | cut -f 2 -d ':')
a=$(echo "($memTot-$memFree)*100/$memTot" | bc)
echo $a > mem-stat
