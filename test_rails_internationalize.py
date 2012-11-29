import random
import unittest
import rails_internationalize

from rails_internationalize import RailsInternationalize

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.inter = RailsInternationalize('home/rails/app/views/users/show.html.erb', 'Some funky string.')

    def test_key_name(self):
        self.assertEqual(self.inter.key_name(), 'some_funky_string')

    def test_erb_tag(self):
        self.assertEqual(self.inter.erb_tag(), "<%= t('.some_funky_string') %>")

    def test_locale_file(self):
        self.assertEqual(self.inter.locale_file(), 'home/rails/app/views/users/en.yml')
    # def test_shuffle(self):
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, range(10))

    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1,2,3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()