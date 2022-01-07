import scalpbot_code
import database_scalp
main = database_scalp.local_database("local_saves.txt", "r+")
print(main.file_path)
print(main.saves.readlines())
print(main.get_text())
"""driver = scalpbot_code.webdriver(main.websites["Best Buy"])
driver.wait(5)
scalpbot_code.show_driver(driver, True)
scalpbot_code.buy(driver, driver.website_obj.procedure)"""
