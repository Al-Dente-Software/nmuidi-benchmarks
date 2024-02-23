#!/usr/bin/env python3
import random
import os
import pathlib

num_top_level_folders = 5179
num_files = 5
file_size = 1024*1024*5

for i in range(0, num_top_level_folders):
    name = hex(random.getrandbits(128))[2:]
    dir_name_length = 8
    for i in range(0, num_files):
        file_name = hex(random.getrandbits(64))[2:]
        path_name = os.path.sep.join(["files"] + [name[i:i+dir_name_length] for i in range(0, len(name), dir_name_length)] + [file_name])
        pathlib.Path(os.path.dirname(path_name)).mkdir(parents=True, exist_ok=True)
        f = open(path_name, 'wb')
        f.truncate(file_size)
        f.close()
