import pyautogui
import time
from PIL import Image
import numpy as np
import tkinter as tk
from threading import Thread

# تحميل الصور المرجعية
image1 = Image.open('image1.png')
image2 = Image.open('image2.png')

# تحويل الصور إلى مصفوفات numpy للمقارنة
image1_array = np.array(image1)
image2_array = np.array(image2)

# إحداثيات المنطقة المحددة (تعديل حسب الحاجة)
x, y, width, height = 100, 100, 300, 200

running = False

def capture_and_compare():
    # التقاط جزء من الشاشة
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot_array = np.array(screenshot)

    # مقارنة الصور
    if np.array_equal(screenshot_array, image1_array) or np.array_equal(screenshot_array, image2_array):
        return True
    return False

def start_program():
    global running
    running = True
    while running:
        if capture_and_compare():
            print("الصورة مطابقة، إيقاف البرنامج لمدة 10 ثواني")
            time.sleep(10)
        else:
            print("الصورة غير مطابقة، البرنامج مستمر في العمل")
        time.sleep(60)  # التحقق كل 60 ثانية

def stop_program():
    global running
    running = False

def start_thread():
    thread = Thread(target=start_program)
    thread.start()

# إنشاء واجهة المستخدم
root = tk.Tk()
root.title("برنامج مقارنة الصور")

start_button = tk.Button(root, text="تشغيل", command=start_thread)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="إيقاف", command=stop_program)
stop_button.pack(pady=10)

root.mainloop()
