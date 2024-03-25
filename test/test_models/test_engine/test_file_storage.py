#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test case for the FileStorage class
    """

    def setUp(self):
        """
        Set up test objects
        """
        self.fs = FileStorage()
        self.base_model = BaseModel()
        self.new_object = User()

    def tearDown(self):
        """
        Remove test objects
        """
        self.fs.reload()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """
        Test if all method correctly returns the dictionary __objects
        """
        self.fs.new(self.base_model)
        self.assertEqual(self.fs.all(self.base_model.__class__), {self.base_model.__class__.__name__ + "." + self.base_model.id: self.base_model})

    def test_save_method(self):
        """
        Test if save method correctly saves objects to file.json
        """
        keys = list(self.fs.all().keys())
        self.fs.save()
        new_keys = list(self.fs.all().keys())
        self.assertEqual(keys, new_keys)

        with open(self.fs.__file_path, "r") as f:
            data = json.load(f)
        self.assertDictEqual(data, {k: v.to_dict() for k, v in self.fs.all().items()})

    def test_reload_method(self):
        """
        Test if reload method correctly reloads data from file.json
        """
        self.fs.new(self.new_object)
        self.fs.save()
        self.fs.reload()
        new_obj = self.fs.all(self.new_object.__class__)[
            self.new_object.__class__.__name__ + "." + self.new_object.id]
        self.assertEqual(self.new_object.to_dict(), new_obj.to_dict())

        # Test if reload method handles empty file.json correctly
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.assertEqual(self.fs.all(), {})

    def test_all_cls_method(self):
        """
        Test if all method correctly returns a filtered dictionary
        """
        self.fs.new(self.base_model)
        self.assertEqual(self.fs.all(BaseModel), {self.base_model.__class__.__name__ + "." + self.base_model.id: self.base_model})
        self.assertEqual(self.fs.all(User), {})

    def test_reload_no_file(self):
        """
        Test if reload method handles no file.json correctly
        """
        self.fs.reload()
        self.assertEqual(self.fs.all(), {})


if __name__ == '__main__':
    unittest.main()

