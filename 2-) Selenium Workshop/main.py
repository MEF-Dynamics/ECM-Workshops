from Web import Web
from    selenium.webdriver.common.by        import By


web = Web(isHidden=False)

web.open_web_page("https://10fastfingers.com/typing-test/turkish")

element = web.create_element('//*[@id="row1"]')

for i in range(2,10) :

    test = f'//*[@id="row1"]/span[{i}]'

    print(web.create_element(test).text)

