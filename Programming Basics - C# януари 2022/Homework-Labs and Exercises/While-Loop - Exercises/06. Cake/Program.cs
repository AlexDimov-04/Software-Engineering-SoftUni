using System;

namespace _06._Cake
{
    class Program
    {
        static void Main(string[] args)
        {
            int length = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int cakePieces = 0;
            string input = Console.ReadLine();
            int taking = 0;
            cakePieces = length * width;

            while (input != "STOP")
            {
                taking = int.Parse(input);
                cakePieces -= taking;

                if (cakePieces < 0)
                {
                    Console.WriteLine($"No more cake left! You need {Math.Abs(cakePieces)} pieces more.");
                    break;
                }

                input = Console.ReadLine();
            }

            if (input == "STOP")
            {
                Console.WriteLine($"{cakePieces} pieces are left.");
            }
        
        }
    }
}








