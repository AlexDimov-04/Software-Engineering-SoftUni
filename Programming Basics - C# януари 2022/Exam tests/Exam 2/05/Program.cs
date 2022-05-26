using System;

namespace _05
{
    class Program
    {
        static void Main(string[] args)
        {
            int first = int.Parse(Console.ReadLine());
            int second = int.Parse(Console.ReadLine());

            string input = Console.ReadLine();

            while (input != "End of battle")
            {
                if (input == "one")
                {
                    second--;
                    if (second <= 0)
                    {
                        Console.WriteLine($"Player two is out of eggs. Player one has {first} eggs left.");
                        break;
                    }
                }
                else
                {
                    first--;
                    if (first <= 0)
                    {
                        Console.WriteLine($"Player one is out of eggs. Player one has {second} eggs left.");
                        break;
                    }
                }

                input = Console.ReadLine();
            }

            if (input == "End of battle") //first > 0 && second > 0
            {
                Console.WriteLine($"Player one has {first} eggs left.");
                Console.WriteLine($"Player two has {second} eggs left.");
            }
        }
    }
}
