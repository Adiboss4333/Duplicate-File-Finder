# Author: Aaditya V.S
import os
import sys
import threading
import time


def getFilePaths(path):
    file_paths = []
    for paths, dirs, files in os.walk(path):
        file_paths = [os.path.join(paths, f) for f in files]
    return file_paths


def removeDuplicateItems(_list):
    _list = list(_list)
    filtered_list = []
    dup = False
    for i in range(0, len(_list), 1):
        for j in range(i + 1, len(_list), 1):
            if _list[i] == _list[j]:
                dup = True
        if dup == False:
            filtered_list.append(_list[i])
        else:
            dup = False
    return filtered_list


def compare():
    print("------------Welcome to the Duplicate File Finder Tool------------")
    try:
        path = input("Enter the Path: ")
    except Exception:
        print('An Error Occured')
        compare()
    if os.path.isdir(path):
        paths = getFilePaths(path)
    else:
        print("Invalid Path Provided")
        exiting(-3)
    duplicates = []
    for i in range(0, len(paths), 1):
        data1 = b''
        data2 = b''
        with open(paths[i], 'rb') as file:
            data1 = file.read()
        for j in range(i + 1, len(paths), 1):
            with open(paths[j], 'rb') as file:
                data2 = file.read()
            if data1 == data2:
                duplicates.append(paths[i])
                duplicates.append(paths[j])
    if len(removeDuplicateItems(duplicates)) == 0:
        print('There are no duplicate files in the provided Directory')
        exiting(-2)
        return
    print('These are thee duplicate files according to their content')
    for i in removeDuplicateItems(duplicates):
        print(os.path.basename(i))
    print()
    print("What do you want to do with these files\n1) Delete and keep any one Copy of the files\n2) Delete all the files\n3) Do Nothing [EXIT]")
    ch = 0
    while ch < 1 or ch > 3:
        try:
            ch = int(input("Enter Your Choice-> "))
        except Exception:
            print('An Error Occured')
            compare()
    if ch == 1:
        _list = removeDuplicateItems(duplicates)
        _list.pop(len(_list) - 1)
        for i in _list:
            if os.path.isfile(i):
                os.remove(i)
        exiting(0)
    elif ch == 2:
        for i in removeDuplicateItems(duplicates):
            if os.path.isfile(i):
                os.remove(i)
        exiting(0)
    elif ch == 3:
        exiting(-1)
    else:
        print("Invalid Input")
        exiting(-1)
def exiting(_l):
    if _l == 0:
        print('The Operation was Successful Executed')
        print('Thank you for using this Tool')
        try:
            choice = input('Do you want to run the Tool again? [Y/N] ')[0]
        except Exception:
            print('An Error Occured')
            compare()
        if choice.upper() == 'Y':
            compare()
        else:
            print("Exiting in ", end='')
            for i in range(3,-1,-1):
                print(i,end=' ')
                time.sleep(1)
            sys.exit(0)
    elif _l == -1:
        print("Exiting in ", end='')
        for i in range(3, -1, -1):
            print(i, end=' ')
            time.sleep(1)
        sys.exit(0)
    elif _l == -2:
        print('Thank you for using this Tool')
        try:
            choice = input('Do you want to run the Tool again? [Y/N] ')[0]
        except Exception:
            print('An Error Occured')
            compare()
        if choice.upper() == 'Y':
            compare()
        else:
            print("Exiting in ", end='')
            for i in range(3, -1, -1):
                print(i, end=' ')
                time.sleep(1)
            sys.exit(0)
    else:
        print('Restarting in ',end='')
        for i in range(3,-1,-1):
            print(i,end=' ')
            time.sleep(1)
        print()
        compare()

comparethread = threading.Thread(compare())
comparethread.start()
