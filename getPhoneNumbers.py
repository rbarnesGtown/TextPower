from datetime import date
readFilePath = "C:/Data/TextPower/in"
readFileName = "Milsoft_Master.txt"
writeFilePath = "C:/Data/TextPower/out"
now = date.today()
strNow = now.strftime('%Y%m%d')
writeFileName = "phoneNumbers" + "_" + strNow + ".csv"

fw = open(writeFilePath + '/' + writeFileName , 'w',encoding='UTF8', newline='')
fw.write("Tag1\r\n")

with open(readFilePath + '/' + readFileName, 'r') as fr:
    lines = fr.readlines()
    for line in lines:
        firstPhone = line[202:212]
        secondPhone = line[217:227]
        if firstPhone != '          ':
            fw.write(firstPhone + "\r\n")
        if secondPhone != '          ':
            fw.write(secondPhone + "\r\n")
    fr.close()
fw.close()    
