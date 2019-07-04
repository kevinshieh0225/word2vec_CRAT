
f = open("WordsCount.txt",encoding="utf-8")
data_counts = {}
line = f.readline()
line = f.readline()
while(line):
    word = line.split()
    data_counts[word[0]] = word[1]
    line = f.readline()
f.close()

key = list(data_counts.keys())
value = list(data_counts.values())


import xlrd
wb = xlrd.open_workbook("教育部辭典庫/dict_revised_2015_20190329_1.xls")
data = {}
table = wb.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data[table.row_values(i)[2]] = 0
wb = xlrd.open_workbook("教育部辭典庫/dict_revised_2015_20190329_2.xls") 
table = wb.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data[table.row_values(i)[2]] = 0
wb = xlrd.open_workbook("教育部辭典庫/dict_revised_2015_20190329_3.xls") 
table = wb.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data[table.row_values(i)[2]] = 0
word = list(data.keys())

f = open("fin_try.txt",'w')
j= 1
ex = []
f.write("標號" + '\t' + "字詞" + '\t' + "詞頻" + '\n')
for i in range(len(key)):
    k = i
    try:
        if (key[i] in word):
            f.write(str(j) + '\t' + str(key[i]) + '\t' + str(value[i]) + '\n')
            j += 1
    except UnicodeEncodeError:     
        f.write(str(j) + '\t' + str(k) + '\t' + str('3') + '\n')
        j+=1
        ex.append(k)
        continue
       
f.close()
#處理編碼問題
