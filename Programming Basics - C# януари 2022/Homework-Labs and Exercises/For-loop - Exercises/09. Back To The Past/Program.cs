using System;

namespace For_Loop_PB_MoreExercises
{
    class Program
    {
        static void Main(string[] args)
        {
            double avaibleMoney = double.Parse(Console.ReadLine());
            int year = int.Parse(Console.ReadLine());
            double totalMoney = 0.0;
            double leftMoney = 0.0;
            int age = 17;
            


            

            for (int i = 1800; i <= year; i++)
            {
                if (i % 2 == 0)
                {
                    leftMoney += 12000;
                }
                else if (i % 2 == 1)
                {
                    age += 2;
                    leftMoney += (12000 + (50 * age));
                }

            }
            totalMoney = avaibleMoney - leftMoney;

            if (totalMoney >= 0)
            {

            Console.WriteLine($"Yes! He will live a carefree life and will have {totalMoney:f2} dollars left.");

            }
            else
            {
                Console.WriteLine($"He will need {Math.Abs(totalMoney):f2} dollars to survive.");
            }

        }
    }
}
