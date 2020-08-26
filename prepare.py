import os, os.path
import json
from shutil import copyfile
# copyfile(src, dst)
# from os import path
def create_metadata():
    imgs = []
    gt = []
    path = "/home/nhanvu/WorkSpace/OCR/Text_Detection/SROIE2019-20200826T034924Z-001/SROIE2019/0325updated.task1train(626p)"
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        # imgs.append(os.path.join(f))
        label = f.split('.')[0] + '.txt'
        if os.path.exists(path+'/'+label):
            # print(path+'/'+label)
            imgs.append(f)
            gt.append(label)
        # break
    print (len(imgs))
    print(len(gt))
    imgs_train = []
    gt_train = []
    imgs_val = []
    gt_val = []
    for i in range(len(imgs)):
        # print(i)
        if i < 620:
            imgs_train.append(imgs[i])
            gt_train.append(gt[i])
        else:
            imgs_val.append(imgs[i])
            gt_val.append(gt[i])

    print(len(imgs_train))
    print(len(imgs_val))
    data_train = {
        "images_path": imgs_train,
        "box_path": gt_train
    }
    data_val = {
        "images_path": imgs_val,
        "box_path": gt_val
    }

    with open('train.json', 'w') as outfile:
        json.dump(data_train, outfile)
    with open('val.json', 'w') as outfile:
        json.dump(data_val, outfile)
    # with open('train.json') as json_file:
    #     data = json.load(json_file)
    #     print(data['images_path'][0])
def copy_data_train(source_path, dest_path, metadata):
    data = None
    with open(metadata) as json_file:
        data = json.load(json_file)
    for name in data['images_path']:
    # name = data['images_path'][0]
        copyfile(source_path+name,dest_path+'img/'+name)
    for name in data['box_path']:
        copyfile(source_path+name,dest_path+'gt/'+name)
# def copy_data_test(source_path, dest_path)
if __name__ == "__main__":
    source_path = "/home/nhanvu/WorkSpace/OCR/Text_Detection/SROIE2019-20200826T034924Z-001/SROIE2019/0325updated.task1train(626p)/"
    dest_path = "/home/nhanvu/WorkSpace/OCR/Text_Detection/Receipt/val/"
    metadata = '/home/nhanvu/WorkSpace/OCR/Text_Detection/PAN.pytorch-master/val.json'
    copy_data_train(source_path,dest_path,metadata)