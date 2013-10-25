#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

import sys
import json
import os
from GetApkDetails import getAllApkDetails
from OssUploadApk import uploadApk

sep = "============================================\n"

def ParseAndUploadApk(apkFileOrDir) :
    fileHandle = open('parse_upload_result.txt','a')
    apkDetailsArray = getAllApkDetails(apkFileOrDir)
    for apkDetails in apkDetailsArray :
        iconArray = apkDetails['iconFileArray']
        nameArray = apkDetails['appNameArray']
        apk_name = apkDetails['apkFileName']
        apk_path = apkDetails['apkFilePath']
        icon = iconArray[0]
        icon_name = os.path.splitext(apk_name)[0]
        icon_ext = os.path.splitext(icon)[1]
        new_icon = os.path.join("./", icon_name+icon_ext)
        open(new_icon, "wb").write(open(icon, "rb").read()) 
        icon_url = uploadApk(new_icon)
        os.remove(new_icon)
        apk_url = uploadApk(apk_path)

        name_array_string = ''
        for name in nameArray:
            if nameArray[-1] == name:
                name_array_string += '%s' % name
            else:
                name_array_string += '%s, ' % name

        print sep
        fileHandle.writelines(sep)
        print "应用名称(app_name): [%s]"%name_array_string
        fileHandle.writelines("应用名称(app_name): [%s]\n"%name_array_string)
        print "安装包名称(package_name): %s"%apkDetails['pkg']
        fileHandle.writelines("安装包名称(package_name): %s\n"%apkDetails['pkg'])
        print "应用版本号(version_code): %s"%apkDetails['versionCode']
        fileHandle.writelines("应用版本号(version_code): %s\n"%apkDetails['versionCode'])
        print "应用版本名称(version_name): %s"%apkDetails['versionName']
        fileHandle.writelines("应用版本名称(version_name): %s\n"%apkDetails['versionName'])
        print "安装包大小(apk_size): %s"%apkDetails['fileSize']
        fileHandle.writelines("安装包大小(apk_size): %s\n"%apkDetails['fileSize'])
        print "应用图标下载链接(icon_url): %s"%icon_url
        fileHandle.writelines("应用图标下载链接(icon_url): %s\n"%icon_url)
        print "安装包下载链接(apk_url): %s"%apk_url
        fileHandle.writelines("安装包下载链接(apk_url): %s\n"%apk_url)
        print sep
        fileHandle.writelines(sep)

    fileHandle.close()
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
