from person import *

persons = [] 
records = [] 

def load_data():
	load_names()
	load_records()


def load_names():
	with open('names.txt', 'r', encoding='utf-8') as rfile:
		lines = rfile.readlines()
		for name in lines:
			id, name = name.split(',')
			persons.append(Person(int(id), name.strip()))

def load_records():
	with open('records.txt', 'r', encoding='utf-8') as rfile:
		lines = rfile.readlines()
		for line in lines:
			#5, 龙四, 白嫖, 36, 高五, -1
			point = line.split(',')
			p1 = find_person(point[0])
			p2 = find_person(point[3].strip())
			if p1 == None  or p2 == None:
				continue
			action = point[2].strip()
			score = int(point[5].strip())

			r = Record(p1, action, score)
			p2.add_record(r)


def find_person(id):
	ps = [p for p in persons if p.id == int(id)]
	if len(ps):
		return ps[0]


load_data()
#for p in persons:
#	print(f'{p.name} has {len(p.records)}')
