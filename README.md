## davidBudgetTesting

This is a continuation of [davidBudget](https://github.com/davidlares/davidBudget) repo.

In this opportunity, we built the testing module for this Webapp. Unit and Integration testing with the  **Unittest** module (I think it already comes with Django 2.1.x).

And Functional testing with the `ChromeDriver` software and `Selenium` for **Automated Web Browser Actions**

#### ChromeDriver

"WebDriver is an open source tool for automated testing of web apps across many browsers". It is a B-side software that displays a web browser built by Chromium

Download: [ChromeDriver](http://chromedriver.chromium.org/)

#### Selenium

Works along with ChromeDriver (the previous software runs a server browser) or something like that, and Selenium automates tasks for testing purposes. Please refer to the `funtional_tests/test_project_list_page.py` file.

## Automated testing

It is a piece of code that makes sure that another piece of code is working correctly under a certain condition
Code like normally do - validates is the functionality is correct

#### Unit Test

  This particular test runs (test cycle) one piece independently of other pieces


    `def add_number(first, second):
        return first + second

     def test_add_numbers():
        assert add_numbers(1,2) == 3

      If True = doesn't complain
    `

#### Integration Test

  Tests for multiple pieces together to ensure that they work well with one another

#### Functional Test

  Usually are the tests are that work from the end-user's POV

#### Running Tests

  `./manage.py test [application]`
  `./manage.py test fuctional_tests` This directory should be a Python module

## Virtualenv

  Make sure that for Django 2.x we need to use Py3-based **Virtualenv**, so, commonly, virtualenv is installed and implemented using the Py2 version. To force it, we need to specify the Python version with the `-p` flag:

  `virtualenv -p python3 [name]`

## Installing dependencies

 Just run the `pip install -r requirements.txt`

## Security Update

According to the National Vulnerability Database, the bug CVE-2019-6975 is present in the Django 2.1.0 version.
So, this repo was updated to 2.1.7, which is a bug-free version of it.

You can find more information here: [CVE-2019-6975](https://nvd.nist.gov/vuln/detail/CVE-2019-6975)

## Credits
[David Lares S](https;//twitter.com/davidlares3)

## License
[MIT](https://opensource.org/licenses/MIT)
