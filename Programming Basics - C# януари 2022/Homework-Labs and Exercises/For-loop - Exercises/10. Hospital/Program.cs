using System;

namespace _02._Hospital
{
    class Program
    {
        static void Main(string[] args)
        {
            int period = int.Parse(Console.ReadLine());
            int treatedPatients = 0;
            int untreatedPatiens = 0;
            int doctors = 7;
          
            for (int i = 1; i <= period; i++)
            {
                int totalPatients = int.Parse(Console.ReadLine());

                if (untreatedPatiens > treatedPatients && (i % 3 == 0))
                {
                    doctors ++;
                }
                if (totalPatients <= 7)
                {
                    treatedPatients = totalPatients;
                }
                if (totalPatients > 7)
                {
                    treatedPatients = 7;
                    untreatedPatiens = totalPatients - 7;
                }
            }

            Console.WriteLine($"Treated patients: {treatedPatients}.");
            Console.WriteLine($"Untreated patients: {untreatedPatiens}.");
            
        }
    }
}
