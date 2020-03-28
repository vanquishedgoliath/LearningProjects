import unittest as u
import unittest.mock
import Connect4 as c4
import builtins


class Connect4Test(u.TestCase):

    def test_ValidateIntegerInput(self):
        # When I call ValidateInput with a valid integer, It should return
        # the integer I gave it and a value of True
        int_input = 3
        int_output, is_int = c4.ValidateInput(int_input)

        self.assertEqual(int_input, int_output)
        self.assertTrue(is_int)

    def test_ValidateStringInput(self):

        str_input = "Dad"
        str_long_input = "This is really stupid long sentence string"

        str_output, is_int = c4.ValidateInput(str_input)

        self.assertFalse(is_int)
        self.assertEqual(str_input, str_output)

   # def test_UserIntegerInput(self):
#
#        user_input = 3
#        output = 3
#
#        with u.mock.patch('builtins.input', side_effect=user_input):
#            program_input = c4.UserInput()
#
#        self.assertEqual(user_input, program_input)

    def test_UserInputInt(self):

        user_input = [3]


        with u.mock.patch('builtins.input', side_effect=user_input):
            program_input = c4.UserInput()

        self.assertEqual(user_input[0], program_input)



if __name__ == '__main__':
    u.main()