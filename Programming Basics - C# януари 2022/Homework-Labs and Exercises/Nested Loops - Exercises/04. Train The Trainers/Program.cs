using System;

namespace _04._Train_The_Trainers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine()); //броя на журито 

            string input = Console.ReadLine();

            double presentationSum; //сборът на всички оценки на моментната презентация

            int presentationNum = 0; //броя на всички презентации;
            double evaluation = 0; //сбор от средните оценки за всяка от презентациите

            //четем имена презентации и ги оценяваме, докато не получим input = "Finish"
            while (input != "Finish")
            {
                //=>input => име на презентация 

                // нулираме сборът от оценките на всеки оценяващ
                presentationSum = 0;

                for (int i = 1; i <= n; i++)
                {
                    //=> всеки ще даде оценка => ще се добавя към presentationSum
                    presentationSum += double.Parse(Console.ReadLine());
                }

                //намираме средна оценка => 
                presentationSum = presentationSum / n;

                // трябва да я добавим към сбора на всички средни оценки=> 
                evaluation += presentationSum;

                Console.WriteLine($"{input} - {presentationSum:f2}.");

                presentationNum++;

                //четем нов вход (input)
                input = Console.ReadLine();
            }

            Console.WriteLine($"Student's final assessment is {evaluation /presentationNum:f2}.");
        }
    }
}
