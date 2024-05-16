import helpers
import authentication
import database
import routers

from helpers.embrapaFiles import embrapaFiles

class TestClassEmbrapa:
    embFiles = embrapaFiles()

    def test_list_all_must_return_a_dict(self):
        assert type(self.embFiles.listAll()) == dict

    def test_list_all_must_be_greater_than_0(self):
        assert len(self.embFiles.listAll()) != 0