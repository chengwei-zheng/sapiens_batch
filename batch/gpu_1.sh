#!/bin/bash

folders=(
    "V200F_VBStalk_Out_GP"
    "V200F_VBStalk_In_GP"
)

for folder in "${folders[@]}"; do
    echo "Running on $folder ..."
    for i in {0..7}; do
        echo "Running for cmr $i ..."
        bash ../lite/scripts/demo/torchscript/normal4batch.sh "$folder" "$i" 1
    done
done