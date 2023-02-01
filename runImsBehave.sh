#!/bin/sh
pip install -r requirements.txt

chmod -R 777 ./ims/drivers/linux/chromedriver

# echo "Frontend selected in use is ${env.frontend}"

# cd ${env.frontend}/
# cd ims/

behave ./ims/feature-service/${serviceName} -f allure_behave.formatter:AllureFormatter -o ./report/ 2>&1

echo "Start Allure"

# allure generate ./report/ --clean -o ./html/

printf 'search khanbank.local' >> /etc/resolv.conf
