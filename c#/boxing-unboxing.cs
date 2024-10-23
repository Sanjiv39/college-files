using System;
public class Boxing
{
    public static void Main()
    {
        int num = 2020;
        // boxing
        object obj = num;
        num = 100;
        Console.WriteLine("BOXING");
        System.Console.WriteLine("value of num is " + num);
        System.Console.WriteLine("value of obj is " + obj);
        num = 23;
        obj = num;
        // unboxing
        int i = (int)obj;
        Console.WriteLine("UNBOXING");
        Console.WriteLine("Value of ob object is :" + obj);
        Console.WriteLine("Value of i is " + i);
    }
}