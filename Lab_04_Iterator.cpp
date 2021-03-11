#include <iostream>
#include <string>
#include <sstream>
#include <ostream>
#include <fstream>
#include <algorithm>
using namespace std;

#include "Linked_List_Interface.h"
#include "LinkedList.h"

//-------- Memory Check --------//

#ifdef _MSC_VER
#define _CRTDBG_MAP_ALLOC  
#include <crtdbg.h>
#define VS_MEM_CHECK _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
#else
#define VS_MEM_CHECK;
#endif

int main(int argc, char* argv[])
{
    VS_MEM_CHECK;

    if (argc < 3)
    {
        cerr << "Please provide name of input and output files";
        return 1;
    }
    cout << "Input file: " << argv[1] << endl;
    ifstream in(argv[1]);
    if (!in)
    {
        cerr << "Unable to open " << argv[1] << " for input";
        return 2;
    }
    cout << "Output file: " << argv[2] << endl;
    ofstream out(argv[2]);
    if (!out)
    {
        in.close();
        cerr << "Unable to open " << argv[2] << " for output";
        return 3;
    }


    // Iterator position = find();

    // Declare myList
    LinkedList<string> myList;


    // process input strings
    for (string line; getline(in, line);)
    {
        string item1, item2, item3;
        if (line.size() == 0) continue;
        out << endl << line;
        istringstream iss(line);
        iss >> item1;

        if (item1 == "Clear")
        {
            myList.clear();
            out << " OK";
        }
        if (item1 == "Insert")
        {
            while (iss >> item2)
            {
                //out << " " << item2;
                myList.push_front(item2);
            }
        }

        else if (item1 == "PrintList")
        {
            try
            {
                if (myList.empty() == true)
                {
                    throw item1;
                }
            }
            catch (string wrong)
            {
                out << " Empty!";
            }
            out << " " << myList.toString();

        }

        else if (item1 == "Size")
        {
            out << " " << myList.size();
        }

        else if (item1 == "Empty")
        {
            out << " " << boolalpha << myList.empty();
        }

        else if (item1 == "Delete")
        {
            try
            {
                if (myList.empty() == true)
                {
                    throw item1;
                }
            }
            catch (string wrong)
            {
                out << " Empty!";
            }
            if (myList.empty() == false)
            {
                myList.pop_front();
                out << " OK";
            }
        }

        else if (item1 == "Reverse")
        {
            try
            {
                if (myList.empty() == true)
                {
                    throw item1;
                }
            }
            catch (string wrong)
            {
                out << " Empty!";
            }
            if (myList.empty() == false)
            {
                myList.reverse();
                out << " OK";
            }
        }

        else if (item1 == "Remove")
        {
            iss >> item2;
            {
                myList.remove(item2);
            }
        }

        else if (item1 == "First")
        {
            try
            {
                if (myList.empty() == true)
                {
                    throw item1;
                }
            }
            catch (string wrong)
            {
                out << " Empty!";
            }

            if (myList.empty() == false)
            {
                out << " " << myList.front();
            }
        }

        //--------Iterate--------//

        else if (item1 == "Iterate")
        {
        try
            {
                if (myList.empty() == true)
                {
                    throw item1;
                }
            }
            catch (string wrong)
            {
                out << " Empty!";
            }
        LinkedList<string>::Iterator iter = myList.begin();
        while (iter != myList.end())
        {
            out << endl << " [" << *iter << "]";
            ++iter;
        }
        }

        //--------Find Function--------//

        else if (item1 == "Find")
        {
            LinkedList<string>::Iterator iter2 = myList.begin();
            iss >> item2;
            
            if (myList.find(myList.begin(), myList.end(), item2) != myList.end())
            {
                out << " OK";
            }

            else
            {
                out << " Not Found";
            }
        }

        //--------Erase Function--------//

        else if (item1 == "Erase")
        {
            LinkedList<string>::Iterator iter = myList.begin();
            iss >> item2;
            while (iter != myList.end())
            {
                if (*iter == item2)
                {
                    myList.erase(iter);
                    out << " OK";
                    break;
                }
                else
                {
                    ++iter;
                }
            }
            if (iter == myList.end())
            {
                out << " Not Found";
            }
        }

        //--------Replace Function--------//

        else if (item1 == "Replace")
        {
        LinkedList<string>::Iterator first = myList.begin();
        LinkedList<string>::Iterator second = myList.end();

        iss >> item2;
        iss >> item3;

        myList.replace(first, second, item2, item3);
        out << " OK";
        }


        //-------InsertBefore--------//

        else if (item1 == "InsertBefore")
        {
            iss >> item2;
            iss >> item3;
            LinkedList<string>::Iterator iter4 = myList.begin();

            while (iter4 != myList.end())
            {
                if (*iter4 == item3)
                {
                    myList.insert(iter4, item2);
                    out << " OK";
                    break;
                }
                else
                {
                    ++iter4;
                }
            }
            if (iter4 == myList.end())
            {
                out << " Not Found";
            }
        }

        //-------InsertAfter--------//

        else if (item1 == "InsertAfter")
        {
            iss >> item2;
            iss >> item3;
            LinkedList<string>::Iterator iter4 = myList.begin();

            while (iter4 != myList.end())
            {
                if (*iter4 == item3)
                {
                    myList.insert_after(iter4, item2);
                    out << " OK";
                    break;
                }
                else
                {
                    ++iter4;
                }
            }
            if (iter4 == myList.end())
            {
                out << " Not Found";
            }
        }

    }

    return 0;
}

/*

*/
