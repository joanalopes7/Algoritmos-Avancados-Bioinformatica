import unittest
import sys
import os

from ReactionGraph import MetabolicNetwork

caminho_grafos = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Grafos')
sys.path.append(caminho_grafos)

from Grafos import MyGraph


class TestMetabolicNetwork(unittest.TestCase):
    
    def setUp(self):
        reactions = {
            'R01': {'cons': ['M03', 'M05'], 'prod': ['M07']},
            'R02': {'cons': ['M04', 'M05'], 'prod': ['M07', 'M02']},
            'R03': {'cons': ['M08', 'M07', 'M02'], 'prod': ['M04', 'M05']},
            'R04': {'cons': ['M03', 'M04'], 'prod': ['M01']},
            'R05': {'cons': ['M05', 'M08'], 'prod': ['M01', 'M04']},
            'R06': {'cons': ['M08', 'M07'], 'prod': ['M01', 'M05']},
            'R07': {'cons': ['M03', 'M07'], 'prod': ['M06', 'M01']},
            'R08': {'cons': ['M01', 'M05'], 'prod': ['M02', 'M08']},
            'R09': {'cons': ['M07', 'M06'], 'prod': ['M04', 'M08']},
            'R10': {'cons': ['M03', 'M05', 'M04'], 'prod': ['M08', 'M02']}
        }
        self.network = MetabolicNetwork(reactions)
        
    def test_metabolitos(self):
        expected = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08']
        result = self.network.metabolitos()
        self.assertEqual(result, expected)

    def test_consome(self):
        #('R10')
        expected = ['M03', 'M05', 'M04']
        result = self.network.consome('R10')
        self.assertEqual(result, expected)


        #('R05')
        expected = ['M05', 'M08']
        result = self.network.consome('R05')
        self.assertEqual(result, expected)


    def test_produz(self):
        
        
        #('R04')
        expected = ['M01']
        result = self.network.produz('R04')
        self.assertEqual(result, expected)

    def test_consomem(self):

        #('M08')
        expected = ['R03','R05','R06']
        result = self.network.consomem('M08')
        self.assertEqual(result, expected)

    def test_produzem(self):

        #('M04')
        expected = ['R03', 'R05', 'R09']
        result = self.network.produzem('M04')
        self.assertEqual(result, expected)

    def test_mlig(self):

        #('M07')
        expected = ['M01', 'M04', 'M05', 'M06', 'M08']
        result = self.network.mlig('M07')
        self.assertEqual(result, expected)

    def test_rlig(self):

        #('R01')
        expected = ['R03','R06', 'R07', 'R09']
        result = self.network.rlig('R01')
        self.assertEqual(result, expected)

    def test_ativadas_por(self):

        #('M06', 'M01')
        expected = []
        result = self.network.ativadas_por('M06', 'M01')
        self.assertEqual(result, expected)

        #('M03', 'M04')
        expected = ['R04']
        result = self.network.ativadas_por('M03', 'M04')
        self.assertEqual(result, expected)


    def test_produzidos_por(self):

        #('R01', 'R02')
        expected = ['M02', 'M07']
        result = self.network.produzidos_por('R01', 'R02')
        self.assertEqual(result, expected)

    def test_r_ativ(self):

        #('M01', 'M05')
        expected = ['R02', 'R03', 'R05', 'R06', 'R08']
        result = self.network.r_ativ('M01', 'M05')
        self.assertEqual(result, expected)

    def test_m_ativ(self):

        #('M01', 'M05')
        expected = ['M01', 'M02', 'M04', 'M05', 'M07', 'M08']
        result = self.network.m_ativ('M01', 'M05')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
