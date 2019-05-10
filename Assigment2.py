import re

ActualData=open('regex_sum_372117.txt','r')
ActualText=ActualData.read()
ActualNumbers=re.findall('[0-9]+',ActualText)

number_sum=0
for number in ActualNumbers:
	number_sum+=int(number)

print(number_sum)

