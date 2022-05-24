using System;

namespace _08._Tennis_Ranklist
{
    class Program
    {
        static void Main(string[] args)
        {
            int tournaments = int.Parse(Console.ReadLine());
            int startingPoints = int.Parse(Console.ReadLine());
            int points = 0;
            int wPoints = 0;
            int fPoints = 0;
            int sfPoints = 0;
            double avarage = 0;
            double wins = 0;
            double percent = 0;

            for (int i = 1; i <= tournaments; i++)
            {
                string stageFromTournament = Console.ReadLine();


                if (stageFromTournament == "W")
                {
                    wPoints += 2000;
                    wins++;
                }
                else if (stageFromTournament == "F")
                {
                    fPoints += 1200;
                }
                else if (stageFromTournament == "SF")
                {
                    sfPoints += 720;
                }
            }
            points = wPoints + fPoints + sfPoints + startingPoints;
            avarage = (wPoints + fPoints + sfPoints) / tournaments;
            percent = (wins / tournaments) * 100;

            Console.WriteLine($"Final points: {points}");
            Console.WriteLine($"Average points: {Math.Floor(avarage)}");
            Console.WriteLine($"{percent:f2}%");
             

           





        }
    }
}
