def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


f = open('years.txt', 'r')
p = open('victory.txt', 'w')
all_words = map(lambda l: l.split(" "), f.readlines())
for wrd in all_words:
	for subwrd in wrd:
		if(is_number(subwrd) and int(subwrd)>1800):
			p.write(subwrd)
			p.write("\n")
