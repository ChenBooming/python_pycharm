# -*- coding:utf-8 -*- 
#from __future__ import with_statement 
import math
import os
import ConfigParser

#默认步数和角度
step=0
angle=0

#文件路径
#currentpath = os.getcwd()
#print currentpath

#文件操作
# f = open('config.cfg','w')
# f.write('[config]\n')
# f.write('x=0\ny=0\nstep=0\nangle=0\n')
# f.close()

#生成文件设置
def reload_location():
  cfd = open('config.cfg','w')
  conf = ConfigParser.ConfigParser()
  conf.add_section('location')
  conf.set('location','x',0)
  conf.set('location','y',0)
  conf.write(cfd)
  cfd.close()

#设置行动结果
def set_location(newLocation):
  cfd = open('config.cfg','a')
  conf = ConfigParser.ConfigParser()
  try:
    conf.set('location','x',newLocation[0])
    conf.set('location','y',newLocation[1])
  except Exception, e:
    conf.add_section('location')
  finally:
    conf.set('location','x',newLocation[0])
    conf.set('location','y',newLocation[1])
  conf.write(cfd)
  cfd.close()

#读取文件设置
def get_location():
  conf = ConfigParser.ConfigParser()
  conf.read('config.cfg')
  #print conf.options('location')
  x = conf.get('location','x')
  y = conf.get('location','y')
  #print x,y
  return x,y

#定位函数
def moved_location(oldLocation,movement):
  newx = float(oldLocation[0]) + movement[0]*math.cos(movement[1])
  newy = float(oldLocation[1]) + movement[0]*math.sin(movement[1])
  return round(newx),round(newy)

#获取行动
def get_movement():
  step=int(raw_input("step:"))
  angle=math.pi/(180/int(raw_input("angle:")))
  movement =(step,angle)
  return movement


#主函数体
if os.path.exists('config.cfg'):
  #print 'exist'
  pass
else:
  reload_location()

#反馈老位置
oldLocation = get_location()
print ('原坐标：%s') % str(oldLocation)

#获取行动
movement = get_movement()
print ('往%.2f度方向走了%s步') % (movement[1],movement[0])

#反馈新位置
newLocation = moved_location(oldLocation,movement)
print ('新坐标：%s') % str(newLocation)

#文件存备份
set_location(newLocation)
#print 'set success'

