#/bin/bash
#pip install pysonde
sounding_converter -i ./examples/level0/*.mwx -o ./examples/level1_mwx/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc -c config/main_mwx.yaml
sounding_converter -i ./examples/level0/*.cor -o ./examples/level1_cor/RS_{campaign}_{platform}_L1_%Y%m%dT%H%M_{direction}.nc -c config/main_cor.yaml

#Add the reformatting code here



#rm ./data/level2/*_????????T????_*.nc
#zip -r data.zip data


