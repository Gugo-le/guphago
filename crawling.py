import requests, re
from bs4 import BeautifulSoup
from collections import OrderedDict

headers = {
    'Referer': 'http://stdweb2.korean.go.kr/search/List_dic.jsp',
    'Content-Type': 'application/x-www-form-urlencoded'
}
r = requests.post('http://stdweb2.korean.go.kr/search/List_dic.jsp', headers=headers, data='idx=&go=&gogroup=1&PageRow=351201&ImeMode=&setJaso=&JasoCnt=0&SearchPart=SP&ResultRows=351201&SearchStartText=&SearchEndText=&JasoSearch=&arrSearchLen=0&Table=words%7Cword&Gubun=0&OrgLang=&TechTerm=&SearchText=&SpCode=9&SpCode=7&SpCode=2&SpCode=1&SpCode=8&SpCode=3')
print('OK')

html = BeautifulSoup(r.text, 'html.parser')
li = html.select('p.exp a')
result = list()
pre = re.compile('^[ㄱ-ㅎ가-힣]+$')

for i in li:
    x = i.text.strip().replace('-', '').replace(' ', '').replace('ㆍ', '').replace('^', '')
    if x and pre.match(x): result.append(x + '\n')

f = open('dict.txt', 'wt', encoding='utf-8')
f.writelines(OrderedDict.fromkeys(result))
f.close()