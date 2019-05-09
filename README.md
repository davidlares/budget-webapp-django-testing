# davidBudget

This repo is a simple budget Webapp for handling projects expenses built with Django 2.x and Vanilla JS.

The whole Django project consists in  CRUDing projects, categories (for the projects) and registering project expenses, just like a personal Wallet. Internally handles pure Django standards and 1:M ORM DB relations.

The frontend is vanilla JS and MaterializeCSS (not a big deal).

## Virtualenv

This is a key concept for running the project on a local environment, feel free to use it as you wish, but I strongly recommend it to isolate working environments and it's dependencies

Just a quick helper here:

`pip install virtualenv`
`virtualenv [name of your project]`

You also can refer to the `requirements.txt` to check the framework version used and other dependencies required.

## Security Update

According to the National Vulnerability Database, the bug CVE-2019-6975 is present on the Django 2.1.0 version of it.
So, this repo was updated to the 2.1.7 which is a bug free version of it.

You can find more information here: [CVE-2019-6975](https://nvd.nist.gov/vuln/detail/CVE-2019-6975)

## Credits

- [David Lares S](https;//twitter.com/davidlares3)

## License

- [MIT](https://opensource.org/licenses/MIT)
