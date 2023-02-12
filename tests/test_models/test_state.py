import unittest
from models.base_model import BaseModel
from models.state import State

class TestStateModel(unittest.TestCase):
    def test_state_model_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_model_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_state_model_attributes_type(self):
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, str)
        self.assertIsInstance(state.updated_at, str)
        self.assertIsInstance(state.name, str)

if __name__ == '__main__':
    unittest.main()
