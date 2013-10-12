import re
import io
with open('gold_summary','r') as f:
    text = f.read()
sentenceEnders = re.compile('[?!.]')
sentenceList = sentenceEnders.split(text)
i = 0
with open('gold_std_summary.html','w') as f:
	f.write(''''<html>\n<head>\n<title>\ngold_Summary</title> </head><body bgcolor="white">\n''')     
	for sentence in sentenceList:
		i += 1
		f.write('''<a name="%d">[%d]</a> <a href="#%d" id=%d>'''%(i,i,i,i) + sentence)
		f.write('\n')
	f.write('</a>\n</body>\n</html>\n')


