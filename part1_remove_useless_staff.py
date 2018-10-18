from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import write_file as writer

def remove_staffs(files):
    list_data_file = {}
    for file in files:
        namefile = "output_"+ file['filename']
        #print(namefile)
        file_out = writer.open_file(namefile)
        list = []
        word_list = open(file['directory'], "r")
        stops = set(stopwords.words('english'))
        #print(stops)
        tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
        for line in word_list:
            for w in line.split():
                if w.lower() not in stops:
                    w = tokenizer.tokenize(w)
                    for i in w:
                        list.append(i)
                        writer.write_file(i + "\n",file_out)
        list_data_file[file['filename']] = list
        #print(list_data_file[file['filename']])
    return list_data_file
