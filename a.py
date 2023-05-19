import pandas as pd
filename = "D:/OneDrive - ueh.edu.vn/NCKH/HuongDanSinhVien/UEH_CV_2023/test.csv"
df = pd.read_csv(filename,encoding= 'unicode_escape')
print(df.to_string()) 
