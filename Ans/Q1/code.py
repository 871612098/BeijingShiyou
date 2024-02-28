"""
外汇牌价查询

这是中国银行外汇牌价网站：https://www.boc.cn/sourcedb/whpj/

请使用python3 和 selenium库写一个程序，实现以下功能：

输入：日期、货币代号

输出：该日期该货币的“现汇卖出价”

示例：
python3 yourcode.py 20211231 USD
输出：636.99
该日期有很多个价位，只需要输出任意一个时间点的价位即可。
货币代号为USD、EUR这样的三位英文代码，请参考这里的标准符号：https://www.11meigui.com/tools/currency

要求：

1， 将selenium爬到的数据打印到一个result.txt 文件里

2， 代码规范，注释清晰，变量命名合理易读，无不必要的冗余

3，有适当的异常处理

"""
import sys

from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
#制作一个检索表，方便查询值
def search_code(code):
    # 货币代号和对应的英文代码
    currency_dict = {
        "港币": "HKD",
        "美元": "USD",
        "瑞士法郎": "CHF",
        "德国马克": "DEM",
        "法国法郎": "FRF",
        "新加坡元": "SGD",
        "瑞典克朗": "SEK",
        "丹麦克朗": "DKK",
        "挪威克朗": "NOK",
        "日元": "JPY",
        "加拿大元": "CAD",
        "澳大利亚元": "AUD",
        "欧元": "EUR",
        "澳门元": "MOP",
        "菲律宾比索": "PHP",
        "泰国铢": "THB",
        "新西兰元": "NZD",
        "韩元": "KRW",
        "卢布": "RUB",
        "林吉特": "MYR",
        "新台币": "TWD",
        "西班牙比塞塔": "ESP",
        "意大利里拉": "ITL",
        "荷兰盾": "NLG",
        "比利时法郎": "BEF",
        "芬兰马克": "FIM",
        "印度卢比": "INR",
        "印尼卢比": "IDR",
        "巴西里亚尔": "BRL",
        "阿联酋迪拉姆": "AED",
        "南非兰特": "ZAR",
        "沙特里亚尔": "SAR",
        "土耳其里拉": "TRY"
    }
    try:
        result_name = {v:k for k, v in currency_dict.items() if v == code}
        return result_name
    except Exception as e:
        print("请检查输入的货币代码，存在异常！")
        print(e)

def format_date(date_str):
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    select_date = datetime(year, month, day).strftime("%Y-%m-%d")
    return select_date

def get_rate(date,input_code):
    #创建浏览器对象
    driver = webdriver.Chrome()
    try:
        #访问网站
        driver.get('https://www.boc.cn/sourcedb/whpj/')

        #等待加载网页
        time.sleep(1)

        # 转成日期格式
        date = format_date(date)
        print(date)

        # 获取货币名称
        request_code = search_code(input_code)
        request_name = request_code[input_code]

        # 输入日期
        element = driver.find_element(By.XPATH, '//*[@id="erectDate"]')
        element.clear()
        element.send_keys(date)
        element = driver.find_element(By.XPATH, '//*[@id="nothing"]')
        element.clear()
        element.send_keys(date)
        print(date)

        # 选择货币
        currency_select = driver.find_element(By.XPATH, '//*[@id="pjname"]')
        currency_select.click()
        currency_option = driver.find_element(By.XPATH, f'//*[@id="pjname"]/option[text()="{request_name}"]')
        currency_option.click()
        print(request_name)
        # 点击查询按钮
        query_button = driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
        query_button.click()

        # 等待查询结果加载完成
        time.sleep(1)
        # 获取现汇卖出价
        price = driver.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text
        print(price)
        return price
    except Exception as e:
        print("抱歉，存在异常！请重新尝试！")
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    #获取命令行参数
    date = sys.argv[1]
    currency_code = sys.argv[2]

    # date = '20211231'
    # currency_code = 'USD'

    name = search_code(currency_code)
    print(name)
     # 查询外汇牌价
    price = get_rate(date, currency_code)

    #将结果保存到result.txt文件
    with open('result.txt', 'w') as f:
        f.write(f"该日期 {date}的 {currency_code}的价格为: {price}")
        f.close()


