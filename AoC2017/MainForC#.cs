using static System.Console;

namespace AoC_2017
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("Solutions to Advent of Code 2017!");

            WriteLine('\n' + "Day 1:");
            Day1.Solution();

            WriteLine('\n' + "Day 3:");
            Day3.Solution();

            WriteLine('\n' + "Day 4:");
            Day4.Solution();

            WriteLine('\n' + "Day 5:");
            Day5.Solution();

            ReadLine();
        }
    }
}
