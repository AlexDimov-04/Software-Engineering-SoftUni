using System;

namespace _03._Vacation
{
    class Program
    {
        static void Main(string[] args)
        {
            double neededMoney = double.Parse(Console.ReadLine());//Нужни пари
            double availableMoney = double.Parse(Console.ReadLine());//Пари с които разполага

            string input = "";
            double money = 0;

            int daysCount = 0;//all days
            int spendCount = 0;//spend days <= 5 !!!

            while (availableMoney < neededMoney)
            {
                input = Console.ReadLine();
                money = double.Parse(Console.ReadLine());
                daysCount++;

                if (input == "save")
                {
                    availableMoney += money;
                    spendCount = 0;
                }
                else if (input == "spend")
                {
                    availableMoney -= money;
                    spendCount++;

                    if (availableMoney < 0)
                    {
                        availableMoney = 0;
                    }

                    if (spendCount == 5)
                    {
                        Console.WriteLine("You can't save the money.");
                        Console.WriteLine($"{daysCount}");
                        break;
                    }
                } 
            }

            if (availableMoney >= neededMoney)
            {
                Console.WriteLine($"You saved the money for {daysCount} days.");
            }






                

        }
    }
}
