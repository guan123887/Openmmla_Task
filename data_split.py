import os
import shutil
import random
# 按照6:2:2划分
# def get_train_index(arr, train_ratio=0.6, val_ratio=0.2):
#     random.shuffle(arr)
#     l = len(arr)
#     train_index, val_index = int(l*train_ratio), int(l*(train_ratio+val_ratio)) 
#     train_set, val_set, test_set = arr[:train_index], arr[train_index:val_index], arr[val_index:]
#     return train_set, val_set, test_set

# 移动文件夹到新划分训练集和验证集文件夹
# def copy(path, label, train_set, val_set, test_set):
#     train_path = os.path.join(os.getcwd(), 'data/train')
#     val_path = os.path.join(os.getcwd(), 'data/val')
#     test_path = os.path.join(os.getcwd(), 'data/test')
#     if not os.path.exists(train_path):
#         os.makedirs(train_path)
#     if not os.path.exists(val_path):
#         os.makedirs(val_path)
#     if not os.path.exists(test_path):
#         os.makedirs(test_path)
#     for train in train_set:
#         move_file(label, train, train_path, path)
#     for val in val_set:
#         move_file(label, val, val_path, path)
#     for test in test_set:
#         move_file(label, test, test_path, path)

def move_file(label, file_name, path, old_path):
    old_file = os.path.join(old_path, label, file_name)
    new_file = os.path.join(path, label, file_name)
    if not os.path.exists(os.path.join(path, label)):
        os.makedirs(os.path.join(path, label))
    shutil.copyfile(old_file, new_file)

def get_train_index(arr, train_ratio=0.7):
    random.shuffle(arr)
    l = len(arr)
    train_index = int(l*train_ratio)
    train_set, val_set = arr[:train_index], arr[train_index:]
    return train_set, val_set

def copy(path, label, train_set, val_set):
    train_path = os.path.join(os.getcwd(), 'data/train')
    val_path = os.path.join(os.getcwd(), 'data/val')
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(val_path):
        os.makedirs(val_path)
    for train in train_set:
        move_file(label, train, train_path, path)
    for val in val_set:
        move_file(label, val, val_path, path)

# 划分训练集和验证集
def spilt_train_val(path):
    for label in os.listdir(path):
        file_names = []
        for f in os.listdir(os.path.join(path, label)):
            file_names.append(f)
        train_set, val_set = get_train_index(file_names)
        copy(path, label, train_set, val_set)

path = './origin_data/fruit30_train'
spilt_train_val(path)
