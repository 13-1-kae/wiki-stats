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
import numpy as np



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
    p=plt.hist(data, bins, facecolor, alpha)
    plt.xlabel=xlabel
    plt.ylable=ylabel
    plt.title=title
    plt.grid(transparent)
    plt.show()
    p.savefig(fname)
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

   wg=WikiGraph()
   wg.load_from_file('wiki_small.txt')
   k=0
   for x in wg._redirect:
       if x==1:
           k+=1
   print('Количество статей с перенаправлением:', k)
   k1=1000000000
   k2=0
   for i in range (len(wg._offset)-1):
       if wg._offset[i+1]-wg._offset[i]==k1:
           k2+=1
       if wg._offset[i+1]-wg._offset[i]<k1:
           k1=wg._offset[i+1]-wg._offset[i]
           k2=0
   print('Mинимальное количество ссылок из статьи:', k1)
   print('Kоличество статей с минимальным количеством ссылок:', k2)
   k3=0
   k4=0
   k5=-1
   for i in range(len(wg._offset) - 1):
       if wg._offset[i + 1] - wg._offset[i] == k3:
           k4 += 1
       if wg._offset[i + 1] - wg._offset[i] > k1:
           k1 = wg._offset[i + 1] - wg._offset[i]
           k4 = 0
           k5=i+1
   print('Mаксимальное количество ссылок из статьи:',k3)
   print('Kоличество статей с максимальным количеством ссылок:', k4)
   print('Cтатья с наибольшим количеством ссылок:', wg._titles[k5])
   l=len(wg._offset)
   k6=wg._offset[l]/l
   print('Cреднее количество ссылок в статье:', k6)
   lst=[]*len(wg._links)
   for x in wg._links:
       lst[x]+=1
   min=1000000000
   k7=-1
   k8=0
   for i in range(len(lst)):
       if lst[i]==min:
           k8+=1
       if lst[i]<min:
           min=lst[i]
           k7=i
           k8=0
   print('Минимальное количество ссылок на статью:', min)
   print('Kоличество статей с минимальным количеством внешних ссылок:', k8)
   max=-1
   k9=-1
   k10=0
   for i in range(len(lst)):
       if lst[i]==max:
           k10+=1
       if lst[i]>max:
           max=lst[i]
           k9=i
           k10=0
   print('Mаксимальное количество ссылок на статью:', max)
   print('Kоличество статей с максимальным количеством внешних ссылок:', k10)
   print('Cтатья с наибольшим количеством внешних ссылок:', wg._titles[k9])
   s=0
   for i in range(len(lst)): s+=lst[i]
   k11=s/len(lst)
   print('Cреднее количество внешних ссылок на статью:', k11)


