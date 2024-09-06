#!/bin/bash

if [ "$1" == "sfc" ]; then
cd sanfranciscocabs/f1_raw_data/
tar -xf sanfranciscocabs_part_1.tar.xz
tar -xf sanfranciscocabs_part_2.tar.xz
rm sanfranciscocabs_part_1.tar.xz
rm sanfranciscocabs_part_2.tar.xz

elif [ "$1" == "rt" ]; then
cd romataxi/f1_raw_data/
tar -xf romataxi_part_1.tar.xz
tar -xf romataxi_part_2.tar.xz
tar -xf romataxi_part_3.tar.xz
tar -xf romataxi_part_4.tar.xz
rm romataxi_part_1.tar.xz
rm romataxi_part_2.tar.xz
rm romataxi_part_3.tar.xz
rm romataxi_part_4.tar.xz

elif [ "$1" == "helsinki" ]; then
cd helsinki/f1_raw_data/
tar -xf helsinki.tar.xz
rm helsinki.tar.xz

elif [ "$1" == "manhattan" ]; then
cd manhattan/f1_raw_data/
tar -xf manhattan.tar.xz
rm manhattan.tar.xz

elif [ "$1" == "ngsim" ]; then
cd ngsim/
tar -xf us-101.tar.xz
cd ..

else
    echo "Invalid parameter"
fi
