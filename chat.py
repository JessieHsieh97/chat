#讀取
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#轉換
def convert(lines):
	new = []
	for line in lines: #lines清單裡的每一行
		if line == 'Allen': #如果line完全等於Allen
			person = 'Allen'#就把Allen這個人名存進person
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + line)
	return new

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#mainfunction
def main():
	lines = read_file('input.txt') #將input.txt投入filename
	lines = convert(lines)
	write_file('output.txt', lines)

main() #使用function 進入點

