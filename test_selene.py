from selene import browser, have

def test_search():
    browser.open_url('https://www.google.com')
    browser.element('[name="q"]').should(have.text('Google'))
