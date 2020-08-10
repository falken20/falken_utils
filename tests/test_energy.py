# by Richi Rod AKA @richionline / falken20

"""
This file contain all TDD test for Energy class
"""

import unittest
import sys
# Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('..')
from utils.energy import Energy


class TestEnergy(unittest.TestCase):

    def setUp(self) -> None:
        """
        Method to create the instance automatically
        """
        self.energy = Energy('user', 'password')

    def test_initial_values(self):
        self.assertEqual(None, self.energy._token)
        self.assertEqual(None, self.energy._cookie)
        self.assertEqual(None, self.energy._session)
