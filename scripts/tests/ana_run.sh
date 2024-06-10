#!/bin/bash

my_dir="File_$RANDOM"
echo $my_dir

source /contrib/software/miniconda/miniconda/etc/profile.d/conda.sh
conda activate /contrib/software/miniconda/miniconda/ras2fim_ray
sudo mkdir -m777 /efs/translated_ras_libraries/temp/$my_dir
python3 /efs/projects/ras_abdul/ras2fim/src/ras2inundation.py -g /efs/translated_ras_libraries/usgs/outputs/cc58022/geocurves -f /efs/fim-data/hand_fim/inputs/rating_curve/nwm_recur_flows/nwm21_17C_recurr_100_0_cms.csv -t /efs/translated_ras_libraries/temp/$my_dir/output_ras2inundation.gpkg
