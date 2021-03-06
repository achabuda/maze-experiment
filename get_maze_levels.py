#!/usr/bin/python
# -*- coding: utf-8 -*-

from parse_result_maze import *
import pandas as pd
from matplotlib import pyplot as plt

COLUMNS_TIME = sum([['time_{}_{}'.format(i, type_) for type_ in ['n', 'T', 'T->']] for i in range(1, 61)], [])
COLUMNS_NUMBER = sum([['number_{}_{}'.format(i, type_) for type_ in ['n', 'T', 'T->']] for i in range(1, 61)], [])
COLUMNS_FINISHED = sum([['finished_{}_{}'.format(i, type_) for type_ in ['n', 'T', 'T->']] for i in range(1, 61)], [])
THRESHOLD = 5
len_=5

class GetMazeLevels(ParseResultMaze):
    def __init__(self, file_result_dir='', file_result_name='', file_out_dir='', file_out_name='', parse_data_in=True):
        if not parse_data_in:
            self.read_data_result(file_result_dir, file_result_name)
	else:
            super(GetMazeLevels, self).__init__(file_result_dir, file_result_name, file_out_dir, file_out_name)
            self.read_data()
            self.extract_data()
    def read_data_result(self, file_result_dir, file_result_name):
        self.data_extracted = pd.read_csv(self._get_file_name(file_result_dir, file_result_name))

    def _extract_time_data(self): 
        return self.data_extracted[COLUMNS_TIME]

    def _extract_finished_data(self): 
        return self.data_extracted[COLUMNS_FINISHED]

    def _extract_number_data(self): 
        return self.data_extracted[COLUMNS_NUMBER]

    def get_levels_time_sort(self):
        related_data = self._extract_time_data()
        self.data_time = pd.DataFrame()
        for col_name in COLUMNS_TIME:
            all_data = related_data[col_name].select(lambda x: related_data[col_name][x]>0.0)
            select_data = all_data.select(lambda x: all_data[x]<all_data.mean()+2*all_data.std() and all_data[x]>all_data.mean()-2*all_data.std()) 
            self.data_time['_'.join(col_name.split('_')[-2:])] = pd.Series(select_data.mean())
        data_sorted = self.data_time.T.sort(column=0)
        self.levels_time_sort = data_sorted.index

    def get_levels_number_sort(self):
        related_data = self._extract_number_data()
        self.data_number = pd.DataFrame()
        for col_name in COLUMNS_NUMBER:
            all_data = related_data[col_name]
            self.data_number['_'.join(col_name.split('_')[-2:])] = pd.Series(all_data.mean())
        data_sorted = self.data_number.T.sort(column=0)
        self.levels_number_sort = data_sorted.index

    def get_levels_finish_sort(self):
        related_data = self._extract_finished_data()
        self.data_finished = pd.DataFrame()
        for col_name in COLUMNS_FINISHED:
            all_data = related_data[col_name]
            self.data_finished['_'.join(col_name.split('_')[-2:])] = pd.Series(len_-sum(all_data.values))
        data_sorted = self.data_finished.T.sort(column=0)
        self.levels_finish_sort = data_sorted.index

    def select_levels(self):
        to_remove = []
        for index, data_finished in enumerate(self.data_finished.T.values,1):
            if data_finished>=THRESHOLD:
                to_remove.append(str(index))
        self.selected_levels = [level for level in self.levels_time_sort if not level in to_remove]

    def run(self):
        self.get_levels_time_sort()
        self.get_levels_finish_sort()
        self.get_levels_number_sort()
        self.select_levels()
        print len(self.selected_levels)
        data_out = []
        plt.plot([self.data_finished[i].values[0] for i in self.selected_levels], '--o')
        plt.plot([self.data_time[i].values[0] for i in self.selected_levels], '--or')
        plt.plot([self.data_number[i].values[0] for i in self.selected_levels], '--og')
        plt.show()

if __name__ == '__main__':
    levels = GetMazeLevels('./', 'wyniki_nowe_1.csv', parse_data_in=False)
    levels.run()

