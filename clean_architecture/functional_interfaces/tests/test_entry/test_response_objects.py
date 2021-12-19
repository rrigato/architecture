from copy import deepcopy
import unittest

class TestResponseObjects(unittest.TestCase):
    def test_response_success(self):
        """ResponseSuccess for different datatypes"""
        from projectname.entry.response_objects import ResponseSuccess


        mock_response_values = [
            {"arg1": ["a", "list"]},
            {},
            None,
            {"arg1": 1, "arg2": 2},
            set(["a", "b"]),
            "arg1", 
            1, 
            2.0,
            (1, 2, 3)

        ]
        for mock_response_value in mock_response_values:
            with self.subTest(mock_response_value=mock_response_value):

                mock_response_object = ResponseSuccess(response_value=deepcopy(mock_response_value))

                self.assertEqual(mock_response_value, mock_response_object.response_value)
                self.assertTrue(bool(mock_response_object))


    @unittest.skip("Skipping for now")
    def test_valid_request_bad_input(self):
        """Unhappy Path ValidRequest invalid datatype for request_filters"""
        from projectname.entry.response_objects import ValidRequest


        mock_response_values = [
            set(["a", "b"]),
            "arg1", 
            1, 
            2.0,
            (1, 2, 3)
        ]
        for mock_response_value in mock_response_values:
            with self.subTest(mock_response_value=mock_response_value):

                with self.assertRaises(TypeError):
                    mock_response_object = ValidRequest(request_filters=deepcopy(mock_response_value))


