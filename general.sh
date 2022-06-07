while IFS= read -r line; do
    python3 general.py $line >> ./uid/$line.txt
    echo "date,follower,likes,video_view,article_view" > ./uid/$line.csv
    tac ./uid/$line.txt >> ./uid/$line.csv
done < uid.txt
