using System;

namespace _03._Sum_Prime_Non_Prime
{
    class Program
    {
        static void Main(string[] args)
        {
            //трябва ни променлива, която да пази нашият вход - input
            string input = Console.ReadLine();
            //трябва да имаме променлива, в която ще запазваме текущото число - num
            int num;

            //променлива за сумата на простите числа -primeSum
            int primeSum = 0;
            //променлива за сумата на НЕпростите числа -nonPrimeSum
            int nonPrimeSum = 0;


            //цикъл, който да се върти, докато не получим input="stop"
            while (input != "stop")
            {
                //преобразуване на нашия input в число
                num = int.Parse(input);

                //правим проверка дали нашето число(num)
                //=>дали num e отрицателно
                //   => игнорираме го!
                //   => отпечатваме "Number is negative."
                //   => четем нов input
                //   => приключваме изпълнението на ТОВА ЗАВЪРТАНЕ на while цикъла => continue;
                if (num < 0)
                {
                    Console.WriteLine("Number is negative.");
                    input = Console.ReadLine();
                    continue;
                }

                //*кое число е просто 
                // num >1; да се дели единстено на 1 и на себе си (num%1==0) && (num%num==0)
                bool isPrime = true;
                //един цикъл, който ще раздели num на всяко едно число от 2 до num-1
                for (int i = 2; i < num - 1; i++)
                {
                    if (num % i == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }

                //=>дали е просто или непросто
                //=> ако num се раздели на някое от числата без ост. => значи е непросто
                //   =>ако е просто => primeSum += num
                //   =>ако е НЕпросто => nonPrimeSum += num
                if (isPrime == true)
                {
                    primeSum += num;
                }
                else
                {
                    nonPrimeSum += num;
                }

                //=> трябва всеки път да четем input

                input = Console.ReadLine();
            }

            //когато получим input="stop" => излизаме от while цикъла и трябва да отпечатаме резултат:
            Console.WriteLine($"Sum of all prime numbers is: {primeSum}");
            Console.WriteLine($"Sum of all non prime numbers is: {nonPrimeSum}");


        }
    }
}
