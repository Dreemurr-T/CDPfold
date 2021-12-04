#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:36:01 2018

@author: zhangch
"""
import os
import pandas as pd
import csv

# 遍历指定目录，显示目录下的所有文件名

list_Dir = 'C:/Users/thy01/Desktop/AI_group/archiveII/' # 修改为本地文件路径
csv_Dir = 'C:/Users/thy01/Desktop/AI_group/data_csv/'
seq_Dir = 'C:/Users/thy01/Desktop/AI_group/data_seq/'


def readfile(fileDir, filename):
    fopen = open(fileDir+filename, 'r')
    rnafile = fopen.readlines()
    del rnafile[0]
    with open("test.txt", 'w') as f:
        for i in rnafile:
            f.write(i)
    data = pd.read_csv("test.txt", sep='\t', header=None)
    return data, filename


def transform(data):
    rnaseq = data.loc[:, 1]
    rnadata1 = data.loc[:, 0]
    rnadata2 = data.loc[:, 4]
    rnastructure = []
    for i in range(len(rnadata2)):
        if rnadata2[i] == 0:
            rnastructure.append(".")
        else:
            if rnadata1[i] > rnadata2[i]:
                rnastructure.append(")")
            else:
                rnastructure.append("(")
    return rnaseq, rnastructure


def savefile(rnaseq, rnastructure, filename):
    if not os.path.exists(csv_Dir):
        os.mkdir(csv_Dir)
    rnafile = filename[:-3]
    rnafile = rnafile+".csv"
    rnafile = csv_Dir + rnafile
    rnacsv = open(rnafile, 'w', newline="")
    writer = csv.writer(rnacsv)
    m = len(rnastructure)
    for i in range(m):
        # print(rnastructure)
        writer.writerow(rnastructure[i])
    if not os.path.exists(seq_Dir):
        os.mkdir(seq_Dir)
    rnaseqfile = seq_Dir + filename[:-3] + "_seq.csv"
    rnaseqcsv = open(rnaseqfile, 'w', newline="")
    seqwriter = csv.writer(rnaseqcsv)
    m = len(rnastructure)
    for i in range(m):
        seqwriter.writerow(rnaseq[i])


if __name__ == '__main__':
    pathDir = os.listdir(list_Dir)
    for i in pathDir:
        if i.endswith(".ct") and i.split('_')[0] != 'telomerase':
            # print(i)
            data, filename = readfile(list_Dir, i)
            rnaseq, rnastructure = transform(data)
            savefile(rnaseq, rnastructure, filename)
