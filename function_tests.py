import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith씨는 온라인 일정 목록 관리 앱 홈페이지에 방문한다.
        self.browser.get('http://localhost:8000')

        # Edith씨는 페이제 제목과 헤더가 to-do list인 것을 보고 올바르게 방문했음을 안다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 일정 입력 페이지로 바로 이동한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Edith씨 취미는 플라이 낚시로 텍스트박스에 "공작새 깃털 구매"를 입력한다.
        inputbox.send_keys('공작새 깃털 구매')

        # Edith씨가 엔터를 입력하면 페이지를 업데이트하고 목록 페이지를 보여준다.
        # "1: 공작새 깃털 구매"가 일정 목록의 첫 번째 항목이다.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: 공작새 깃털 구매' for row in rows))

        # Edith씨는 추가로 텍스트 박스에 입력을 할 수 있고
        # "플라이 만드는데 공작새 깃털 사용"이라고 입력한다.
        self.fail('Finish the test!')

        # 다시 페이지를 업데이트하고 일정 두 가지 모두 목록에 표시한다.

        # Edith씨는 일정 목록이 사이트에 올바로 저장되었는지 궁금해서
        # unique URL을 생성을 확인한다.

        # Edith씨는 URL을 방문하고 일정 목록이 올바르게 있음을 확인한다.

        # Edith씨는 만족하고 이제 자러 간다.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
