from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import cv2
import ddddocr
import time
import csv
import jieba
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件

#PATH = "C:/Users/Mishima Yuna/Desktop/python/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay") #設定網址
action = ActionChains(driver)
legal = driver.find_element("xpath", '//*[@id="legal"]') #按法人按鈕
action.click(legal)
action.perform()
time.sleep(1)
ID2 = driver.find_element("id", 'id2') #抓取統編輸入格
#ID2.clear() #清空預設文字
ID2.send_keys("12208883") #格上統編
path = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final"
driver.save_screenshot('ss.png')
img = cv2.imread("ss.png")
x = 365 # 裁切區域的 x 與 y 座標（左上角）
y = 660
w = 120 # 裁切區域的長度與寬度
h = 40
crop_img = img[y:y+h, x:x+w] # 裁切圖片
#cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('s.png', crop_img)
ocr = ddddocr.DdddOcr()
with open('s.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
#print(res)
#time.sleep(5)
e = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input')
e.clear()  # 清空默认文本
e.send_keys(res)
driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input').click()
#time.sleep(3)
enter = driver.find_element("xpath", '//*[@id="search2"]/img')
action.click(enter)
action.perform()
#print("Recaptcha Success")
# 檔案路徑
file = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/ss.png"
file2 = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/s.png"
os.remove(file)
os.remove(file2)
time.sleep(1)
#ID.send_keys(Keys.RETURN) #按ENTER(這裡註解因網站不支援)
#WebDriverWait(driver, 50).until(
#    EC.presence_of_element_Located((By.CLASS_NAME, "caption_std"))) #確認12208883 ，違規紀錄如下：這句話出來再開始抓取，最多等30秒
a = 0
pathtxt = 'result.csv'
f = open(pathtxt, 'w', encoding='utf-8')
f.write("公司" + "," + "原因" + "\n")
while a <=99:
    date = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[2]')  # 擷取文字從1-10
    reason = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[3]')
    #print(date.text + "  " + reason.text)
    f.write("格上" + "," + reason.text + "\n")
    date2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[2]')
    reason2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[3]')
    #print(date2.text + "  " + reason2.text)
    f.write("格上" + "," + reason2.text + "\n")
    date3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[2]')
    reason3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[3]')
    #print(date3.text + "  " + reason3.text)
    f.write("格上" + "," + reason3.text + "\n")
    date4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[2]')
    reason4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[3]')
    #print(date4.text + "  " + reason4.text)
    f.write("格上" + "," + reason4.text + "\n")
    date5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[2]')
    reason5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[3]')
    #print(date5.text + "  " + reason5.text)
    f.write("格上" + "," + reason5.text + "\n")
    date6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[2]')
    reason6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[3]')
    #print(date6.text + "  " + reason6.text)
    f.write("格上" + "," + reason6.text + "\n")
    date7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[2]')
    reason7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[3]')
    #print(date7.text + "  " + reason7.text)
    f.write("格上" + "," + reason7.text + "\n")
    date8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[2]')
    reason8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[3]')
    #print(date8.text + "  " + reason8.text)
    f.write("格上" + "," + reason8.text + "\n")
    date9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[2]')
    reason9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[3]')
    #print(date9.text + "  " + reason9.text)
    f.write("格上" + "," + reason9.text + "\n")
    date10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[2]')
    reason10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[3]')
    #print(date10.text + "  " + reason10.text)
    f.write("格上" + "," + reason10.text + "\n")
    enter = driver.find_element("xpath", '//*[@id="next"]/img')
    action.click(enter)
    action.perform()
    #print(a)
    a = a + 1
    time.sleep(1)
else:
    #print("Web closed")
    time.sleep(5)
    driver.quit()
f.close

driver = webdriver.Chrome()
driver.get("https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay") #設定網址
action = ActionChains(driver)
legal = driver.find_element("xpath", '//*[@id="legal"]') #按法人按鈕
action.click(legal)
action.perform()
time.sleep(1)
ID2 = driver.find_element("id", 'id2') #抓取統編輸入格
#ID2.clear() #清空預設文字
ID2.send_keys("70364778") #和運統編
path = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final"
driver.save_screenshot('ss.png')
img = cv2.imread("ss.png")
x = 365 # 裁切區域的 x 與 y 座標（左上角）
y = 660
w = 120 # 裁切區域的長度與寬度
h = 40
crop_img = img[y:y+h, x:x+w] # 裁切圖片
#cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('s.png', crop_img)
ocr = ddddocr.DdddOcr()
with open('s.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
#print(res)
#time.sleep(5)
e = driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input')
e.clear()  # 清空默认文本
e.send_keys(res)
driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[1]/div[3]/div/div[2]/form/table/tbody/tr[4]/td/input').click()
#time.sleep(3)
enter = driver.find_element("xpath", '//*[@id="search2"]/img')
action.click(enter)
action.perform()
#print("Recaptcha Success")
# 檔案路徑
file = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/ss.png"
file2 = "C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/s.png"
os.remove(file)
os.remove(file2)
time.sleep(1)
#ID.send_keys(Keys.RETURN) #按ENTER(這裡註解因網站不支援)
#WebDriverWait(driver, 50).until(
#    EC.presence_of_element_Located((By.CLASS_NAME, "caption_std"))) #確認12208883 ，違規紀錄如下：這句話出來再開始抓取，最多等30秒
a = 0
pathtxt = 'result2.csv'
f = open(pathtxt, 'w')
f.write("公司" + "," + "原因" + "\n")
while a <=99:
    date = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[2]')  # 擷取文字從1-10
    reason = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[1]/td[3]')
    #print(date.text + "  " + reason.text)
    f.write("和運" + "," + reason.text + "\n")
    date2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[2]')
    reason2 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[2]/td[3]')
    #print(date2.text + "  " + reason2.text)
    f.write("和運" + "," + reason2.text + "\n")
    date3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[2]')
    reason3 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[3]/td[3]')
    #print(date3.text + "  " + reason3.text)
    f.write("和運" + "," + reason3.text + "\n")
    date4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[2]')
    reason4 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[4]/td[3]')
    #print(date4.text + "  " + reason4.text)
    f.write("和運" + "," + reason4.text + "\n")
    date5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[2]')
    reason5 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[5]/td[3]')
    #print(date5.text + "  " + reason5.text)
    f.write("和運" + "," + reason5.text + "\n")
    date6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[2]')
    reason6 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[6]/td[3]')
    #print(date6.text + "  " + reason6.text)
    f.write("和運" + "," + reason6.text + "\n")
    date7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[2]')
    reason7 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[7]/td[3]')
    #print(date7.text + "  " + reason7.text)
    f.write("和運" + "," + reason7.text + "\n")
    date8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[2]')
    reason8 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[8]/td[3]')
    #print(date8.text + "  " + reason8.text)
    f.write("和運" + "," + reason8.text + "\n")
    date9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[2]')
    reason9 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[9]/td[3]')
    #print(date9.text + "  " + reason9.text)
    f.write("和運" + "," + reason9.text + "\n")
    date10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[2]')
    reason10 = driver.find_element("xpath", '//*[@id="info"]/tbody/tr[10]/td[3]')
    #print(date10.text + "  " + reason10.text)
    f.write("和運" + "," + reason10.text + "\n")
    enter = driver.find_element("xpath", '//*[@id="next"]/img')
    action.click(enter)
    action.perform()
    #print(a)
    a = a + 1
    time.sleep(1)
else:
    #print("Web closed")
    time.sleep(5)
    driver.quit()
f.close



def search_keyword(csv_file, keyword):
    count = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword in seg_list:
                    count += 1

    return count

# 設定CSV檔路徑和關鍵字
csv_file = 'C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/result.csv'
keyword = '格上'

# 呼叫函式並輸出結果
result = search_keyword(csv_file, keyword)
#print(f'中文關鍵字 "{keyword}" 在CSV檔中出現了 {result} 次。')


def search_keyword2(csv_file2, keyword2):
    count2 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file2:
        reader = csv.reader(file2)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword2 in seg_list:
                    count2 += 1

    return count2

keyword2= '停車'
result2 = search_keyword2(csv_file, keyword2)
#print(f'中文關鍵字 "{keyword2}" 在CSV檔中出現了 {result2} 次。')


def search_keyword3(csv_file, keyword3):
    count3 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword3 in seg_list:
                    count3 += 1

    return count3

keyword3= '20'
result3 = search_keyword3(csv_file, keyword3)
#print(f'中文關鍵字 "{keyword3}" 在CSV檔中出現了 {result3} 次。')


def search_keyword4(csv_file, keyword4):
    count4 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword4 in seg_list:
                    count4 += 1

    return count4

keyword4= '40'
result4 = search_keyword4(csv_file, keyword4)
#print(f'中文關鍵字 "{keyword4}" 在CSV檔中出現了 {result4} 次。')


def search_keyword5(csv_file, keyword5):
    count5 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword5 in seg_list:
                    count5 += 1

    return count5

keyword5= '60'
result5 = search_keyword5(csv_file, keyword5)
#print(f'中文關鍵字 "{keyword5}" 在CSV檔中出現了 {result5} 次。')


def search_keyword6(csv_file, keyword6):
    count6 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword6 in seg_list:
                    count6 += 1
    return count6

keyword6= '燈光'
result6 = search_keyword6(csv_file, keyword6)
#print(f'中文關鍵字 "{keyword6}" 在CSV檔中出現了 {result6} 次。')



def search_keyword7(csv_file, keyword7):
    count7 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword7 in seg_list:
                    count7 += 1

    return count7

keyword7= '標線'
result7 = search_keyword7(csv_file, keyword7)
#print(f'中文關鍵字 "{keyword7}" 在CSV檔中出現了 {result7} 次。')


def search_keyword8(csv_file, keyword8):
    count8 = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if keyword8 in seg_list:
                    count8 += 1

    return count8

keyword8= '方向'
result8 = search_keyword8(csv_file, keyword8)
#print(f'中文關鍵字 "{keyword8}" 在CSV檔中出現了 {result8} 次。')

result9 = result - result2 - result3 - result4 - result5 - result6 - result7 - result8

#print(str(result9))




def search_key(csv_file2, key):
    c = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key in seg_list:
                    c += 1

    return c

# 設定CSV檔路徑和關鍵字
csv_file2 = 'C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/result2.csv'
key = '運'

# 呼叫函式並輸出結果
r = search_key(csv_file2, key)
#print(f'中文關鍵字 "{key}" 在CSV檔中出現了 {r} 次。')


def search_key(csv_file2, key2):
    c2 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key2 in seg_list:
                    c2 += 1

    return c2

key2 = '停車'

r2 = search_key(csv_file2, key2)
#print(f'中文關鍵字 "{key2}" 在CSV檔中出現了 {r2} 次。')


def search_key(csv_file2, key3):
    c3 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key3 in seg_list:
                    c3 += 1

    return c3

key3 = '20'

r3 = search_key(csv_file2, key3)
#print(f'中文關鍵字 "{key3}" 在CSV檔中出現了 {r3} 次。')


def search_key(csv_file2, key4):
    c4 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key4 in seg_list:
                    c4 += 1

    return c4

key4 = '40'

r4 = search_key(csv_file2, key4)
#print(f'中文關鍵字 "{key4}" 在CSV檔中出現了 {r4} 次。')


def search_key(csv_file2, key5):
    c5 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key5 in seg_list:
                    c5 += 1

    return c5

key5 = '60'

r5 = search_key(csv_file2, key5)
#print(f'中文關鍵字 "{key5}" 在CSV檔中出現了 {r5} 次。')


def search_key(csv_file2, key6):
    c6 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key6 in seg_list:
                    c6 += 1

    return c6

key6 = '燈光'

r6 = search_key(csv_file2, key6)
#print(f'中文關鍵字 "{key6}" 在CSV檔中出現了 {r6} 次。')



def search_key(csv_file2, key7):
    c7 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key7 in seg_list:
                    c7 += 1

    return c7

key7 = '標線'

r7 = search_key(csv_file2, key7)
#print(f'中文關鍵字 "{key7}" 在CSV檔中出現了 {r7} 次。')


def search_key(csv_file2, key8):
    c8 = 0

    with open(csv_file2, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                seg_list = jieba.cut(value, cut_all=False)
                if key8 in seg_list:
                    c8 += 1

    return c8

key8 = '方向'

r8 = search_key(csv_file2, key8)
#print(f'中文關鍵字 "{key8}" 在CSV檔中出現了 {r8} 次。')

r9 = r - r2 - r3 - r4 - r5 - r6 - r7 - r8



t2 = result2 + r2
t3 = result3 + r3
t4 = result4 + r4
t5 = result5 + r5
t6 = result6 + r6
t7 = result7 + r7
t8 = result8 + r8
t9 = result9 + r9


#print(str(result9))
pathtxt = 'result-EN.csv'
f = open(pathtxt, 'w')
f.write("Reason" + "," + "Go Smart" + "," + "iRent" + "," + "Count" + "\n")
f.write("Illegal Parking" + "," + str(result2) + "," + str(r2) + "," + str(t2) + "\n")
f.write("Speeding Under 20" + "," + str(result3) + "," + str(r3) + "," + str(t3) + "\n")
f.write("Speeding Under 40" + "," + str(result4) + "," + str(r4) + "," + str(t4) + "\n")
f.write("Speeding Under 60" + "," + str(result5) + "," + str(r5) + "," + str(t5) + "\n")
f.write("Running a Red Light" + "," + str(result6) + "," + str(r6) + "," + str(t6) + "\n")
f.write("Not Following Marks" + "," + str(result7) + "," + str(r7) + "," + str(t7) + "\n")
f.write("Not Using Turn Signal" + "," + str(result8) + "," + str(r8) + "," + str(t8) + "\n")
f.write("Other" + "," + str(result2) + "," + str(r9) + "," + str(t9) + "\n")

f.close()



accident = pd.read_csv("C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/result-EN.csv")
#print(accident.head(10))    # 顯示前3筆資料

plt.figure(figsize=(13, 13))  # 顯示圖框架大小

labels = accident["Reason"]  # 製作圓餅圖的類別標籤
separeted = (0, 0, 0.3, 0, 0.3)  # 依據類別數量，分別設定要突出的區塊
size = accident["Count"]  # 製作圓餅圖的數值來源
total = 2087
def make_autopct(size):
    def my_autopct(pct):
        total = sum(size)
        val = int(round(pct*total/100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
plt.pie(size,  # 數值
        labels = labels,  # 標籤
        autopct = make_autopct(size),
        pctdistance = 0.6,  # 數字距圓心的距離,
        textprops = {"fontsize": 12},  # 文字大小
        shadow = True )  # 設定陰影
plt.axis('equal')  # 使圓餅圖比例相等
plt.title("Pie Chart of Violate Traffic Law", {"fontsize": 18})  # 設定標題及其文字大小
plt.legend(loc="best")  # 設定圖例及其位置為最佳
plt.savefig("C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/Pie chart of violate traffic law.png",  # 儲存圖檔
            bbox_inches='tight',  # 去除座標軸占用的空間
            pad_inches=0.0)  # 去除所有白邊

plt.figure(figsize=(16, 10))  # 顯示圖框架大小


x = labels
h = size
plt.bar(x,h)
plt.savefig("C:/Users/Mishima Yuna/Desktop/python/selenium code/CSV Final/Bar chart of violate traffic law.png")
plt.title("Bar Chart of Violate Traffic Law", {"fontsize": 18})# 設定標題及其文字大小

plt.show()
plt.close()  # 關閉圖表