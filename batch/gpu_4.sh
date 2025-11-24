#!/bin/bash

folders=(
    "V203M_MensJumper_L_GP"
    "V203M_Snoopy_S_GP_2"
)

for folder in "${folders[@]}"; do
    echo "Running on $folder ..."
    for i in {0..7}; do
        echo "Running for cmr $i ..."
        bash ../lite/scripts/demo/torchscript/normal4batch.sh "$folder" "$i" 4
    done
done