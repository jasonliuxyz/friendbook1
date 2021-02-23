import random

xings_str = "李，王，张，刘，陈，杨，黄，赵，周，吴，徐，孙，朱，马，胡，郭，林，何，高，梁，郑，罗，宋，谢，唐，韩，曹，许，邓，萧，冯，曾，程，蔡，彭，潘，袁，于，董，余，苏，叶，吕，魏，蒋，田，杜，丁，沈，姜，范，江，傅，钟，卢，汪，戴，崔，任，陆，廖，姚，方，金，邱，夏，谭，韦，贾，邹，石，熊，孟，秦，阎，薛，侯，雷，白，龙，段，郝，孔，邵，史，毛，常，万，顾，赖，武，康，贺，严，尹，钱，施，牛，洪，龚"
mings_str = "大，二，三，四，五，六，七，八，九"
add_score_things = "点赞，赞美，投币，充电，打电话，帮助，送礼物"
reduce_score_things = "骂，打，欺骗，白嫖，要挟"

names = []
records = [((1, '张三'), '骂了', (2, '李四'), -1)]
name_dict = {}
record_dict = {}
score_dict = {} #{张三: {李四: 8, 王五：1}}

def mock_names():
	xings = xings_str.split('，')
	mings = mings_str.split('，')
	for i in range(100):
		xing = random.choice(xings)
		ming = random.choice(mings)
		names.append((i+1, xing+ming))

def mock_records():
	good_things = add_score_things.split('，')
	bad_things = reduce_score_things.split('，')
	things = good_things + bad_things

	for i in range(100000):
		name1 = random.choice(names)
		name2 = random.choice(names)
		thing = random.choice(things)
		if thing in good_things:
			score = 1
		elif thing in bad_things:
			score = -1

		records.append((name1, thing, name2, score))

def build_record_dict():
	for r in records:
		id = r[2][0]
		if id in record_dict:
			my_records = record_dict[id]
			my_records.append(r)
		else:
			record_dict[id] = [r]

def build_score():
	for r in records:
		passive_id = r[2][0]
		acctive_id = r[0][0]
		if passive_id in score_dict:
			scores = score_dict[passive_id]
			if acctive_id in scores:
				scores[acctive_id] += r[3] 
			else:
				scores[acctive_id] = r[3]
		else:
			score_dict[passive_id] = {acctive_id:r[3]}

	for id in score_dict:
		scores = score_dict[id]
		sortd_score = {k:v for k,v in sorted(scores.items(), key=lambda item: item[1])}
		score_dict[id] = sortd_score

def build_name_dict():
	for n in names:
		name_dict[n[0]] = n[1]

def mock_data():
	mock_names()
	mock_records()
	build_record_dict()
	build_name_dict()
	build_score()

mock_data()
