import os
import shutil

def path_verify(path:str)->bool:
    return os.path.isdir(path)


def menu():
    path = input('scri locatia unde vrei sa se aranjeze fisierele sau apasa q pentru a iesi: ')
    while not path_verify(path):
        if path.upper() == 'Q':
            exit()
        else:
            path = input('scri locatia unde vrei sa se aranjeze fisierele sau apasa q pentru a iesi: ')
    return path

def list_files(path:str)->list:
    files = [file for file in os.listdir(path) if os.path.isfile(path+'\\'+file)]
    return files

def create_dirs(path:str):
    for dir in DIRECTORY:
        if not os.path.isdir(path+'\\'+dir):
            os.mkdir(path+'\\'+dir)

def connections(path:str)->dict:
    dir_and_files = {path+'\\'+location:EXTENSION[i] for i, location in enumerate(DIRECTORY) if os.path.isdir(path)}
    return dir_and_files

def extension(file:str)->str:
    index_dots = [i for i,dots in enumerate(file) if dots == '.']
    extens = file[index_dots[-1]:]
    return extens


if __name__ == '__main__':
    DIRECTORY = ['Pictures','Videos','PDFs','Music',"TXTs",'PYs','WORDs','EXCELs','EXEs','Compressed_files','torrents']
    EXTENSION = [['.jpg','.jpeg','.png','.JPG'],['.mp4','.MP4','.MOV','.mov','.avi'],['.pdf','.PDF'],
                 '.mp3','.txt','.py',['.doc','.docs','.docx'],['.csv','.xlsx','.xls'],'.exe',['.7z','.zip'],'.torrent']

    path = menu()
    mapping = connections(path)
    files = list_files(path)
    create_dirs(path)
    for file in files:
        extens = extension(file)
        for k,v in mapping.items():
            if extens in v:
                try:
                    shutil.move(path+'\\'+file , k)
                except:
                    print(f'{file} nu se poate muta')

