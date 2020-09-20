import requests 
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df

#Initializing variables/Getting BS to read page
page = requests.get("http://www.j-archive.com/showgame.php?game_id=6394") #replace game_id with what game you want
page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')

firstclue_list = soup.find(id="jeopardy_round").find_all(class_ = 'clue')
firstcategory_list = soup.find(id="jeopardy_round").find_all(class_ = 'category_name')
secondclue_list = soup.find(id="double_jeopardy_round").find_all(class_ = 'clue')
secondcategory_list = soup.find(id="double_jeopardy_round").find_all(class_ = 'category_name')
class JeopardyClue:
	def __init__(self, cluetext, answer, money):
		self.cluetext = cluetext
		self.answer = answer
		self.money = money

	def print(self):
		print(self.cluetext + ", " + self.answer + ", " + self.money)
firstcategories = []
secondcategories = [] 
jeopardyround = []
doublejeopardy = []

for category in firstcategory_list:
	print(category.contents)
#Filling arrays with Jeopardy Clues and Category Headers
for clue in firstclue_list:
	cluetext = ''.join(clue.find('td', attrs = {'class' : 'clue_text'}).contents)
	money = clue.find('td', attrs = {'class' : 'clue_value'})
	if money is not None:
		money = money.contents
	else: 
		money = clue.find('td', class_="clue_value_daily_double").contents
	money = ''.join(money)
	clue = clue.find('div', {'onmouseover': True})
	answerindex = clue['onmouseover'].find('correct_response')+18
	lastindex = clue['onmouseover'][answerindex:].find('</em')
	answer = clue['onmouseover'][answerindex:(answerindex+lastindex)]
	clueobject = JeopardyClue(cluetext, answer, money)
	clueobject.print()
for category in secondcategory_list:
	print(category.contents)

for clue in secondclue_list:
	cluetext = ''.join(clue.find('td', attrs = {'class' : 'clue_text'}).contents)
	money = clue.find('td', attrs = {'class' : 'clue_value'})
	if money is not None:
		money = money.contents
	else: 
		money = clue.find('td', class_="clue_value_daily_double").contents
	money = ''.join(money)
	clue = clue.find('div', {'onmouseover': True})
	answerindex = clue['onmouseover'].find('correct_response')+18
	lastindex = clue['onmouseover'][answerindex:].find('</em')
	answer = clue['onmouseover'][answerindex:(answerindex+lastindex)]
	clueobject = JeopardyClue(cluetext, answer, money)
	clueobject.print()