from dobtrack.tests import *

class TestDobitemController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='dobitem', action='index'))
        # Test response...
