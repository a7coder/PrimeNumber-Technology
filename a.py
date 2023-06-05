from time import sleep
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def get_Data():

    print()
    print('**************************** Script Started ****************************')
    print()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--log-level=3')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('ignore-certificate-errors')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
   
    
    
    url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'  

    driver.get(url)
    sleep(1)

    print()
    print('**************************** Collecting the Items, Please Wait ****************************')
    print()

    first_element = driver.find_element(By.XPATH, '//*[@id="table_id"]/tbody/tr[1]/td[4]/div/a')
    first_element.click()
    sleep(1)

    data={}
    # ***********************************Iterating over 5 items*************************
    for i in range(5):

        date=driver.find_element(By.XPATH,'//*[@id="view-bid-posting"]/div[2]/div[2]/div/b[2]').text[14:]
        val=driver.find_element(By.XPATH,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text
        text=driver.find_element(By.XPATH,'//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text
       
        data[i]={'est_val':val,'date':date,'desc':text}

        next_btn=driver.find_element(By.XPATH,'//*[@id="id_prevnext_next"]')
        next_btn.click()
        sleep(1)

    print('**************************** Saving Data In a File ****************************')
    print()

    # *********************Saving the file in CSV format **************************
    with open('data.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Est. Value Notes','Closing Date','Description'])

        for k in data:
            writer.writerow([data[k]['est_val'],data[k]['date'],data[k]['desc']])
        

    driver.quit()

    print('**************************** Script Completed ****************************')
    print()

if __name__=='__main__':
     try:
        get_Data()
     except Exception as e:
        print('Something Went Wrong',e)