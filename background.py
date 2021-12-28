import os.path
import keyboard # using module keyboard
from datetime import datetime

from pylsl import StreamInfo, StreamOutlet

def checkFile(save_path, fileName):
    #偵測該日期是否已存在檔案，有的話則命名為"日期_1、日期_2..."
    count = 1
    while True:
        path_and_filename = save_path + fileName
        #print(path_and_filename, os.path.exists(path_and_filename))
        if os.path.exists(path_and_filename):
            fileName = fileName.replace(".txt","")
            string = "_" + str(count-1)
            fileName = fileName.replace(string,"")
            fileName = fileName + "_" + str(count) + ".txt"
            count = count + 1
        else:
            fileName.replace("C:/","")
            return fileName

def setFile():
    save_path = 'C:/' # 檔案儲存路徑
    
    # 取得今日日期作為檔案名稱
    today = datetime.today()
    name_of_file = today.strftime('%Y%m%d') #檔案名稱預設為今日日期
    fileName = name_of_file+".txt"
    #檢查檔案是否存在，已存在的話則換新的檔名
    fileName = checkFile(save_path, fileName)

    completeName = os.path.join(save_path, fileName)
    return completeName

def space_pressed(completeName):
    # 取得按下空白鍵的時間，並將時間存檔
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    current_time = current_time+" Space\n"
    
    #將時間存檔
    f = open(completeName,"a")
    f.writelines(current_time)
    f.close()

def main():
    completeName = setFile()

    keypress = False
    while True:
        # 當使用者按下空白鍵的時候
        if keypress and not keyboard.is_pressed(" "):
            '''DO YOUR THING'''
            space_pressed(completeName)
            #beak out of while loop?
            keypress = False
            continue
        elif keyboard.is_pressed(" ") and not keypress:
            keypress = True
            

if __name__ == "__main__":
    main()