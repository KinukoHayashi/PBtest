import h5py
import shutil
import numpy as np
import pandas as pd
import pathlib as path
import csv
import os

# 自分で設定する値
n = 13  # 計算回数


# CSVファイル読み込み
data = pd.read_csv("D:/Guest50um/SAC10/PBtest.csv", encoding="shift-jis").values.tolist()  #

# print(data)
# print(data[1][1])
# print(data[0][0])
# 1行目が０、1列目が０
# デバッグ用


# 二次元ファイルにデータを代入

for i in range(n):

    os.mkdir("D:/Guest50um/SAC10_"+str(i+1)+"_data")
    shutil.copy("D:/Guest50um/SAC10_0_data/0.h5",
                "D:/Guest50um/SAC10_"+str(i+1)+"_data/0.h5")
    shutil.copyfile("D:/Guest50um/SAC10_0.dem",
                    "D:/Guest50um/SAC10_"+str(i+1)+".dem")
    shutil.copyfile("D:/Guest50um/SAC10_0.dfg",
                    "D:/Guest50um/SAC10_"+str(i+1)+".dfg")
    shutil.copyfile("D:/Guest50um/SAC10_0.efd",
                    "D:/Guest50um/SAC10_"+str(i+1)+".efd")
    shutil.copyfile("D:/Guest50um/SAC10R_0.ess",
                    "D:/Guest50um/SAC10_"+str(i+1)+".ess")
    shutil.copyfile("D:/Guest50um/SAC10_0.dem",
                    "D:/Guest50um/SAC10R_"+str(i+1)+".ptf")

    outputfile = "F:/Calibration Kits/Dynamic angle of repose test/DAOR/DAOR_" +str(i+1)+"_data/0.h5"
    h5file = h5py.File(outputfile, 'r+')
    dir = "CreatorData/"

    # list作成
    members = []

    # "CreatorData中のすべてのフォルダーを展開してlistに収納
    h5file[dir].visit(members.append)

    # 収納した0番目のフォルダー(0になる)を表示
    print(members[0])
    folder0 = "CreatorData/"+str(members[0])+"/Interactions"
    folder1 = "CreatorData/"+str(members[0])+"/Materials"

    # 元のデータを計算した配列の値に変換する

    h5file[folder0][2, "restitution"] = data[i][1]  # eppH-H
    h5file[folder0][1, "restitution"] = data[i][2]  # eppH-G
    h5file[folder0][0, "restitution"] = data[i][3]  # eppG-G
    h5file[folder0][2, "staticFriction"] = data[i][4]  # μppH-H
    h5file[folder0][1, "staticFriction"] = data[i][5]  # μppH-G
    h5file[folder0][0, "staticFriction"] = data[i][6]  # μppG-G
    h5file[folder0][2, "rollingFriction"] = data[i][7]  # μrppH-H
    h5file[folder0][1, "rollingFriction"] = data[i][8]  # μrppH-G
    h5file[folder0][0, "rollingFriction"] = data[i][9]  # μrppG-G
    #h5file[folder1][0, "density"] = data[i][1]  # d
    #h5file[folder1][0, "poisson"] = data[i][2]  # γpp
    #h5file[folder1][0, "shearMod"] = data[i][4]  # Gpp
    #h5file[folder1][1, "poisson"] = data[i][8]  # γwp
    #h5file[folder1][1, "shearMod"] = data[i][10]  # Gwp

    h5file.flush()
    h5file.close()
 
  
bat_file = " python.bat"
command = bat_file
#command += " " + str(i+1)
os.system(command)
