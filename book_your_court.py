from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#date
import datetime
from dateutil.relativedelta import relativedelta
today_date = datetime.datetime.now()
today = today_date.strftime("%d/%m/%y")

today_day = int(today_date.strftime("%d"))

tomorrow_date = today_date + relativedelta(day= today_day + 1)
tomorrow = tomorrow_date.strftime("%d/%m/%y")

# #set browser
# driver = webdriver.Chrome()
# driver.get("https://bookyourcourt.psm.tu.ac.th/account/login")

# # # define wait time
# wait = WebDriverWait(driver, 10)

#login
def login(id, pwd): #login
    login_id = wait.until(EC.visibility_of_element_located((By.NAME, 'userNameOrEmailAddress')))
    login_id.send_keys(id)

    login_password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    login_password.send_keys(pwd)
    login_password.send_keys(Keys.RETURN)

def select_info(court_index=8, date=today, sport_name="Badminton"): #book info
    #select court
    gym4 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div/div/div/div[1]/div/div/a/div[2]/i')))
    driver.execute_script("arguments[0].click();", gym4)

    ###details
    #sport select
    sport = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[1]/div/select')))
    select_sport = Select(sport)
    select_sport.select_by_visible_text(sport_name)

    #station select
    time.sleep(0.1)
    station = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[2]/div/select')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[2]/div/select')))
    select_station = Select(station)
    select_station.select_by_index(1)

    #court
    time.sleep(0.1)
    court = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[3]/div/select')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[3]/div/select')))
    select_court = Select(court)
    select_court.select_by_index(court_index)

    #-booking date
    time.sleep(0.1)
    date_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Booking_BookingDate"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Booking_BookingDate"]')))
    date_box.clear()
    date_box.send_keys(date)

    #-search button
    time.sleep(0.1)
    search_bt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[5]/button')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[1]/div/div/div[5]/button')))
    search_bt.click()

def book(slot=1): #select book slot
    time.sleep(0.1)
    time_bt = wait.until(EC.presence_of_element_located((By.XPATH, ('//*[@id="kt_wrapper"]/div[2]/ng-component/div/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/button[%d]' % slot))))
    driver.execute_script("arguments[0].click();", time_bt)
    
def confirm(): #to confirm reservation
    time.sleep(0.1)
    confirm_bt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[2]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[2]')))
    confirm_bt.click()
    #driver.execute_script("arguments[0].click();", confirm_bt)
    
def cancle():
    time.sleep(0.1)
    cancle_bt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[1]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_wrapper"]/div[2]/ng-component/div/confirmmodal/div/div/div/div/div/a[1]')))
    cancle_bt.click()

def home(): # back to menu
    time.sleep(0.1)
    menu_bt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_header"]/div/div[2]/default-logo/a/img')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kt_header"]/div/div[2]/default-logo/a/img')))
    menu_bt.click()
    
    

def one_day(day,std_id="", std_pwd="", period=2, sp_name="Badminton", index=8):
    #set browser
    global driver
    driver = webdriver.Chrome()
    driver.get("https://bookyourcourt.psm.tu.ac.th/account/login")

    # # define wait time
    global wait
    wait = WebDriverWait(driver, 5)
    login(id=std_id, pwd=std_pwd)
    select_info(sport_name=sp_name, date=day, court_index=index)
    book(period)
    #cancle()
    confirm()


def two_day_same(std_id="",std_pwd="",period=2, sp_name="Badminton", index=8, test=False):
    #set browser
    global driver
    driver = webdriver.Chrome()
    driver.get("https://bookyourcourt.psm.tu.ac.th/account/login")
    

    # # define wait time
    global wait
    wait = WebDriverWait(driver, 5)
    login(id=std_id, pwd=std_pwd)
    select_info(sport_name=sp_name, date=today, court_index=index)
    book(period)
    if test:
        cancle()
    else:
        confirm()
    home()
    select_info(sport_name=sp_name, date=tomorrow, court_index=index)
    book(period)
    if test:
        cancle()
    else:
        confirm()
    






#-calendar
# span_element = driver.find_element(By.XPATH, '//*[@id="kt_body"]/bs-datepicker-container/div/div/div/div/bs-days-calendar-view/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[1]/span')
# span_text = span_element.text
# print(span_text) --> how to get span text value

