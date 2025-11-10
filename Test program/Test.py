import unittest
from unittest.mock import patch, mock_open
from commandmaster import *
import os
import json

class TestCommandMaster(unittest.TestCase):
    def setUp(self):
        self.history_file = HISTORY_FILE
        self.config_file = get_shell_config_file()

    def tearDown(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_get_shell_config_file(self):
        with patch.dict('os.environ', {'SHELL': 'zsh'}):
            self.assertEqual(get_shell_config_file(), os.path.expanduser('~/.zshrc'))
        with patch.dict('os.environ', {'SHELL': 'bash'}):
            self.assertEqual(get_shell_config_file(), os.path.expanduser('~/.bashrc'))

    @patch('builtins.input', side_effect=['test_command', 'echo "test"'])
    def test_create_command(self, mock_input):
        create_command()
        with open(self.history_file, 'r') as f:
            history = json.load(f)
            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]['name'], 'test_command')
            self.assertEqual(history[0]['action'], 'echo "test"')
        with open(self.config_file, 'r') as f:
            content = f.read()
            self.assertIn('alias test_command=\'echo "test"\'', content)

    @patch('builtins.input', side_effect=['1', 'y'])
    def test_remove_command(self, mock_input):
        # Create a command to remove
        with patch('builtins.input', side_effect=['test_command', 'echo "test"']):
            create_command()

        remove_command()
        with open(self.history_file, 'r') as f:
            history = json.load(f)
            self.assertEqual(len(history), 0)
        with open(self.config_file, 'r') as f:
            content = f.read()
            self.assertNotIn('alias test_command=\'echo "test"\'', content)

    @patch('builtins.input', side_effect=['1', 'echo "new_test"', 'y'])
    def test_update_command(self, mock_input):
        # Create a command to update
        with patch('builtins.input', side_effect=['test_command', 'echo "test"']):
            create_command()

        update_command()
        with open(self.history_file, 'r') as f:
            history = json.load(f)
            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]['action'], 'echo "new_test"')
        with open(self.config_file, 'r') as f:
            content = f.read()
            self.assertIn('alias test_command=\'echo "new_test"\'', content)

if __name__ == '__main__':
    unittest.main()
