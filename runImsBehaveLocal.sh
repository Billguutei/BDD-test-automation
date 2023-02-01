#!/bin/sh


# pip install -r requirements.txt


# echo "Frontend selected in use is ${env.frontend}"

# cd ${env.frontend}/

cd IMS/

echo "Check if chrome driver is present"

# ls
# ls -lrt /opt/workspace/
pwd

behave -f allure_behave.formatter:AllureFormatter -o ./report/

allure generate ./report/ --clean -o ./html/

printf 'search khanbank.local' >> /etc/resolv.conf
