#!/usr/bin/python3

import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from HBNBCommand import HBNBCommand


class TestHBNBCommmand(unittest.TestCase):
    """
    Test case for the HBNBCommand class
    """

    def setUp(self):
        """
        Set up test objects
        """
        self.fs = FileStorage()
        self.base_model = BaseModel()
        self.cmd = HBNBCommand()

    def tearDown(self):
        """
        Remove test objects
        """
        self.fs.reload()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_quit_command(self):
        """
        Test quit command to exit the program
        """
        self.assertIsInstance(self.cmd.do_quit(""), bool)

    def test_invalid_create_command(self):
        """
        Test create command with invalid class name
        """
        with self.assertRaises(Exception):
            self.cmd.do_create("InvalidClass")

    def test_create_command(self):
        """
        Test create command with valid class name
        """
        self.assertIsInstance(self.cmd.do_create("BaseModel"), str)

    def test_show_command_no_id(self):
        """
        Test show command without id
        """
        with self.assertRaises(Exception):
            self.cmd.do_show("BaseModel")

    def test_show_command_invalid_class(self):
        """
        Test show command with invalid class name
        """
        with self.assertRaises(Exception):
            self.cmd.do_show("InvalidClass 1234-1234-1234")

    def test_show_command(self):
        """
        Test show command with valid class name and id
        """
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            self.cmd.do_create("BaseModel")
            self.cmd.do_show("BaseModel " + self.base_model.id)
        output = captured_output.getvalue().strip()
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)

    def test_postloop_newline(self):
        """
        Test postloop newline
        """
        self.cmd.postloop()
        self.assertEqual("\n", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()

