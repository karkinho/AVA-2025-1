#!/bin/bash
c=0
i=65536
while ((c < 11))
do
    x=0
    while ((x < 30))
    do
        ./ordena $i >> ./res.csv 
    ((x+=1))
    done
   ((i = i*2))
   ((c+=1))
done