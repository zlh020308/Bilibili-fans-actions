#!/bin/bash
python3 bilibili.py
python3 bilibili.py >> ./data.txt
echo "date,follower" > ./data.csv
tac ./data.txt >> ./data.csv
