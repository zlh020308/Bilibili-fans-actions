#!/bin/bash
python3 bilibili.py >> ./data/data.txt
echo "date,follower" > ./data/data.csv
tac ./data/data.txt >> ./data/data.csv
