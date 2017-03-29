__author__ = 'student'
#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            nm=-1
            (n, _nlinks)=(0, 0)
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for rl in f.readlines():
                rl2=rl.split()
                if len(rl2)==2:
                    n=int(rl2[0])
                    _nlinks=int(rl2[1])
                if len(rl2)==3:
                    self._redirect.append(int(rl2[1]))
                    self._sizes.append(int(rl2[0]))
                    self._offset.append(self._offset[nm]+int(rl2[2]))
                if len(rl2)==1:
                    if rl2[0].isdigit():
                        self._links.append(int(rl2[0]))
                    else:
                        self._titles.append(rl2[0])
                        nm+=1


        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1]-self._offset[_id]
        pass

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]
        pass

    def get_id(self, title):
        return self._titles.index(title)
        pass

    def get_number_of_pages(self):
        return len(self._sizes)
        pass

    def is_redirect(self, _id):
        return self._redirect[_id]
        pass

    def get_title(self, _id):
        return self._titles[_id]
        pass

    def get_page_size(self, _id):
        return self._sizes[_id]
        pass


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

   wg=WikiGraph()
   wg.load_from_file('wiki_small.txt')

    # TODO: статистика и гистограммы