using System;

namespace While_Loop_Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string favouriteBook = Console.ReadLine();
            int count = 0; //Quantity of books that had been checked out.
            string input = Console.ReadLine();//Checking if input(the book that we picked) is the same as favouritebook.

            while (input!= "No More Books")
            {
                if (input == favouriteBook)
                {
                    break;
                }

                count++;
                input = Console.ReadLine();
            }

            if (input == favouriteBook)
            {
                Console.WriteLine($"You checked {count} books and found it.");
            }
            else
            {
                Console.WriteLine("The book you search is not here!");
                Console.WriteLine($"You checked {count} books.");
            }
        }
    }
}
