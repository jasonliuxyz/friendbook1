from friend_data import *

def show_list():
	for p in persons:
		print(f'{p.id}. {p.name}')

def find(name):
	my_persons = [ n for n in persons if name == n.name ]

	count = len(my_persons)
	if count == 0:
		print(f'没有{name}')
	elif count > 1:
		for n in my_persons:
			print(f'{n.id}. {n.name}')
		print(f'有多个{name}，请根据ID重新输入')
			#show_one(name)
	else:
		show_one(my_persons[0])

def find_by_id(id):
	id = int(id)
	person = find_person(id)
	if person == None:
		print(f'无效的ID{id}')
	else:
		show_one(person)

def show_one(person):
	print(f'{person.id}. {person.name}')
	show_records(person)
	show_summary(person)

def show_records(person):
	for r in person.records:
		print(f'{r.person.name}({r.person.id}) 给我 {r.action} {r.score}')

def show_summary(person):
	for sid, score in person.scores.items():
		p = find_person(sid)
		print(f'{p.name}, {score}')


#	for item in names:
#		if name in item:
#			print(item)
