#!/bin/bash

counter=0

until [ $counter -gt 20 ]
do
    echo $counter
    ((counter++))
    python query_tweet.py > data.txt

    file_name=$(python get_filename.py $counter)
    tts --text "$(cat data.txt)"   --model_name "tts_models/en/ljspeech/tacotron2-DDC"    --out_path $file_name

done

