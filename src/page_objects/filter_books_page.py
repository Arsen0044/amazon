import re
from src.common_methods.ui_common_methods import CommonMethods


class FilterBooksPage(CommonMethods):

    def __init__(self):
        super().__init__()

    def provide_full_flow(self):
        self.open_the_page_and_avoid_you_are_not_a_robot_page()
        self.set_the_book_filter()
        self.input_and_search_by_text('Java')
        books_info_list = self.get_information_about_books()
        print(books_info_list)
        self.verify_book_is_in_list(books_info_list)

    def verify_book_is_in_list(self, list_info):
        verification_book = self.data.book_for_verification
        for sublist in list_info:
            if all(item in sublist for item in verification_book):
                assert True, 'Book is in the list'
                break
        else:
            assert False, 'Book is not in the list'

    def get_information_about_books(self):
        books_information = []
        items_on_search_result = self.get_element_by_locator(self.locators_type.CSS_SELECTOR,
                                                             '[data-component-type="s-search-result"]', is_many=True)
        for item in items_on_search_result:
            information_list = self.get_name_and_author(item)
            full_price = self.get_price_and_best_seller(item)
            if isinstance(full_price, list):
                information_list.extend(full_price)
            else:
                information_list.append(full_price)
            books_information.append(information_list)
        return books_information

    def get_name_and_author(self, item):
        title = item.find_element(self.locators_type.CSS_SELECTOR, self.locators.book_title_and_author)
        name = title.find_element(self.locators_type.TAG_NAME, 'h2')
        author_string = title.find_element(self.locators_type.TAG_NAME, 'div')
        author = self.clear_string(author_string.text)
        information_list = [name.text, author]
        return information_list

    @CommonMethods.decrease_implicitly_wait_for_func
    def get_price_and_best_seller(self, item):
        result = []
        try:
            price = item.find_elements(self.locators_type.CLASS_NAME, 'a-price-whole')
            fraction = item.find_elements(self.locators_type.CLASS_NAME, 'a-price-fraction')
            for i in range(len(price)):
                result.append(f'{price[i].text}.{fraction[i].text}')
            best_seller = item.find_element(self.locators_type.CSS_SELECTOR,
                                            '[data-component-type="s-status-badge-component"]')
            result.append(best_seller.text)
            return result
        except Exception:
            return result

    def input_and_search_by_text(self, text):
        self.input_text_by_id(text, self.locators.search_field_id)
        self.click_on_element_by_id(self.locators.submit_button)

    def set_the_book_filter(self):
        self.click_on_element_by_id(self.locators.filter_button_id)
        books_option = self.get_element_by_locator(self.locators_type.CSS_SELECTOR,
                                                   '[value="search-alias=stripbooks-intl-ship"]')
        books_option.click()

    def open_the_page_and_avoid_you_are_not_a_robot_page(self):
        self.go_to_url('https://www.amazon.com/')
        self.waiter(2)
        self.go_to_url('https://www.amazon.com/')

    @staticmethod
    def clear_string(string_):
        matches = re.findall(r'\|', string_)

        if len(matches) == 0:
            return string_
        elif len(matches) == 1:
            index = string_.find('|')
            return string_[:index]
        else:
            start = string_.find('|') + 1
            end = string_.rfind('|')
            return string_[start:end]
