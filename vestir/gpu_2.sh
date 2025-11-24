#!/bin/bash

folders=(
    "V200F_VBJeans_28_GP"
    "V200F_VBDress_Zipped_GP"
)

for folder in "${folders[@]}"; do
    echo "Running on $folder ..."
    for i in {0..7}; do
        echo "Running for cmr $i ..."
        bash ../lite/scripts/demo/torchscript/normal4batch.sh "$folder" "$i" 2
    done
done