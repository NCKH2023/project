import csv
filename = "D:/OneDrive - ueh.edu.vn/NCKH/HuongDanSinhVien/UEH_CV_2023/test.csv"
csvfile=open(filename, 'r')
csvreader = csv.reader(csvfile)
tieude = []
dulieu = []
tieude = next(csvreader) #Dòng này là dòng tiêu đề
for row in csvreader:
    print("%s",row)
