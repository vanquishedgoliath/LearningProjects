import unittest as u
import numpy as np
import greedywalk as greedy

class greedywalkTest(u.TestCase):

    array = np.array([[90, 80, 70, 60], [20, 10, 12, 1], [30, 1, 1, 7], [1, 17, 8, 10]], dytpe=int)


    def test_least_change_in_elevation(self):

        current_elevation = 5
        elevation_1 = 5
        elevation_2 = 10
        elevation_3 = 11
        next_elevation = greedy.least_change_in_elevation(current_elevation, elevation_1, elevation_2, elevation_3)
        test_flag = True
        self.assertEqual(next_elevation, test_flag)


    def test_next_three_elevations(self):

        array = np.array([[90, 80, 70, 60], [20, 10, 12, 1], [30, 1, 1, 7], [1, 17, 8, 10]], dytpe=int)
        i = 2
        midpoint = 1
        elevation_1_test = array[1][2]
        elevation_2_test = array[2][2]
        elevation_3_test = array[3][2]

        next_elevation = greedy.next_three_elevations(array, i, midpoint)
        self.assertEquals(next_elevation, next_elevation)

    def test_greedy_walk(self):

        image = greedy.greedy_walk(array)

        # self.assert(its blue, certain pixel)
        # self.assert(its not blue, other pixel)
        # path = the path that the program should highlight [(0,0), (1,0), (1,2) ect]
        # for thingy in path:
        #    self.assert(blue, image[thingy]

if __name__ == '__main__':
    u.main()