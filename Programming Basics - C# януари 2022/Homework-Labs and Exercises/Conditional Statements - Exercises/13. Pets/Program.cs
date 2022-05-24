using System;

namespace Pets
{
    class Program
    {
        static void Main(string[] args)
        {
            int days = int.Parse(Console.ReadLine());
            int avaibleFood = int.Parse(Console.ReadLine());
            double dogFoodKg = double.Parse(Console.ReadLine());
            double catFoodKg = double.Parse(Console.ReadLine());
            double turtleFoodGr = double.Parse(Console.ReadLine());
            double turtleFoodKg = turtleFoodGr / 1000;
            double neededDogFood = days * dogFoodKg;
            double neededCatFood = days * catFoodKg;
            double neededTurtleFood = days * turtleFoodKg;
            double totalFood = neededCatFood + neededDogFood + neededTurtleFood;
            if (totalFood <= avaibleFood)
            {
                Console.WriteLine($"{Math.Floor(avaibleFood - totalFood)} kilos of food left.");
            }
            else
            {
                Console.WriteLine($"{Math.Ceiling(totalFood - avaibleFood)} more kilos of food are needed.");
            }

        }
    }
}
