using System;
delegate int NumberChanger(int n);

namespace example
{
    class Delegate
    {
        static int num = 10;
        public static int AddNum(int a)
        {
            num += a;
            return num;
        }
        public static int SubNum(int b)
        {
            num -= b;
            return num;
        }
        public static int getNum()
        {
            return num;
        }
        static void Main(string[] args)
        {
            NumberChanger n1 = new NumberChanger(AddNum);
            NumberChanger n2 = new NumberChanger(SubNum);
            n1(25);
            Console.WriteLine("Addition= {0}", getNum());
            n2(5);
            Console.WriteLine("subtraction={0}", getNum());
            Console.ReadKey();
        }
    }
}