# FLPUCI-Datasets
Datasets used in the FLPUCI Framework

This repository includes the following datasets:
* San Francisco Cabs (sanfranciscocabs)
* Roma Taxi (romataxi)
* Sumo Ipanema (sumo_ipanema)
* Next Generation Simulation (ngsim)

To unpack these dataset, run the unpack.sh script or

### San Francisco Cabs (sanfranciscocabs), Roma Taxi (romataxi), and Sumo Ipanema

Within these dataset directories, there is a subdirectory named f1_raw_data that contains tar.xz files.

Unpack these files inside the f1_raw_data and delete them from the directory.

### Next Generation Simulation (ngsim)

Within this dataset directory, there are tar.xz files. 

Unpack the tar.xz, go back to the root directory, and run the [handle_ngsim_locations.py](handle_ngsim_locations.py) 
script. By doing this, the directory named f1_raw_data will be created with the ngsim raw data files.

This dataset contains four subsets, so the [handle_ngsim_locations.py](handle_ngsim_locations.py) script generates
the raw data for one of them.

Then in the FLPUCI project run pre_processing.py script to preprocess the raw data.

Finally, run main.py for the experiments.
