from __future__ import division

import csv
import threading

from stemming.porter2 import stem
from math import log
import write_file as writer
TF_docs = {}
IDF_docs = {}
all_word = {}
TF_q = {}
IDF_q = {}
def calc_tf(vocabulary_list,files,query=False):
    all_tf = {}
    for file in files:
        _tf = []
        max_freq_word=vocabulary_list[file['filename']][0][1]
        for list in vocabulary_list[file['filename']]:
            _tf.append((list[0] , list[1] / max_freq_word))
        all_tf[file['filename']] = _tf
        namefile1 = "output_tf_" + file['filename']
        th = threading.Thread(target=save_in_file, args=(namefile1,_tf,query,), name="thread_tf_"+file['filename'])
        th.start()
    if query:
        global TF_q
        TF_q = all_tf
    else:
        global TF_docs
        TF_docs = all_tf

def calc_idf(vocabulary_list,files,total_doc=1400,query=False):
    global all_word
    all_word = read_words_file()
    all_idf = {}
    for file in files:
        _idf = []
        for list in vocabulary_list[file['filename']]:
            try:
                _idf.append((list[0] , log(total_doc / float(all_word[stem(list[0])][1]))))
            except KeyError:
                _idf.append((list[0] , 0))

        all_idf[file['filename']] = _idf
        namefile1 = "output_idf_" + file['filename']
        th = threading.Thread(target=save_in_file, args=(namefile1,_idf,query,), name="thread_idf_"+file['filename'])
        th.start()
    if query:
        global IDF_q
        IDF_q = all_idf
    else:
        global IDF_docs
        IDF_docs = all_idf

def calc_tf_idf_weight(vocabulary_list,files,total_doc=1400,query=False):
    W = {}
    th1 = threading.Thread(target=calc_tf, args=(vocabulary_list,files,query,), name="thread_tf")
    th2 = threading.Thread(target=calc_idf, args=(vocabulary_list,files,total_doc,query,), name="thread_idf")
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    if query:
        TF = TF_q
        IDF = IDF_q
    else:
        TF = TF_docs
        IDF = IDF_docs

    for file in files:
        row = []
        for i in range(TF[file['filename']].__len__()):
            row.append((TF[file['filename']][i][0] , TF[file['filename']][i][1]*IDF[file['filename']][i][1]))
        W[file['filename']] = row
        namefile1 = "output_tf_idf_" + file['filename']
        th = threading.Thread(target=save_in_file, args=(namefile1,row,query,), name="thread_tf_idf_"+file['filename'])
        th.start()
    th_c = threading.Thread(target=save_in_csv_file, args=(files,W,query,), name="save_matrix")
    th_c.start()

def read_words_file():
    file = open("words.txt", "r")
    all = {}
    for lin in file:
      line = lin.split('\n')
      s=line[0].split('\t')
      all[s[0]] = (s[1],s[2])
    return all

def save_in_file(namefile,para,query):
        if query:
            file_out2 = writer.open_file(namefile,"outputs/tf_idf_with_query/")
        else:
            file_out2 = writer.open_file(namefile)
        for each in para:
            writer.write_file(str(each)+"\n",file_out2)

def save_in_csv_file(files,W,query):

    global all_word
    if query:
        namefilecsv = "outputs/matrix_with_query.csv"
    else:
        namefilecsv = "outputs/matrix.csv"
    with open(namefilecsv, 'w') as csvfile:
        fieldnames = []
        fieldnames.append("words")
        for file in files:
            fieldnames.append(file['filename'])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        msg = "main"
        i=0
        for key in all_word:
            th = threading.Thread(target=pro, args=(key,files,W,writer,), name=key)
            th.start()
            i+=1
            if query:
                msg="query"
            print("please wait if you want csv file for " + msg+ " matrix... (" +str(i) + "/4500)\n")
    print("finish!!")


def pro(key,files,W,writer):
    row = {}
    row['words'] = key
    for file in files:
        for weg in W[file['filename']]:
            if key in stem(weg[0]):
                row[file['filename']] = weg[1]
                break
            row[file['filename']] = 0.0
    writer.writerow(row)

