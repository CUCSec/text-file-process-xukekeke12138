dic = {}

id_number = '学号：201811113030'
dic[id_number] = 0

with open('log_files/201811113030.log', encoding='utf8') as f:
	for line in f:
		if id_number in line:
			dic[id_number] += 1

print(dic)

f.close()
