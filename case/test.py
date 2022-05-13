# import json,os
#
# # data = "pageNum=1&pageSize=30&column=szse&tabName=fulltext&plate=szmb&stock=&searchkey=&secid=&category=&trade=&seDate=2021-10-28~2022-04-28&sortName=&sortType=&isHLtitle=true"
# # data_dict = {item.split("=")[0]: item.split("=")[1] for item in data.split("&")}
# #
# # data = json.dumps(data_dict, indent=4)
# # print(data)
# #
# # cwd_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# # conf_path = os.path.join(cwd_path, 'config')
# # file_path = os.path.join(conf_path, '%s.ini' %DB_config )
# # # self.file_path = file_path
# # # self.config = ConfigParser()
# # print(cwd_path)
# # print(conf_path)
# # from lib.config_operate import ConfigOperate
# # from lib.log import LOG
# # import pymysql
#
#
# # import pymysql
# #
# # conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='root')
# # cursor=conn.cursor()
# # print(conn)
# # print(cursor)
# #
# # cursor.close()
# # conn.close()
# #
#
#
# import sys
# a=sys.argv[0]
# # print(a)
#
# import datetime
#
# today = datetime.datetime.today()
# username = input('Please input your name：')
# welcome  = '欢迎 %s 登录，今天的日期是 %s'%(username,today)
# print(welcome)