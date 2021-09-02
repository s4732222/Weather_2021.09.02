from pyautogui import sleep
from pynput import keyboard
from pynput.keyboard import Key
import pywinauto
import time
import pynput
import win32api
import win32con
import pyautogui as pag



def OpenGis():

  def press_shift(ctr):
    with ctr.pressed(
      pynput.keyboard.Key.shift
    ):pass

  def press_Ctrl_O(ctr):
    with ctr.pressed(
      pynput.keyboard.KeyCode.from_vk(17),
      'o'
    ):pass

  def press_keydown(ctr):
    ctr.press(Key.down)
    ctr.release(Key.down)

  def press_enter():
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

  def press_model():
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(9,0,0,0)
    win32api.keybd_event(9,0,0,0)
    win32api.keybd_event(17,0,0,0)

  def validate():
    win32api.keybd_event(16,0,0,0)
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)

    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(17,0,0,0) 
    win32api.keybd_event(16,0,0,0)
  
  def run():
    win32api.keybd_event(16,0,0,0)
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(82,0,0,0)

    win32api.keybd_event(82,0,0,0)
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(16,0,0,0)

  

  
  
  #打開GIS
  app = pywinauto.application.Application()
  app.start("C:/Program Files/ArcGIS/Pro/bin/ArcGISPro.exe")
  time.sleep(5)
  print("開啟GIS成功")

  #keyboard-controller
  ctr = pynput.keyboard.Controller()

  #將英文轉成中文
  press_shift(ctr)

  time.sleep(7)

  #使用CTRL+O快捷鍵開起工作目錄
  press_Ctrl_O(ctr)

  time.sleep(3)

  #於工作目錄輸入欲開啟檔案
  ctr.type("自動化")

  time.sleep(1)

  #down
  press_keydown(ctr)

  time.sleep(1)

  #於工作目錄輸入ENTER，選取自動化
  press_enter()

  time.sleep(1)

  #於工作目錄輸入ENTER，開啟自動化
  press_enter()

  time.sleep(15)
  
  #按下ctrl+tab，更換自MODEL
  press_model()

  time.sleep(10)

  #按下ENTER，選取model
  press_enter()

  time.sleep(5)

  #滑鼠游標移至中間
  pag.click(1000,600,button='left')


  time.sleep(5)

  #使用Validate初始化(ctrl+shift+v)
  validate()
  print('Validate初始化')

  time.sleep(5)

  #run_model(ctrl+shift+R)
  run()
  print('run')

  win32api.keybd_event(17,0,0,0)
  win32api.keybd_event(16,0,0,0)
  win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
 
OpenGis()
