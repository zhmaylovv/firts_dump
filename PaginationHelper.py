'''
https://www.codewars.com/kata/515bb423de843ea99400000a/train/python
For this exercise you will be strengthening your page-fu mastery.
You will complete the PaginationHelper class, which is a utility class helpful
for querying paging information related to an array.
The class is designed to take in an array of values and an integer
indicating how many items will be allowed per each page.
The types of values contained within the collection/array are not relevant.
'''
from CodewarsTest import Test



class PaginationHelper:


    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page



    def item_count(self):
        return len(self.collection)



    def page_count(self):
        if self.item_count() % self.items_per_page == 0:
            return self.item_count() / self.items_per_page
        else:
            return (self.item_count() // self.items_per_page) + 1



    def page_item_count(self,page_index):

        full_page = (self.item_count() // self.items_per_page)
        if  full_page >= page_index and self.item_count() % self.items_per_page == 0:
            return self.items_per_page
        elif  full_page > page_index :
            return self.items_per_page
        elif self.item_count() % self.items_per_page != 0 and page_index + 1 == self.page_count():
            return self.item_count() - (self.items_per_page * (self.page_count() - 1))
        elif page_index + 1 >  self.page_count():
            return -1
        else:
            return -1


    def page_index(self,item_index):
        if item_index>=self.item_count() or item_index < 0 :
            return -1
        else:
            return item_index // self.items_per_page


collection = [i for i in range(1,25)]

helper = PaginationHelper(['a','b','c','d','e','f'], 4)

Test.assert_equals(helper.page_count(), 2)
Test.assert_equals(helper.page_index(-23), -1)
Test.assert_equals(helper.page_item_count(1), 2)
