from friend_data import *

def show_list():
	for i in names:
		print(f'{i[0]}. {i[1]}')

def find(name):
	my_names = [ n for n in names if name == n[1]]

	count = len(my_names)
	if count == 0:
		print(f'没有{name}')
	elif count > 1:
		for n in my_names:
			print(f'{n[0]}. {n[1]}')
		print(f'有多个{name}，请根据ID重新输入')
			#show_one(name)
	else:
		show_one(my_names[0])

def find_by_id(id):
	id = int(id)
	my_names = [ n for n in names if id == n[0]]
	if len(my_names) == 0:
		print(f'无效的ID{id}')
	else:
		show_one(my_names[0])

def show_one(person):
	print(f'{person[0]}. {person[1]}')
	#show_records(person[0])
	show_summary(person[0])

def show_records(id):
	if id in record_dict:
		my_records = record_dict[id]
		for r in my_records:
			print(f'{r[0][1]}({r[0][0]}) 给我 {r[1]} {r[3]}')
def show_summary(id):
	if id in score_dict:
#		scores = score_dict[id]
#		for sid in scores:
#			score = scores[sid]
#			print(f'{name_dict[sid]}, {score}')

		scores = score_dict[id]
		for sid, score in list(scores.items())[-1:-6:-1]:
			print(f'{name_dict[sid]}, {score}')


#	for item in names:
#		if name in item:
#			print(item)
