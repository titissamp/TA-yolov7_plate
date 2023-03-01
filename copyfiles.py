import os
import shutil

# set source and destination folders
src_folder = 'D:/TUGASAKHIR/Dataset/Dataset_Baru/'
dst_folder = 'D:/TUGASAKHIR/Dataset/Dataset_Baru/split'

# iterate through files in source folder
for file in os.listdir(src_folder):
    # check if file has .jpg extension
    if file.endswith('.jpg'):
        # get filename without extension
        filename = os.path.splitext(file)[0]
        # check if matching .txt file exists in source folder
        if os.path.exists(os.path.join(src_folder, filename + '.txt')):
            # copy both files to destination folder
            shutil.copy(os.path.join(src_folder, filename + '.jpg'), dst_folder)
            shutil.copy(os.path.join(src_folder, filename + '.txt'), dst_folder)
