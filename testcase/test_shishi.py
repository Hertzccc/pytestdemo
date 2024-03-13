import pytest


class Testshishi:

    @pytest.mark.smoke
    def test_01_shishi(self):
        print('shishi')

    @pytest.mark.user_management
    def test_02_niub(self):
        print('niub')


    def test_03_buniub(self):
        print('buniub')
