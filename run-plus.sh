
python3 bilibili-plus.py >> ./data/data-plus.txt
echo "date,follower,likes,video_view,article_view" > ./data/data-plus.csv
tac ./data/data-plus.txt >> ./data/data-plus.csv
