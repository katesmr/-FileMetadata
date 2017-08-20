import unittest
from src.utils.utils import permission


class PermissionTests(unittest.TestCase):
    def setUp(self):
        self.permission_test1 = permission(["110", "110", "100"])
        self.permission_test2 = permission(["111", "010", "000"])

    def test_permission(self):
        self.assertEqual(self.permission_test1,
                         {'other': ['read'], 'group': ['read', 'write'], 'user': ['read', 'write']})
        self.assertEqual(self.permission_test2,
                         {'user': ['read', 'write', 'execute'], 'group': ['write'], 'other': []})

if __name__ == "__main__":
    unittest.main()

