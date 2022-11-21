from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
import argparse

class LoadUp:
    def __init__(self, uid, pd):
        self.uid: str = str(uid)
        self.pd: str = pd
        self.ipaddr = None
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(options=option)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://ipgw.neu.edu.cn/srun_portal_pc?ac_id=1&theme=pro")
        time.sleep(5)

        # 判断页面是否已经登录
        try:
            self.ipaddr = driver.find_element(By.XPATH, '//*[@id="ipv4"]').text
            if self.ipaddr is not None:
                print("已经登录，ip为：{}".format(self.ipaddr))
                return None
        except Exception:
            pass
        # 定位连接网络
        login_btn = driver.find_element(By.XPATH, '//*[@id="login-sso"]')
        login_btn.click()
        time.sleep(5)

        # driver.window_handles[-1] 获取当前页面（跳转过来的页面）
        # driver.switch_to.window(driver.window_handles[-1]) 切换窗口
        driver.switch_to.window(driver.window_handles[-1])
        # username
        uid_elem = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/div[1]/input[1]')
        uid_elem.clear()
        uid_elem.send_keys(self.uid)

        time.sleep(2)
        # pwd
        pwd_elem = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/div[1]/input[2]')
        pwd_elem.clear()
        pwd_elem.send_keys(self.pd)

        time.sleep(2)
        # 定位登录
        loadup_btn = driver.find_element(By.XPATH, '//*[@id="index_login_btn"]')
        loadup_btn.click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[-1])
        self.ipaddr = driver.find_element(By.XPATH, '//*[@id="ipv4"]').text
        print("login successful!\tip为: {}".format(self.ipaddr))


if __name__ == '__main__':
    # sys.argv的用法
    # args = sys.argv[1:]
    # load = LoadUp(args[0], args[1])
    # load.login()

    # argparse的用法
    parser = argparse.ArgumentParser(prog="login-NEU", description="description: Automatically login NEU Networks:", usage="%(prog)s [options]")
    parser.add_argument('-n', '--name', help="input your userid of %(prog)s program.", required=True)
    parser.add_argument('-p', '--pwd', help="input your passwd of %(prog)s program.", required=True)
    args = parser.parse_args()

    # print(args.name)
    # print(args.pwd)
    load = LoadUp(args.name, args.pwd)
    load.login()
