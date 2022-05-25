using System;

namespace _02._ExamPreparation
{
    class Program
    {
        static void Main(string[] args)
        {
            int failedTimes = int.Parse(Console.ReadLine());//max number of grades <=4, a student can have.

            double evaluationSum = 0.0;//сбора от Grades
            int evaluationCount = 0;//броя на Grades
            string exerciseName = "";//the exercise name
            int evaluation = 0;//grade from the exercise
            int failedCount = 0;//броя grades <= 4 ----> пътите в които се е провалил.

            string input = Console.ReadLine();

            while (input != "Enough")
            {
                exerciseName = input;
                evaluation = int.Parse(Console.ReadLine());

                evaluationSum += evaluation;
                evaluationCount++;

                if (evaluation <= 4)
                {
                    failedCount++;
                    if (failedCount >= failedTimes)
                    {
                        Console.WriteLine($"You need a break, {failedCount} poor grades.");
                        break;
                    }
                } 

                input = Console.ReadLine();
            }
            double averageGrade = evaluationSum / evaluationCount;

            if (input == "Enough")
            {
                Console.WriteLine($"Average score: {averageGrade:f2}");
                Console.WriteLine($"Number of problems: {evaluationCount}");
                Console.WriteLine($"Last problem: {exerciseName}");
            }
           

        }
    }
}
