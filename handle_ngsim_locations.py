import os.path

import numpy as np
import pandas as pd

import shutil

f1_raw_data = f'ngsim/f1_raw_data'


def split_nodes(location):
    """
    This function splits a csv file per node. At the end, N new files are created, one for each node.
    :param location: The csv file name (location name)
    """
    with open(f'ngsim/{location}.csv', 'r') as file_r:
        lines = file_r.readlines()
        for line in lines:
            line_split = line.split(',')
            x = line_split[0]
            y = line_split[1]
            veh_id = line_split[2]
            timestamp = line_split[3]

            new_line = f'{x}, {y}, {veh_id}, {timestamp}'

            with open(f'{f1_raw_data}/{veh_id}.csv', 'a') as file_w:
                file_w.write(new_line)
    print(f'{location} done!')


def print_info(location):
    """
    This function reorganizes the XY coordinates of a csv file, so that the min(x) and the min(y) start from zero.
    It also prints the min and max timestamp, x and y in the new file.
    :param location: The csv file name (location name)
    """
    df = pd.read_csv(f'ngsim/{location}.csv', names=['x', 'y', 'veh_id', 'time']).sort_values(by='time')
    if df.x.min() < 0:
        df.x = df.x + np.absolute(df.x.min())
    else:
        df.x = df.x - np.absolute(df.x.min())
    if df.y.min() < 0:
        df.y = df.y + np.absolute(df.y.min())
    else:
        df.y = df.y - np.absolute(df.y.min())
    df.to_csv(f'ngsim/{location}.csv', index=False, header=False)
    print(f'{location}')
    print(f'min time: {df.time.min()} - max time: {df.time.max()}')
    print(f'min x: {df.x.min()} - max x: {df.x.max()}')
    print(f'min y: {df.y.min()} - max y: {df.y.max()}')


file = int(input('Choose the number that represents one of the following locations: \n1 - i-80 \n2 - us-101 \n'
                 '3 - lankershim \n4 - peachtree \n'))

while file < 1 or file > 4:
    print('Choose a valid value \n')
    file = int(input('Choose the number that represents one of the following locations: \n1 - i-80 \n2 - us-101 \n'
                     '3 - lankershim \n4 - peachtree \n'))

files = ['i-80', 'us-101', 'lankershim', 'peachtree']
file = files[file-1]

try:
    print(f'Handling {file}...')
    if os.path.exists(f1_raw_data):
        shutil.rmtree(f1_raw_data)
    os.mkdir(f1_raw_data)
    print_info(file)
    split_nodes(file)
except OSError as e:
    print(f'Error removing directory {f1_raw_data}: {e}')

