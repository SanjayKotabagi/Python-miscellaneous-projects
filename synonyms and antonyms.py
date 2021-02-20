#First step is to install required libraries 
#Use the follwing to install
#pip install selenium
#import pyttsx3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
word = input("enter word : ")
driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.synonyms.com/synonym/{}".format(word)
driver.get(url)

s = driver.find_element_by_class_name("syns")
value = s.text
print(value)
s = driver.find_element_by_class_name("ants")
value = s.text
print(value)
