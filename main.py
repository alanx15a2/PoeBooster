import os
import shutil
from wand.image import Image
from multiprocessing import Pool, freeze_support

def ignore_files(folder, files):
    return [f for f in files if not os.path.isdir(os.path.join(folder, f))]

def thumbnail(imgs):
    file_name, new_file_name, resize_times = imgs
    try:
        if os.path.getsize(file_name) < 1024:
            print('Skipping small (<1KB) file', file_name)
            return

        with Image(filename=file_name) as im:
            new_width = im.width//(2**resize_times)
            new_height = im.height//(2**resize_times)
            if new_width < 4 or new_height < 4:
                print(f'Too small to compress {im.width} * {im.height}', file_name)
                return
            
            # start resize
            im.resize(new_width, new_width)
            im.save(filename=new_file_name)
            print(file_name)

        return 'OK'
    except Exception as e:
        return e

if __name__ == '__main__':
    # prevent error when using pyinstaller
    freeze_support()

    # user input
    input_path = input('Please input src path : ')
    output_path = input('Please input dst path : ')
    threads = int(input('How many threads use? default all : ') or os.cpu_count())
    resize_times = int(input('How many times resize? default 2 : ') or 2)

    print('copying root...')
    shutil.copytree(input_path, output_path, dirs_exist_ok=True, ignore=ignore_files)
    
    # Put all dds file into the queue.
    print('scaning dds file...')
    imgs = []
    for root, directories, files in os.walk(input_path):
        for name in files:
            if os.path.splitext(name)[1] == '.dds':
                name = os.path.join(root, name)
                imgs.append((name, name.replace(input_path, output_path), resize_times))

    pool = Pool(threads)
    results = pool.map(thumbnail, imgs)
    pool.close()