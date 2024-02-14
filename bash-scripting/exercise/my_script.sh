#!/bin/bash

n=$1
total_time=0
for i in $(seq 1 $n); do
  (time -p python3 my_script.py) 2> time.txt
  time=$(grep real time.txt | awk '{print $2}')
  total_time=$(echo "$total_time + $time" | bc)
done
average_time=$(echo "scale=3; $total_time / $n" | bc)
echo $average_time >> average_time.txt