import os

def remove_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path) 
    else: 
        pass


if __name__ =='__main__':
    remove_file('6hdaC0rlt9A')