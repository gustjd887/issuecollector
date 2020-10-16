from issue_postgres import IssueDB

db = IssueDB()

#전체 랭킹
total_list = db.select("""select id, site, (reply + "like" / hit::float) from issue_issue where date > current_date - interval '1' day;""")

total_list.sort(key=lambda rank_rate: rank_rate[2])
total_rank = ",".join(str(id[0]) for id in total_list[:10])

db.update("""update issue_community set rank = '%s' where site='total'""" % total_rank)

#오유 랭킹
ou_list = []
for list in total_list:
    if list[1]=='ou': ou_list.append(list)

ou_list.sort(key=lambda rank_rate: rank_rate[1])
ou_rank = ",".join(str(id[0]) for id in ou_list[:10])

db.update("""update issue_community set rank = '%s' where site='ou'""" % ou_rank)

#클리앙 랭킹
cl_list = []
for list in total_list:
    if list[1]=='cl': cl_list.append(list)

cl_list.sort(key=lambda rank_rate: rank_rate[1])
cl_rank = ",".join(str(id[0]) for id in cl_list[:10])

db.update("""update issue_community set rank = '%s' where site='cl'""" % cl_rank)

#뽐뿌 랭킹
pp_list = []
for list in total_list:
    if list[1]=='pp': pp_list.append(list)

pp_list.sort(key=lambda rank_rate: rank_rate[1])
pp_rank = ",".join(str(id[0]) for id in pp_list[:10])

db.update("""update issue_community set rank = '%s' where site='pp'""" % pp_rank)

#랭킹 업데이트
# print("""update issue_rank_board_rank set total_rank = '%s', ou_rank = '%s', cl_rank = '%s', pp_rank = '%s' where id=1""".format(total_rank, ou_rank, cl_rank, pp_rank))
# db.update("""update issue_community set total_rank = %s, ou_rank = %s, cl_rank = %s, pp_rank = %s where id=1""", total_rank, ou_rank, cl_rank, pp_rank)
# db.update("""update issue_community set total_rank = %s, ou_rank = %s, cl_rank = %s, pp_rank = %s where id=1""", total_rank, ou_rank, cl_rank, pp_rank)
db.close()
