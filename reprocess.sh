#/bin/bash
#pip install pysonde
sounding_converter -i ./examples/level0/*.mwx -o ./examples/level1_mwx/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc -c config/main_mwx.yaml
sounding_converter -i ./examples/level0/*.cor -o ./examples/level1_cor/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc -c config/main_cor.yaml

# Reformatting starts here
# Directory containing the level1 files
directory_level1="../data/level1"
# Execute the script to add the launching platform as a coordinate
python ./reformat_level-1_data/reformat_level1.py "$directory_level1"

ncrcat -h ../data/level1/RS_*L1_*.nc ../data/concatenated/RS_ORCESTRA_level1_v1.0.0.nc



