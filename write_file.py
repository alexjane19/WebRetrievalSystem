import os

def open_file(filename,dir="outputs/"):
    try:
        os.makedirs(dir, 0o0755)
    except OSError as e:
        if e.errno == 17:  # errno.EEXIST
            os.chmod(dir, 0o0755)
    #if not os.path.exists(dir):
       # os.makedirs(dir)
    file_output = open(dir+filename, 'w')
    file_output.truncate() #erase file
    return file_output

def write_file(data,file_output):
    file_output.write(data)