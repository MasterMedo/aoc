using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC_2017
{
    class Day4
    {
        public static void Solution()
        {
            string line;
            System.IO.StreamReader input = new System.IO.StreamReader(@".\input\04.txt");
            int counter1 = 0;
            int counter2 = 0;
            while ((line = input.ReadLine()) != null)
            {
                HashSet<string> passphrase = new HashSet<string>();
                string[] potential = line.Split(' ');

                // First part of the Day
                bool flag1 = true;
                for (int i = 0; i < potential.Length; i++)
                {
                    if (!passphrase.Add(potential[i]))
                    {
                        flag1 = false;
                        break;
                    }
                }
                if (flag1)
                {
                    counter1++;

                    // Second part of the Day
                    bool flag2 = true;
                    foreach (string word1 in passphrase)
                    {
                        foreach (string word2 in passphrase)
                        {
                            if (word1 != word2)
                            {
                                if (String.Concat(word1.OrderBy(c => c)) == String.Concat(word2.OrderBy(c => c)))
                                {
                                    flag2 = false;
                                    break;
                                }
                            }
                        }
                        if (!flag2) break;
                    }
                    if (flag2) counter2++;                }
            }
            input.Close();
            Console.WriteLine(counter1 + " passphrases are valid in the input");
            Console.WriteLine(counter2 + " passphrases are valid in the input");
        }
    }
}
