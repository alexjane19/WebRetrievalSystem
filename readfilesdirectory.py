import os
def get_directory_files(dir="Dataset/"):
    dir_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                dir_files.append({'directory':os.path.join(root, file),'filename': file})
                 #print(os.path.join(root, file))
    return dir_files