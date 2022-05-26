using System;

namespace _04
{
    class Program
    {
        static void Main(string[] args)
        {
            int days = int.Parse(Console.ReadLine());
            double food = double.Parse(Console.ReadLine());

            double dogFood = 0;
            double catFood = 0;
            double biscuits = 0;

            double dayDogFood;
            double dayCatFood;


            for (int today = 1; today <= days; today++)
            {
                dayDogFood = double.Parse(Console.ReadLine());
                dayCatFood = double.Parse(Console.ReadLine());

                if (today % 3 == 0)
                {
                    biscuits += (dayDogFood + dayCatFood) / 10;   //*10 и разделяме на 100, но
                                                                  //в случая имаме 100 върху 10
                                                                  //то става 10.
                }

                dogFood += dayDogFood;
                catFood += dayCatFood;

               

            }

            Console.WriteLine($"Total eaten biscuits: {biscuits:f0}gr.");

            Console.WriteLine($"{(dogFood + catFood) * 100 / food:f2}% of the food has been eaten.");
            Console.WriteLine($"{dogFood * 100 / (dogFood + catFood):f2}% eaten from the dog.");
            Console.WriteLine($"{catFood * 100 / (dogFood + catFood):f2}% eaten from the cat.");
        }
    }
}
