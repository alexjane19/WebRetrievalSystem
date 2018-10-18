import part1_remove_useless_staff
import part2_vocabulary_count
import part4_TF_IDF_documents
def TF_IDF_query(path_query,voca_dic,files):
    file_q = []
    file_q.append({'directory': path_query,'filename': path_query})
    list_word_query = part1_remove_useless_staff.remove_staffs(file_q)
    list_vocab_query = part2_vocabulary_count.calc_vocabulary_per_document(list_word_query, file_q, True)

    copy_files = files[:]
    copy_files.append(file_q[0])
    copy_voca_dic = voca_dic.copy()
    copy_voca_dic[path_query] = list_vocab_query[path_query]
    part4_TF_IDF_documents.calc_tf_idf_weight(copy_voca_dic, copy_files, 1401, True)




