'''
    简单处理csv文件，用open打开
    'w+'新建读写，会将文件清零
    配置一个csv写对象writer来操作csvFile
    写入csv文件的列名
    按行写入，退出保存
'''
import csv

csvFile = open("./files/test.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()