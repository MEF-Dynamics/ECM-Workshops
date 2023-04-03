from    selenium.webdriver.chrome.service   import Service
from    selenium.webdriver.chrome.options   import Options
from    selenium.webdriver.common.by        import By
from    selenium                            import webdriver
import  os


obj = webdriver.Chrome()

obj.get("https://www.google.com")

test = obj.find_element(By.XPATH, "//*[@id=\"gb\"]/div/div[2]/a")

test.click()

test2 = obj.find_element(By.XPATH, '//*[@id="identifierId"]')
print(test2)
print(test2.text)
test2.send_keys("merhabalar mef dnymics uyeleri@gmail.com")

input()
"""
['__abstractmethods__', '__class__', '__delattr__', 
 '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
 '__ge__', '__getattribute__', '__getstate__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__le__', 
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 
 '_execute', '_id', '_parent', '_upload', 'accessible_name', 
 'aria_role', 'clear', 'click', 'find_element', 'find_elements', 
 'get_attribute', 'get_dom_attribute', 'get_property', 'id', 
 'is_displayed', 'is_enabled', 'is_selected', 'location', 
 'location_once_scrolled_into_view', 'parent', 'rect', 
 'screenshot', 'screenshot_as_base64', 'screenshot_as_png', 
 'send_keys', 'shadow_root', 'size', 'submit', 'tag_name', 
 'text', 'value_of_css_property']"""