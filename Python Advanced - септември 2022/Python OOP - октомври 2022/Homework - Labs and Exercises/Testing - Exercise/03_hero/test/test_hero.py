from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('dimanou_', 1, 100, 100)
        self.enemy = Hero('ivan_', 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, 'dimanou_')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_when_hero_is_the_same_as_enemy_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_fight_with_zero_hero_health_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_fight_with_zero_enemy_health_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ve.exception), f"You cannot fight {self.enemy.username}. He needs to rest")

    def test_health_remove_after_fight_is_draw_expect_correct(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy.health, -50)
        self.assertEqual(result, 'Draw')

    def test_battle_enemy_and_win_expect_stats_improve(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, 'You win')

    def test_battle_enemy_and_lose_expect_stats_improve(self):
        self.enemy, self.hero = self.hero, self.enemy
        result = self.hero.battle(self.enemy)

        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 55)
        self.assertEqual(self.enemy.damage, 105)
        self.assertEqual(result, 'You lose')

    def test_correct__str__(self):
        self.assertEqual(str(self.hero), f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                                         f"Health: {self.hero.health}\n"
                                         f"Damage: {self.hero.damage}\n")


if __name__ == '__main__':
    main()
