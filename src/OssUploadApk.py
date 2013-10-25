#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

import time
from oss.oss_api import *


#ACCESS_ID, SECRET_ACCESS_KEY, APK_BUCKET 默认是空，请填入您申请的正确的ID和KEY.
#HOST = ""
#ACCESS_ID = ""
#SECRECT_ACCESS_KEY = ""
#APK_BUCKET = ""


def uploadApk(apkfile):
    oss = OssAPI(HOST, ACCESS_ID, SECRECT_ACCESS_KEY)

    #列出创建的bucket
    res = oss.get_service()
    if (res.status / 100) == 2:
        body = res.read()
        h = GetServiceXml(body)
        print "bucket list size is: ", len(h.list())
        print "bucket list is: "
        for i in h.list():
            print i
    else:
        print res.status

    headers = {}
    params = {}
    filename = os.path.basename(apkfile)
    print filename
    res = oss.put_object_from_file(APK_BUCKET, filename, apkfile, '', headers, params)
    if (res.status / 100) == 2:
        print "put_object_from_fp OK"
    else:
        print "put_object_from_fp ERROR"
    print res.status
    download_url = "http://"+APK_BUCKET+"."+HOST+"/"+filename;
    print download_url
    return download_url

def printHelp():
    print u'python <base-path>/OssUploadApk <apk file path>'


def main() :
    if len(sys.argv) != 2 :#若命令参数不等于2
        printHelp()	
    else :
    	apkfile = unicode(sys.argv[1] , "gbk") ;
    	if os.path.exists(apkfile) != True:
            printHelp()
            return 2
        uploadApk(apkfile)


if __name__ == '__main__': main()  #程序入口  
