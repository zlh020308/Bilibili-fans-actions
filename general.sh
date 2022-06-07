while IFS= read -r line; do
    python3 general.py $line >> ./txt/$line.txt
    echo "date,follower,likes,video_view,article_view" > ./csv/$line.csv
    tac ./txt/$line.txt >> ./csv/$line.csv
done < uid.txt
