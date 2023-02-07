import os

def rename_files(path):
    for i, filename in enumerate(os.listdir(path)):
        dest = f'map_{i}.jpg'
        source = path + filename
        dest = path + dest
        os.rename(source, dest)

if __name__ == '__main__':
    rename_files('training_data/')