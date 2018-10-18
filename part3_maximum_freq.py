from collections import Counter
import write_file as writer
def find_ten_max_freq(list_word,files):
    all_doc = []
    namefile = "output_ten_of_max_freq.txt"
    file_out1 = writer.open_file(namefile)
    for file in files:
        all_doc = all_doc + list_word[file['filename']]
    num = Counter(all_doc).most_common()
    for i in range(0,10):
        writer.write_file(str(num[i]) + "\n",file_out1)
        #print(num[i])