import allure
from pages.login_page import LoginPage
from pages.add_page import AddPage


@allure.title("Сценарий: Оформление заказа и проверка итоговой суммы")
@allure.description(
    "Тест проверяет полный путь пользователя: "
    "авторизация, добавление товаров, переход в корзину, оформление заказа."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_and_total(driver):
    url = "https://www.saucedemo.com"
    login_page = LoginPage(driver)
    add_page = AddPage(driver)

    with allure.step("Шаг 1: Авторизация"):
        driver.get(url)
        login_page.login(username="standard_user", password="secret_sauce")
        assert "Swag" in driver.title, (
            f"Не удалось войти! Заголовок: {driver.title}"
        )

    with allure.step("Шаг 2: Добавление товаров и переход в корзину"):
        cart_page = (
            add_page
            .add_backpack()
            .add_bolt_tshirt()
            .add_onesie()
            .go_to_cart()
        )

    # Проверка Chekout
    with allure.step("Шаг 3: Оформление заказа"):
        cart_page.click_checkout()
