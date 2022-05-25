using System;

namespace _06._CinemaTickets
{
    class Program
    {
        static void Main(string[] args)
        {
            

            string movieName = Console.ReadLine();
            int freeSeats = 0;

            double studentTickets = 0;
            double standardTickets = 0;
            double kidTickets = 0;

            string ticketType = "";
             
            double soldTickets;

             while (movieName != "Finish")
             {
                freeSeats = int.Parse(Console.ReadLine());

                soldTickets = 0;

                for (int i = 0; i < freeSeats; i++)
                {

                    ticketType = Console.ReadLine();
                   
                    if (ticketType == "student")
                    {
                        studentTickets++;
                    }
                    else if (ticketType == "standard")
                    {
                        standardTickets++;
                    }
                    else if (ticketType == "kid")
                    {
                        kidTickets++;
                    }
                    else if (ticketType == "End")
                    {
                        break;
                    }

                    soldTickets++;
                }

                Console.WriteLine($"{movieName} - {(soldTickets / freeSeats) * 100:f2}% full.");
                movieName = Console.ReadLine();

             }

            Console.WriteLine($"Total tickets: {(studentTickets + standardTickets + kidTickets)}");
            Console.WriteLine($"{(studentTickets / (studentTickets + standardTickets + kidTickets) * 100):f2}% student tickets.");
            Console.WriteLine($"{(standardTickets / (studentTickets + standardTickets + kidTickets) * 100):f2}% standard tickets.");
            Console.WriteLine($"{(kidTickets / (studentTickets + standardTickets + kidTickets) * 100):f2}% kids tickets.");

        }





















    }
}
