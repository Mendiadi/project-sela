
# UI Testing Automation Project.

In this project im testing a small part of the UI of automation practice store site.
im using selenium lib.

## INFO:
if test failed you can see a screenshot in allure reports
### Example:
Screenshot failed test example in allure:

![alt text](https://github.com/Mendiadi/project-sela/blob/selenium/exm_img.PNG?raw=true)

### Markers:
    valid Marker - will run only valid tests.
    invalid Marker - will run only invalid tests.


## HOW TO RUN:

### Configuration file:
in the test folder you can find init.json file
it a configuration file for the test data
you can change the login info (email,password)
and also url and browser.
make sure you change it by the rules.

#### run default:
*** Make sure u run it from tests folder - cd ./tests
and the driver.exe is there otherwise program will not find driver path
will run all tests and use default settings - Chrome browser

```commandline
    pytest test_my_store.py
```

#### Run specific marker:

##### valid:
```commandline
    pytest -m valid test_my_store.py
```
##### invalid:
```commandline
    pytest -m invalid test_my_store.py
```

### Allure reports:
```commandline
    pytest --alluredir=reports\ test_my_store.py
```
```commandline
    allure serve reports/
```