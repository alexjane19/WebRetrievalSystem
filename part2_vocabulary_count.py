import threading
from collections import Counter
import write_file as writer1
import write_file as writer2

def calc_vocabulary_per_document(list_word,files,query=False):
    voca_dic = {}
    if not query:
        namefile = "output_vocabulary.txt"
        file_out1 = writer1.open_file(namefile)
    for file in files:
        num = Counter(list_word[file['filename']]).most_common()
        #print("listnum: ",num)
        voca_dic[file['filename']] = num
        if not query:
            writer1.write_file(file['filename'] + " : " + str(num.__len__())+"\n",file_out1)
        namefile1 = "output_freq_" + file['filename']
        #save_freq_words_in_file(namefile1,num)
        th = threading.Thread(target=save_freq_words_in_file, args=(namefile1,num,), name="thread_"+file['filename'])
        th.start()
    return voca_dic
def save_freq_words_in_file(namefile,listcount):
        file_out2 = writer2.open_file(namefile)
        for each in listcount:
            writer2.write_file(str(each)+"\n",file_out2)
