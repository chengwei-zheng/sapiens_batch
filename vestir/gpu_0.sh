#!/bin/bash

folders=(
    "V200F_PatternedTrousers_S_GP_2"
    "V200F_Fish_S_GP_2"
)

for folder in "${folders[@]}"; do
    echo "Running on $folder ..."
    for i in {0..7}; do
        echo "Running for cmr $i ..."
        bash ../lite/scripts/demo/torchscript/normal4batch.sh "$folder" "$i" 0
    done
done