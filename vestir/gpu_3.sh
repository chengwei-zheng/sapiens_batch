#!/bin/bash

folders=(
    "V200F_VBDress_Halfzip_GP"
    "V203M_MensJumper_S_GP_2"
)

for folder in "${folders[@]}"; do
    echo "Running on $folder ..."
    for i in {0..7}; do
        echo "Running for cmr $i ..."
        bash ../lite/scripts/demo/torchscript/normal4batch.sh "$folder" "$i" 3
    done
done