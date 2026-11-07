import unittest

from logic import Task


class TestTask(unittest.TestCase):
    def test_defaults(self):
        task = Task("Сдать лабу", "2026-11-10")
        self.assertEqual(task.title, "Сдать лабу")
        self.assertEqual(task.deadline, "2026-11-10")
        self.assertFalse(task.done)

    def test_done_flag(self):
        task = Task("Купить хлеб", "2026-11-08", done=True)
        self.assertTrue(task.done)


if __name__ == "__main__":
    unittest.main()
