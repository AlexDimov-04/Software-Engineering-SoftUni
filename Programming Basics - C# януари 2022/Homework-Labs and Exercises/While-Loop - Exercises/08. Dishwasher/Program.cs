using System;

namespace While_Loop_PB_More_Excercises
{
    class Program
    {
        static void Main(string[] args)
        {
            int bottlesCleaner = int.Parse(Console.ReadLine());
            string input = Console.ReadLine();

            int usedPlates = 0;
            int usedPots = 0;
            int plates = 0;
            int pots = 0;

            int detergentLiters = bottlesCleaner * 750;
            int loading = 0;
         
            while (input != "End")
            {
                int washedDishes = int.Parse(input);
                loading++;

                if (loading % 3 == 0)
                {
                    pots += washedDishes;
                    usedPots = washedDishes * 15;
                    detergentLiters -= usedPots;
                }
                else
                {
                    plates += washedDishes;
                    usedPlates = washedDishes * 5;
                    detergentLiters -= usedPlates;
                }

                if (detergentLiters < 0)
                {
                    Console.WriteLine($"Not enough detergent, {Math.Abs(detergentLiters)} ml. more necessary!");
                    //return;
                }

                input = Console.ReadLine();
            }

            if (detergentLiters >= 0)
            {
                Console.WriteLine("Detergent was enough!");
                Console.WriteLine($"{plates} dishes and {pots} pots were washed.");
                Console.WriteLine($"Leftover detergent {detergentLiters} ml.");
            }
               
                




        }
    }
}
