diem = open("C:/Users/Long/he/sesison1/code.csv",mode = "r",encoding="utf-8-sig")

ghi = open("C:/Users/Long/he/sesison1/code2.csv",mode = "w",encoding = "utf-8-sig")

header = diem.readline()
ghi.write(header.strip() + ";DTB;HL\n")
row = diem.readline()
while row != "":
    row_list = row.split(";")
    Tv = float(row_list[2])
    Av = float(row_list[3])
    T = float(row_list[4])
    TBC = (Tv+Av+T)/3
    TBC = round(TBC,1)
    HL = ""
    if TBC >=5.0:
        HL = "Hoàn thành"
    if TBC >=9.0:
        HL = "Tốt"
    row_new = row.strip() + ";" + str(TBC) + ";" + HL +"\n"
    ghi.write(row_new)
    print(TBC)
    row = diem.readline()