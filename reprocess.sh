#/bin/bash
#pip install pysonde
sounding_converter -i ../data/level0/*.mwx -o "../data/level1_mwx/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc" -c config/main_mwx.yaml
sounding_converter -i ../data/level0/*.cor -o "../data/level1_cor/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc" -c config/main_cor.yaml

# Directory containing the level2 files
directory_level2="../data/level2"
# Execute the script to add the launching platform as a coordinate
python ./platform_coordinate/add_platform_coordinate.py "$directory_level2"

ncrcat -h ../data/level2/RS_*L2_*.nc ../data/concatenated/RS_ORCESTRA_level2_v1.0.0.nc
#rm ./data/level2/*_????????T????_*.nc
#zip -r data.zip data


