import unittest, requests,json
from lib.log import LOG
from lib.config_operate import ConfigOperate
from parameterized import parameterized, param
from lib.canshu_gesi import canshu

class TestAppSearchClass(unittest.TestCase):
    '''app接口搜索、获取信息类接口'''

    def setUp(self):
        self.url = ConfigOperate('UrlConf').get_config('bj_tuanche', 'url')
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
    #
    @parameterized.expand(
    #     [ param(
    #          "name_null",
    #          data_params={'phone': '15633669988', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
    #                       'groupbyNum': 2001}),
        [ param(data_params=canshu("pageNum=1&pageSize=30&column=szse&tabName=fulltext&plate=szmb&stock=&searchkey=&secid=&category=&trade=&seDate=2021-10-28~2022-04-28&sortName=&sortType=&isHLtitle=true"))
         ])
    def test_sign_params_null(self,data_params):
        '''验证报名各字段参数为空'''
        # data = "pageNum=1&pageSize=30&column=szse&tabName=fulltext&plate=szmb&stock=&searchkey=&secid=&category=&trade=&seDate=2021-10-28~2022-04-28&sortName=&sortType=&isHLtitle=true"
        # data_dict = {item.split("=")[0]: item.split("=")[1] for item in data.split("&")}
        # data_new = json.dumps(data_dict, indent=4)
        uri = '/new/hisAnnouncement/query'
        response = requests.post(self.url + uri, data=data_params, headers=self.headers)
        LOG.info('请求{0},参数{1},状态{2},\n 响应数据{3}'.format(uri, data_params, response, response.text))
        self.assertEqual(response.status_code, 200, '断言响应结果为200')
        # self.assertEqual(response.json()['code'], 100000, '断言结果为100001')
        # self.assertEqual(response.json()['msg'], '参数异常', '断言参数异常')



    def tearDown(self):
            pass

# if __name__ == '__main__':
#     unittest.main()