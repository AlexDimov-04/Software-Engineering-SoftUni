using System;

namespace _08._Graduation
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            double sum = 0.0;
            int grade = 1; // the current grade of the student, e.g 1
            int counter = 0;// counts the number of times the student has been excluded 

            while (grade <= 12)
            {
                double yearlyGrade = double.Parse(Console.ReadLine());

                if (yearlyGrade < 4)
                {
                    if (counter == 1)
                    {
                        break;
                    }
                    counter++;
                    continue;
                }
                sum += yearlyGrade;
                grade++;
            }
            double averageGrade = sum / 12;

            if (grade > 12)
            {
                Console.WriteLine($"{name} graduated. Average grade: {averageGrade:f2}");
            }
            else
            {
                Console.WriteLine($"{name} has been excluded at {grade} grade");
            }

        }
    }
}
