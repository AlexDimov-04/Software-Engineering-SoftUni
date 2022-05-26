using System;

namespace _04._Balls
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int points = 0;

            int redBall = 0;
            int orangeBall = 0;
            int yellowBall = 0;
            int whiteBall = 0;
            double blackBall = 0;
            int otherColorBall = 0;

            for (int i = 1; i <= n; i++)
            {
                string color = Console.ReadLine();

                if (color == "red")
                {
                    points += 5;
                    redBall++;
                }
                else if (color == "orange")
                {
                    points += 10;
                    orangeBall++;
                }
                else if (color == "yellow")
                {
                    points += 15;
                    yellowBall++;
                }
                else if (color == "white")
                {
                    points += 20;
                    whiteBall++;
                }
                else if (color == "black")
                {
                    points /= 2; // MATH.FLOOR IN CW!!!!!
                    blackBall++;
                }
                else
                {
                    otherColorBall++;

                }
            }

            Console.WriteLine($"Total points: {points}");
            Console.WriteLine($"Red balls: {redBall}");
            Console.WriteLine($"Orange balls: {orangeBall}");
            Console.WriteLine($"Yellow balls: {yellowBall}");
            Console.WriteLine($"White balls: {whiteBall}");
            Console.WriteLine($"Other colors picked: {otherColorBall}");
            Console.WriteLine($"Divides from black balls: {Math.Floor(blackBall)}");








        }
    }
}
    

