import os
import random
import re


def distribute_imgs():
    # list_ = os.listdir('./falcon/imgs')
    # print('num is:\n ', len(list_))
    i = 100
    while (len(os.listdir('./falcon/imgs')) >= 300):
        list_ = os.listdir('./falcon/imgs')
        imgs_list = random.sample(list_, 300)
        print('every list:\n', len(imgs_list))
        os.system(f"mkdir ./imgs_{i}")

        for imgs in imgs_list:
            print(f"move image: {imgs}")
            os.system(f"mv ./falcon/imgs/{imgs} ./imgs_{i}/")
            imgsName = re.findall('(.*).jpg', imgs)
            os.system(f"mv ./falcon/labels/{imgsName[0]}.xml ./imgs_{i}/")
        
        i += 1

    os.system(f"mkdir ./imgs_{i}")
    list_ = os.listdir('./falcon/imgs')
    for imgs in list_:
        print(f"move image: {imgs}")
        os.system(f"mv ./falcon/imgs/{imgs} ./imgs_{i}/")
        imgsName = re.findall('(.*).jpg', imgs)
        os.system(f"mv ./falcon/labels/{imgsName[0]}.xml ./imgs_{i}/")


if __name__ == "__main__":
    distribute_imgs()