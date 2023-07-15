file = open ("datatest.csv", mode="r", encoding="utf-8-sig")
file_new = open("rating_new.csv", mode="w", encoding="utf-8-sig")

header = file.readline()
file_new.write(header.strip() + "xếp hạng chất lượng\n")

row = file.readline()
while row != "":
	row_list = row.split(",")

	epi = str (row_list[2])
	rating = str (row_list[3])
	member = str (row_list[4])

	rank = ""
	if rating >= 9.0:
		rank = "Cao"
	if rating >=8.0 and rating <9.0:
		rank = "Trung "
	else:
		rank = "Thấp"

	row_new = row.strip() + "," + rate + "\n"

	file_new.write(row_new)
	row = file.readline()
