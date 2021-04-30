import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome();
url="http://automationpractice.com/index.php";

driver.get(url);
print("navigate to the url"+url+"successfully");
driver.maximize_window();
print("maximize the browser successfully");
driver.find_element_by_xpath("//*[@title='Log in to your customer account']").click();
time.sleep(3);
print("clicked on login button");
driver.find_element_by_xpath("//input[@id='email']").send_keys("b4.shrikant.sakure@gmail.com");
time.sleep(3);
print("enter the username");
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("Ambition123!@#");
time.sleep(3);
print("enter the password");
driver.find_element_by_xpath("//button[@id='SubmitLogin']").click();
time.sleep(3);
print("clicked on signin button");


#method to search element
def search():
    search = "dress";
    driver.find_element_by_xpath("//input[@id='search_query_top']").send_keys(search);
    print(" entered the search name as " + search)
    time.sleep(6);
    driver.find_element_by_xpath("//button[@name='submit_search']").click();
    time.sleep(6);
    print(" item search successfully");
search();

# first item
driver.find_element_by_xpath("(//a[@title='Printed Summer Dress'])[2]").click();
time.sleep(10);
print("clicked on printed summer dress successfully");
def add_element_to_cart():
    time.sleep(5);
    driver.find_element_by_xpath("//*[@type='submit' and @name='Submit']").click();
    time.sleep(8);
    print("added to the cart");
    driver.find_element_by_xpath("//a[@title='Proceed to checkout']").click();
    time.sleep(8);
    print("proceed for the checkout for printed summer dress");
add_element_to_cart();
def delete_element_from_cart():
    driver.find_element_by_xpath("//*[@title='Delete']").click();
    time.sleep(6);
    print("order deleted for printed summer dress");

delete_element_from_cart();

# second item search and add to cart
search();
time.sleep(5);
driver.find_element_by_xpath("(//*[@title='Printed Dress'])[6]").click();
time.sleep(9);
add_element_to_cart();
delete_element_from_cart();

#add third element to the cart

search();
time.sleep(5);
driver.find_element_by_xpath("(//*[@title='Printed Summer Dress'])[5]").click();

time.sleep(9);
add_element_to_cart();
delete_element_from_cart();






















