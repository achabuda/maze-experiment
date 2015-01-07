#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import os.path

COLUMNS_OUT = sum([['finished_{}'.format(i), 'time_{}'.format(i), 'number_{}'.format(i)] for i in range(1, 61)], [])

class ParseResultMaze(object):
    def __init__(self, file_result_dir, file_result_name, file_out_dir, file_out_name):
        super(ParseResultMaze, self).__init__()
        self.file_in = self._get_file_name(file_result_dir, file_result_name)
        self.file_out = self._get_file_name(file_out_dir, file_out_name)


    def _get_file_name(self, file_dir, file_name):
        return os.path.expanduser(os.path.normpath(os.path.join(os.path.normpath(file_dir), file_name)))

    def read_data(self):
        self.data =  np.load(self.file_in)

    def extract_data(self):
        self.data_extracted = pd.DataFrame()
        for person_id, person_data in enumerate(self.data):
            record = pd.DataFrame()
            try:
                for maze_index in person_data['kolejnosc']:
                    maze_name = maze_index
                    if -1 in person_data[maze_name]:
                        record['{}_{}'.format('finished', maze_name)] = pd.Series(0)
                        record['{}_{}'.format('time', maze_name)] = pd.Series(0)
                    else:
                        record['{}_{}'.format('finished', maze_name)] = pd.Series(1)
                        record['{}_{}'.format('time', maze_name)] = pd.Series(sum([time for time in person_data[maze_index]]))
                    record['{}_{}'.format('number', maze_name)] = pd.Series(len(person_data[maze_index]))
                self.data_extracted = self.data_extracted.append(record)
            except KeyError:
                pass
        self.data_extracted = self.data_extracted.set_index([range(1, len(self.data_extracted.values)+1)])

    def save_to_csv(self):
        self.data_extracted.to_csv(self.file_out, cols=COLUMNS_OUT)

    def run(self):
        self.read_data()
        self.extract_data()
        self.save_to_csv()

if __name__ == '__main__':
    parser = ParseResultMaze('./labirynt', 'wyniki.npy', './', 'wyniki.csv')
