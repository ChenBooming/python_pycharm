# _*_ coding:utf-8 _*_

from PIL import Image
import os

size = input('Please input size as (long,width):')
filetype = raw_input('Please input one filetype as jpg :')
print '.' + filetype
filelist = os.listdir(os.getcwd())
for filename in filelist:
    name = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    if extension =='.'+filetype:
      im = Image.open(filename)
      print "原文件尺寸和格式："+str((im.size,im.mode,im.format))
      im.thumbnail(size)
      new_filename = name + str(size) + extension
      print "压缩完成，文件名是："+new_filename
      im.save(new_filename,'JPEG')


  
