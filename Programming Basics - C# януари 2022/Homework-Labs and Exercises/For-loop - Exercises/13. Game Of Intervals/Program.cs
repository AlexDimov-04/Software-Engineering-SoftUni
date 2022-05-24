using System;

namespace _05._GameOfIntervals
{
    class Program
    {
        static void Main(string[] args)
        {
            int moveThroughGame = int.Parse(Console.ReadLine());
            double number0To9 = 0;
            double number10To19 = 0;
            double number20To29 = 0;
            double number30To39 = 0;
            double number40To50 = 0;
            double invalidNumber = 0;

            double points = 0;
            


            for (int i = 0; i < moveThroughGame; i++)
            {
                double num = double.Parse(Console.ReadLine());

                if (num >= 0 && num <= 9)
                {
                    points += num * 0.2;
                    number0To9++;


                }
                else if (num >= 10 && num <= 19)
                {
                    points += num * 0.3;
                    number10To19++;
                }
                else if (num >= 20 && num <= 29)
                {
                    points += num * 0.4;
                    number20To29++;

                }
                else if (num >= 30 && num <= 39)
                {
                    points += 50;
                    number30To39++;
                }
                else if (num >= 40 && num <= 50)
                {
                    points += 100;
                    number40To50++;
                }
                else if (num < 0 || num > 50)
                {
                    points = points / 2;
                    invalidNumber++;
                }


            }

            double percent0To9 = (number0To9 / moveThroughGame) * 100;
            double percent10To29 = (number10To19 / moveThroughGame) * 100;
            double percent20To29 = (number20To29 / moveThroughGame) * 100;
            double percent30To39 = (number30To39 / moveThroughGame) * 100;
            double percent40To50 = (number40To50 / moveThroughGame) * 100;
            double invalidPercent = (invalidNumber / moveThroughGame) * 100;

            Console.WriteLine($"{points:f2}");
            Console.WriteLine($"From 0 to 9: {percent0To9:f2}%");
            Console.WriteLine($"From 10 to 19: {percent10To29:f2}%");
            Console.WriteLine($"From 20 to 29: {percent20To29:f2}%");
            Console.WriteLine($"From 30 to 39: {percent30To39:f2}%");
            Console.WriteLine($"From 40 to 50: {percent40To50:f2}%");
            Console.WriteLine($"Invalid numbers: {invalidPercent:f2}%");

           
        }
    }
}
