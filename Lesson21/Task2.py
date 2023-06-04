import unittest
import os
import logging
from Task1 import CustomFile


class TestCustomFile(unittest.TestCase):
    def setUp(self):
        self.test_file_path = 'test.txt'
        with open(self.test_file_path, 'w') as f:
            f.write("This is a test file")
        self.log_file_path = 'example.log'

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)

        CustomFile.open_files = dict()

    def test_file_open_close(self):
        with CustomFile(self.test_file_path) as f:
            self.assertFalse(f.closed)
        self.assertTrue(f.closed)

    def test_file_read(self):
        with CustomFile(self.test_file_path) as f:
            self.assertEqual(f.read(), "This is a test file")

    def test_file_open_counter(self):
        with CustomFile(self.test_file_path) as f:
            pass
        self.assertEqual(CustomFile.open_files[self.test_file_path], 1)
        with CustomFile(self.test_file_path) as f:
            pass
        self.assertEqual(CustomFile.open_files[self.test_file_path], 2)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with CustomFile("non_existent_file.txt") as f:
                pass

    def test_file_exception_handling(self):
        with self.assertRaises(RuntimeError):
            with CustomFile(self.test_file_path) as f:
                raise RuntimeError("An error occurred")
        if os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'r') as f:
                log_content = f.read()
            self.assertIn("An error occurred", log_content)


if __name__ == "__main__":
    unittest.main()
