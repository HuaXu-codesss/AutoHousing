import requests
import time

# url：查看浏览器的开发者工具中的网络一栏，查看某个http请求中的请求网址
url = "http://gmis.xjtu.edu.cn/pyxx/pygl/pkjlcx/listpk?sEcho=1&iColumns=11&sColumns=&iDisplayStart=0&iDisplayLength=15&mDataProp_0=RN&mDataProp_1=KCBH&mDataProp_2=KCMC&mDataProp_3=BJMC&mDataProp_4=KCXF&mDataProp_5=KCZXS&mDataProp_6=ZJJSMC&mDataProp_7=SKSJ&mDataProp_8=RNRS&mDataProp_9=XKRS&mDataProp_10=KKFS&yxsh=&xq_SELECTNAME=2023%25E7%25A7%258B&xq=49&sftsk=&kcbh=%25E7%25AE%2597%25E6%25B3%2595&_=1691977215985"

# cookie信息也在http请求报文中，直接复制粘贴
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Cookie":"JSESSIONID=50D430C753AF18DBE5F98C47276DA93D.pyxx_server5.pyxx_server5; _ga=GA1.3.1453050705.1691551101"}

while True:
    # 查看当前时间
    print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(time.time())))
    
    # 注意HTTP请求的方法，get/post
    response = requests.get(url, headers = header)
    
    # 查看响应状态码
    print (response.status_code)
    # 查看响应头部字符编码
    print (response.encoding)
    # 查看完整url地址
    # print (response.url)
    
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print("--------返回信息如下--------\n", response.text)
    print("\n")
    time.sleep(1)
