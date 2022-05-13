import json

# class canshu_gesi(object):
#
#     """
#     参数格式转化
#     """
#     def __init__(self):
#         """
#         传入参数
#         :param data:
#         """



def canshu (data):
        data_dict = {item.split("=")[0]: item.split("=")[1] for item in data.split("&")}
        data_new = json.dumps(data_dict, indent=4)

        return data_new
        # print(data_new)
# a =canshu("pageNum=1&pageSize=30&column=szse&tabName=fulltext&plate=szmb&stock=&searchkey=&secid=&category=&trade=&seDate=2021-10-28~2022-04-28&sortName=&sortType=&isHLtitle=true")
# print(a)
# if __name__ == '__main__':
# data = canshu("pageNum=1&pageSize=30&column=szse&tabName=fulltext&plate=szmb&stock=&searchkey=&secid=&category=&trade=&seDate=2021-10-28~2022-04-28&sortName=&sortType=&isHLtitle=true")
# print(data)