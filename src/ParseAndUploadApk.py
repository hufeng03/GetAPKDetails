#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

import sys
import json
import os
from GetApkDetails import getAllApkDetails
from OssUploadApk import uploadApk

def ParseAndUploadApk(apkFileOrDir) :
    apkDetailsArray = getAllApkDetails(apkFileOrDir)
    for apkDetails in apkDetailsArray :
        iconArray = apkDetails['iconFileArray']
        nameArray = apkDetails['appNameArray']
        apk_name = apkDetails['apkFilePath']
        print apk_name
        print iconArray
        print nameArray
        print apkDetails['pkg']
        print apkDetails['versionCode']
        print apkDetails['versionName']
        print apkDetails['fileSize']
        icon = iconArray[0]
        name = nameArray[0]
        icon_name = os.path.split(icon)[1]
        icon_ext = os.path.splitext(icon)[1]
        new_icon = os.path.join("./", name+icon_ext)
        print new_icon
        open(new_icon, "wb").write(open(icon, "rb").read()) 
        uploadApk(new_icon)
        os.remove(new_icon)
        uploadApk(apk_name)

    jsonResult = json.dumps(apkDetailsArray)
    return jsonResult

def printHelp():
    print u'python <base-path>/ParseAndUploadApk <apk file/dir path>'


def main() :
    if len(sys.argv) != 2 :#若命令参数不等于2
        printHelp()	
    else :
    	apkFileOrDir = unicode(sys.argv[1] , "gbk") ;
    	if os.path.exists(apkFileOrDir) != True:
            printHelp()
            return 2

        jsonResult = ParseAndUploadApk(apkFileOrDir) 

        #print jsonResult

if __name__ == '__main__': main()  #程序入口  
