import unittest

class TestDynamicFactory(unittest.TestCase):


    def test_factory_dispatch_router(self):
        """Dict has int index up to 199 and all values are functions"""
        from factory_function_selection.dynamic_routing import factory_dispatch_router
        from inspect import isfunction

        dispatch_router = factory_dispatch_router()

        [self.assertTrue(isfunction(x)) for x in dispatch_router.values()]
        [self.assertEqual(type(x), int) for x in dispatch_router.keys()]
        self.assertEqual(len(dispatch_router.keys()), 200)

