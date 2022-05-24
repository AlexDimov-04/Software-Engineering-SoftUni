using System;

namespace Grades
{
    class Program
    {
        static void Main(string[] args)
        {
            int students = int.Parse(Console.ReadLine());
            double count2 = 0.0;
            double count3 = 0.0;
            double count4 = 0.0;
            double count5 = 0.0;
            double sumResult = 0.0;
            double totalGrade = 0.0;



            for (int i = 1; i <= students; i++)
            {
                double grade = double.Parse(Console.ReadLine());
                sumResult += grade;

                if (grade >= 2.00 && grade <= 2.99)
                {
                    count2++;
                }
                else if (grade >= 3.00 && grade <= 3.99)
                {
                    count3++;
                }
                else if (grade >= 4.00 && grade <= 4.99)
                {
                    count4++;
                }
                else if (grade >= 5.00 && grade <= 6.00)
                {
                    count5++;
                }

               totalGrade = sumResult / students;
            }

            double percent5 = (count5 / students) * 100;
            double percent4 = (count4 / students) * 100;
            double percent3 = (count3 / students) * 100;
            double percent2 = (count2 / students) * 100;

            Console.WriteLine($"Top students: {percent5:f2}%");
            Console.WriteLine($"Between 4.00 and 4.99: {percent4:f2}%");
            Console.WriteLine($"Between 3.00 and 3.99: {percent3:f2}%");
            Console.WriteLine($"Fail: {percent2:f2}%");
            Console.WriteLine($"Average: {totalGrade:f2}");
    
            
        }
    }
}
