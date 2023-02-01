from modules.constants import *
from modules.utils import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Rate:


    # def upload_file(self):

#         driver = self.driver        
#         WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropzone_file_limits"]')))                 
#         # driver.find_element_by_xpath("//*[@id='dropzone_file_limits']").send_keys("C:/Users/20195/Desktop/image.jpg")
#         # time.sleep(7)
#         driver.execute_script(""" $(document).ready(function () {
#         Dropzone.autoDiscover = false;
#         $("#dZUpload").dropzone({
#         url: "hn_SimpeFileUploader.ashx",
#         addRemoveLinks: true,
#         success: function (file, response) {
#             var imgName = response;
#             file.previewElement.classList.add("dz-success");
#             console.log("Successfully uploaded :" + imgName);
#         },
#         error: function (file, response) {
#             file.previewElement.classList.add("dz-error");
#         }
#         });
#       }); """)        

    def search_history(self, search_type):

        # Hanshiig ognoor haih function
        
        driver = self.driver
        if search_type == 'Шинэчлэгдсэн ханшийн мэдээлэл':
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="date-block"]/div[2]/div[1]/input')))        
            driver.find_element_by_xpath('//*[@id="date-block"]/div[2]/div[1]/input').send_keys('11/20/2019')                        
            driver.find_element_by_xpath('//*[@id="date-block"]/div[2]/div[2]/button').click()            
        elif search_type == 'Хүлээгдэж буй ханшийн мэдээлэл':
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="date-waiting-block"]/div[2]/div[1]/input')))
            driver.find_element_by_xpath('//*[@id="date-waiting-block"]/div[2]/div[1]/input').send_keys('11/20/2019')              
            driver.find_element_by_xpath('//*[@id="date-waiting-block"]/div[2]/div[2]/button').click()
