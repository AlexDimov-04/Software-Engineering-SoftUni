from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('TeamName')
        self.team1 = Team('TeamNameOne')
        self.team.members = {'Alex': 2, 'Ivan': 4}
        self.team1.members = {'Stanislav': 1, 'Dimitar': 2, 'Plamen': 6}

    def test_correct_initialization(self):
        self.assertEqual(self.team.name, 'TeamName')
        self.assertEqual(self.team.members, {'Alex': 2, 'Ivan': 4})

    def test_not_correct_team_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'team_name'

        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_to_add_member_in_the_dictionary(self):
        result = self.team.add_member(Gosho=4, Tosho=3)

        self.assertEqual(self.team.members, {'Alex': 2, 'Ivan': 4, 'Gosho': 4, 'Tosho': 3})
        self.assertEqual(result, "Successfully added: Gosho, Tosho")

    def test_to_remove_member_from_the_team_members(self):
        result = self.team.remove_member('Alex')

        self.assertEqual(self.team.members, {'Ivan': 4})
        self.assertEqual(result, "Member Alex removed")

    def test_to_remove_member_who_does_not_exist(self):
        result = self.team.remove_member('Karpantiel')

        self.assertEqual(self.team.members, {'Alex': 2, 'Ivan': 4})
        self.assertEqual(result, "Member with name Karpantiel does not exist")

    def test_the_length_of_the_both_instance_dictionaries_return_True(self):
        self.team.members = {'Alex': 2, 'Ivan': 4, 'Kolio': 3, 'Daniel': 8}
        result = self.team.__gt__(self.team1)

        self.assertEqual(result, True)

    def test_the_length_of_the_both_instance_dictionaries_return_False(self):
        result = self.team.__gt__(self.team1)

        self.assertEqual(result, False)

    def test_the_length_of_the_both_instance_dictionaries_return_False_if_equal(self):
        self.team.members = {'Alex': 2, 'Ivan': 4, 'Kolio': 3}
        result = self.team.__gt__(self.team1)

        self.assertEqual(result, False)

    def test_length_of_the_passed_dict(self):
        self.assertEqual(len(self.team), 2)
        self.assertEqual(self.team.members, {'Alex': 2, 'Ivan': 4})

    def test__add___method(self):
        self.team.members = {}

        self.team.add_member(Simon=13)
        self.team.add_member(Filip=8)

        new_team = Team('Something')
        new_team.add_member(Stancho=4)

        merge = self.team + new_team

        self.assertEqual(merge.name, 'TeamNameSomething')
        self.assertEqual(merge.members, {'Simon': 13, 'Filip': 8, 'Stancho': 4})

    def test_correct__str__method(self):
        result = f"Team name: TeamName\n" \
                 f"Member: Ivan - 4-years old\n" \
                 f"Member: Alex - 2-years old"

        self.assertEqual(result, str(self.team))


if __name__ == '__main__':
    main()
