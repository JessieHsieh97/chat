#讀取
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


#計算
def count(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image = 0
	viki_image = 0
	for line in lines: #lines清單裡的每一行
		s = line.split(' ') #遇到空格就split
		time = s[0] #清單中第一格是time
		name = s[1] #清單中第二格是name
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image += 1
			else:
				for m in s[2:]: #清單分割法指從s[2]到清單的最後
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image += 1
			else:
				for m in s[2:]: 
					viki_word_count += len(m)
	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_sticker_count, '個貼圖以及', allen_image, '張圖片	')
	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_sticker_count, '個貼圖以及', viki_image, '張圖片')

		
#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


#mainfunction
def main():
	lines = read_file('LINE-Viki.txt') #將input.txt投入filename
	lines = count(lines)
	# write_file('output.txt', lines)

main() #使用function 進入點
