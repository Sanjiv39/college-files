using System;
namespace ConsoleApplication3
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1 = 0, num2 = 1, num3, num;
            Console.WriteLine("Upto how many number you want fibonacci series:");
            num = int.Parse(Console.ReadLine());
            Console.WriteLine(num1 + "\t" + num2 + "");
            for (int i = 2; i < num; i++)
            {
                num3 = num1 + num2;
                Console.WriteLine("\t" + num3);
                num1 = num2;
                num2 = num3;
            }
        }
    }
}