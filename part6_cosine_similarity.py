import threading

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import operator
import write_file as writer

cosine_similarity_list = {}

def calc_cosine_similarity(files):
    documents = read_documents_and_query(files,"query.txt")
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    a=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    find_ten_doc(a[0][1:],files)
    th = threading.Thread(target=save_in_file, args=(a[0][1:],files,), name="thread_cosine_similarity")
    th.start()

def read_documents_and_query(files,path_query):
    documents = []
    file_q = open(path_query,"r")
    documents.append(file_q.read())
    for file in files:
        text = open(file['directory'],"r")
        documents.append(text.read())
    return documents

def save_in_file(cos_sim,files):
    global cosine_similarity_list
    namefile = "output_cosine_similarity.txt"
    file_out2 = writer.open_file(namefile)
    for i in range(files.__len__()):
        writer.write_file(files[i]['filename']+ " : "+str(cos_sim[i])+ "\n",file_out2)
        cosine_similarity_list[files[i]['filename']] = cos_sim[i]


def find_ten_doc(list_doc_sim,files):
    temp = list_doc_sim.copy()
    namefile = "output_ten_documents_similarity.txt"
    file_out2 = writer.open_file(namefile)
    for i in range(10):
        index, value = max(enumerate(temp), key=operator.itemgetter(1))
        writer.write_file(files[index]['filename']+ " : "+str(value)+ "\n",file_out2)
        temp[index]=0.0

