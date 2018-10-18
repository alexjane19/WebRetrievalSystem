import readfilesdirectory
import part1_remove_useless_staff
import part2_vocabulary_count
import part3_maximum_freq
import part4_TF_IDF_documents
import part5_TF_IDF_query
import part6_cosine_similarity
import time
def main():
    start=time.time()
    print("Start Time: " , start)
    files = readfilesdirectory.get_directory_files()
    list_words = part1_remove_useless_staff.remove_staffs(files)
    voca_dic = part2_vocabulary_count.calc_vocabulary_per_document(list_words, files)
    part3_maximum_freq.find_ten_max_freq(list_words, files)
    part4_TF_IDF_documents.calc_tf_idf_weight(voca_dic, files)
    part5_TF_IDF_query.TF_IDF_query("query.txt", voca_dic, files)
    part6_cosine_similarity.calc_cosine_similarity(files)
    end = time.time()
    print("End Time: " , end)
    print("duration: " , end - start)
if __name__ == "__main__": main()