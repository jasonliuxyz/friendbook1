from person import *

class Record:
	def __init__(self, person, action, score):
		self.person = person
		self.action = action
		self.score = score

if __name__ == '__main__':
	p1 = Person(1, '张三')
	record = Record(p1, '打', -1)

	print(record.score)