# playwright
playwright sandbox

`python -m venv .venv --system-site-packages`

`source .venv/Scripts/activate`

`playwright install`

`playwright codegen --viewport-size=800,600 https://naveenautomationlabs.com/opencart/`

`playwright codegen -o lesson.py https://naveenautomationlabs.com/opencart/`

`pytest --headed tests/test_demo.py `

`pytest --headed --browser webkit --browser firefox`

`pytest --slowmo 1000`

`pytest --video=on`
