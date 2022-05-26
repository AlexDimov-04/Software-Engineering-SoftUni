using System;

namespace _05._Best_Player
{
    class Program
    {
        static void Main(string[] args)
        {
            bool check = true;

            string name = Console.ReadLine();
            int goals = int.Parse(Console.ReadLine());

            string bestPlayer = "";
            int mostGoals = 0;

            while (check)
            {
                if (goals > mostGoals)
                {
                    bestPlayer = name;
                    mostGoals = goals;
                }
                if (goals >= 10) break;
                name = Console.ReadLine();
                if (name == "END") break;
                else goals = int.Parse(Console.ReadLine());
            }
            

            Console.WriteLine($"{bestPlayer} is the best player!");
            if (mostGoals >= 3) Console.WriteLine($"He has scored {mostGoals} goals and made a hat-trick !!!");
            else Console.WriteLine($"He has scored {mostGoals} goals");

            

                
               




        }
    }
}
