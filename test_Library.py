import unittest

from Library import (
    books,
    add_book_data,
    search_book_by_id,
    issue_book_by_id
)


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):

        books.clear()

        books.append({
            "id": "1",
            "title": "Python",
            "author": "Ali",
            "issued": False
        })

    def test_add_book_success(self):

        result = add_book_data("2", "Java", "Ahmed")

        self.assertTrue(result)

    def test_add_duplicate_book(self):

        result = add_book_data("1", "Python", "Ali")

        self.assertFalse(result)

    def test_search_existing_book(self):

        result = search_book_by_id("1")

        self.assertIsNotNone(result)

    def test_search_invalid_book(self):

        result = search_book_by_id("99")

        self.assertIsNone(result)

    def test_issue_book_success(self):

        result = issue_book_by_id("1")

        self.assertTrue(result)

    def test_issue_already_issued_book(self):

        issue_book_by_id("1")

        result = issue_book_by_id("1")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()