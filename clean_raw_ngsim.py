import os.path


"""
The NGSIM dataset is available at 
https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj

After download it, change the file name to NGSIM.csv to run the script.
"""


def split_locations():
    """
    This function runs over the NGSIM.csv file. It splits the dataset per location (roads). The four locations are i_80, us_101, lankershim and
    peachtree. Then, it creates a csv file for each location. Each file contains the vehicles the travel through a road
    """
    with open('NGSIM.csv') as ngsim:
        lines = ngsim.readlines()
        i_80 = []
        us_101 = []
        lankershim = []
        peachtree = []

        path = f'ngsim/'
        if not os.path.exists(path):
            os.mkdir(path)

        for line in lines[1:]:
            line_split = line.split(',')
            veh_id = line_split[0]
            timestamp = line_split[3][:10]
            x = line_split[4]
            y = line_split[5]
            location = line_split[24].replace('\n', '')

            new_line = f'{x}, {y}, {veh_id}, {timestamp}\n'

            if location == 'i-80':
                i_80.append(new_line)
            elif location == 'us-101':
                us_101.append(new_line)
            elif location == 'lankershim':
                lankershim.append(new_line)
            elif location == 'peachtree':
                peachtree.append(new_line)

        write_new_lines('i-80', i_80)
        write_new_lines('us-101', us_101)
        write_new_lines('lankershim', lankershim)
        write_new_lines('peachtree', peachtree)


def write_new_lines(file_name, list_lines):
    """
    This function writes the lines of a csv file
    :param file_name: The name of the file to open
    :param list_lines: The list of lines to be written
    """
    with open(f'ngsim/{file_name}.csv', 'w') as file:
        for line in list_lines:
            file.write(line)
    print(f'{file_name} done!')


split_locations()

