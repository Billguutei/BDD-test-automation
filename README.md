behave -f allure_behave.formatter:AllureFormatter -o reports
allure-2.13.3\bin\allure generate reports html
allure-2.13.3\bin\allure generate reports html --clean

git add .
git commit -m "test"
git pull
git push
git add .
git commit -m "test"
git commit -m "test"
git push


git branch # show branch list
git branch # created ${change, hotfix, impact}-${domain}-${workItem} name branch
git checkout ${branchName}
git status
git add, commit 
git push origin ${branchName}
# BDD-test-automation
