import unittest

from src.modules.Garden import *
from src.modules.Plants import *

class TestPlantClass(unittest.TestCase):
    def setUp(self):
        self.Basil = Plants('Basil','Purple','Easy',5.14,'spring','summer',4,'fertile','spring',1)
        self.Squash = Plants('Squash','Peach','easy',23,"hello",'mornining',2,'fertile','easter',5)
        self.Thyme = Plants('Thyme','English','medium',4.23,'Fall','May',8,'barren','yesterday',3)
    

class TestGardenClass(unittest.TestCase):
    def setUp(self):
        self.Garden = Garden('Andy',4,50,"raised bed",4,'soil')
        self.Garden2 = Garden('Andy',2,50,"raised bed",4,'soil')
        
        self.Basil = Plants('Basil','Purple','Easy',5.14,'spring','summer',4,'fertile','spring',1)
        self.Squash = Plants('Squash','Peach','easy',23,"hello",'mornining',2,'fertile','easter',5)
        self.Thyme = Plants('Thyme','English','medium',4.23,'Fall','May',8,'barren','yesterday',3)

    def test_add_bed(self):
        self.assertEqual(self.Garden.add_bed(2,3,4),(24, 24, 200), 'beds are not added correctly')
        self.assertEqual(self.Garden2.add_bed(2,3,4),(24, 24, 100), 'beds are not added correctly')

    def test_check_garden(self):
        self.Garden.add_bed(1,4,5)
        self.Garden.add_plant(self.Basil,1)
        self.Garden.add_plant(self.Squash,1)
        self.assertEqual(self.Garden.check_garden(),(28.14), 'beds are not added correctly')

if __name__ == '__main__':
    unittest.main()