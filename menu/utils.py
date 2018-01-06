from urllib3 import PoolManager
from bs4 import BeautifulSoup


def get_entries_for_menu(menu):
    url = menu.url
    parent_element = menu.menu_element
    meal_element = menu.meal_element
    price_element = menu.price_element

    meal_selector = f"{parent_element} > * {meal_element}"
    price_selector = f"{parent_element} > * {price_element}"

    conn_pool = PoolManager()
    downloaded_page = conn_pool.request('GET', menu.url)
    print(downloaded_page._body)

    file_html = downloaded_page._body
    """
    file_html = f.readlines()
    file_html = "".join(file_html)
    """

    soup = BeautifulSoup(file_html, 'html.parser')

    "div#day-selection-tab-1 > * div.single-food > strong"

    meals = soup.select(meal_selector)
    prices = soup.select(price_selector)

    menu_entries = []
    for meal, price in zip(meals, prices):
        menu_entries.append((meal, price))

    return menu_entries
