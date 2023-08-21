import csv
import os
import argparse
import datetime

def password_generator(companyName, size=0):
    #This function will take a company name and generate a password list
    print(f"\nWORD: {args.company} ({len(args.company)} characters long)\n")
    
    # Get Date
    companyName = companyName.strip()
    now = datetime.datetime.now()
    year = str(now.year)
    yearLong = now.year
    yearShort = year[2:]
    nextYearLong = yearLong + 1
    nextYearShort = int(yearShort) + 1

    count = 0

    # Start playing
    unique_list = []
    companyName = companyName.lower()
    password_list = [
        # Current year
        companyName + str(yearShort),
        companyName + str(yearLong),
        companyName.upper() + str(yearShort), 
        companyName.upper() + str(yearLong),
        companyName.title() + str(yearShort), 
        companyName.title() + str(yearLong),
        companyName + str(yearShort) + '!',
        companyName + str(yearLong) + '!',
        companyName.upper() + str(yearShort) + '!', 
        companyName.upper() + str(yearLong) + '!',
        companyName.title() + str(yearShort) + '!', 
        companyName.title() + str(yearLong) + '!',
        
        # Year 2022
        companyName + '22',
        companyName + '2022',
        companyName.upper() + '22', 
        companyName.upper() + '2022',
        companyName.title() + '22', 
        companyName.title() + '2022',
        companyName + '22' + '!',
        companyName + '2022' + '!',
        companyName.upper() + '22' + '!', 
        companyName.upper() + '2022' + '!',
        companyName.title() + '22' + '!', 
        companyName.title() + '2022' + '!',
        
        # Year 2021
        companyName + '21',
        companyName + '2021',
        companyName.upper() + '21', 
        companyName.upper() + '2021',
        companyName.title() + '21', 
        companyName.title() + '2021',
        companyName + '21' + '!',
        companyName + '2021' + '!',
        companyName.upper() + '21' + '!', 
        companyName.upper() + '2021' + '!',
        companyName.title() + '21' + '!', 
        companyName.title() + '2021' + '!',

        # Year 2020
        companyName + '20',
        companyName + '2020',
        companyName.upper() + '20', 
        companyName.upper() + '2020',
        companyName.title() + '20', 
        companyName.title() + '2020',
        companyName + '20' + '!',
        companyName + '2020' + '!',
        companyName.upper() + '20' + '!', 
        companyName.upper() + '2020' + '!',
        companyName.title() + '20' + '!', 
        companyName.title() + '2020' + '!',

        # Year 2019
        companyName + '19',
        companyName + '2019',
        companyName.upper() + '19', 
        companyName.upper() + '2019',
        companyName.title() + '19', 
        companyName.title() + '2019',
        companyName + '19' + '!',
        companyName + '2019' + '!',
        companyName.upper() + '19' + '!', 
        companyName.upper() + '2019' + '!',
        companyName.title() + '19' + '!', 
        companyName.title() + '2019' + '!',

        # Everything else
        companyName + '1' + '!', 
        companyName.title() + '1', 
        companyName.title() + '1' + '!', 
        companyName + '1', 
        companyName.title() + '321', 
        companyName + '321', 
        companyName.lower(), 
        companyName.lower() + '123', 
        companyName.upper(), 
        companyName.title(), 
        companyName.title() + '123', 
        companyName.title().replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1").replace("b", "8").replace("s", "5"), 
        companyName.title().replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1").replace("b", "8"), 
        companyName.title().replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1"), 
        companyName.title().replace("o", "0").replace("a", "4").replace("e", "3"), 
        companyName.title().replace("o", "0").replace("a", "4"), 
        companyName.title().replace("o", "0"), 
        companyName.replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1").replace("b", "8").replace("s", "5"), 
        companyName.replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1").replace("b", "8"), 
        companyName.replace("o", "0").replace("a", "4").replace("e", "3").replace("i", "1"), 
        companyName.replace("o", "0").replace("a", "4").replace("e", "3"), 
        companyName.replace("o", "0").replace("a", "4"), 
        companyName.replace("o", "0"),
        
        # Seasons and months
        'Spring' + str(yearShort), 
        'Summer' + str(yearShort), 
        'Autumn' + str(yearShort), 
        'Winter' + str(yearShort), 
        'January' + str(yearShort), 
        'February' + str(yearShort), 
        'March' + str(yearShort), 
        'April' + str(yearShort), 
        'May' + str(yearShort), 
        'June' + str(yearShort), 
        'July' + str(yearShort), 
        'August' + str(yearShort), 
        'September' + str(yearShort), 
        'October' + str(yearShort), 
        'November' + str(yearShort), 
        'December' + str(yearShort), 
        'Password' + str(yearShort), 
        'spring' + str(yearShort), 
        'summer' + str(yearShort), 
        'autumn' + str(yearShort), 
        'winter' + str(yearShort), 
        'january' + str(yearShort), 
        'february' + str(yearShort), 
        'march' + str(yearShort), 
        'april' + str(yearShort), 
        'may' + str(yearShort), 
        'june' + str(yearShort), 
        'july' + str(yearShort), 
        'august' + str(yearShort), 
        'september' + str(yearShort), 
        'october' + str(yearShort), 
        'november' + str(yearShort), 
        'december' + str(yearShort), 
        'password' + str(yearShort), 
        'Spring' + str(yearLong), 
        'Summer' + str(yearLong), 
        'Autumn' + str(yearLong), 
        'Winter' + str(yearLong), 
        'January' + str(yearLong), 
        'February' + str(yearLong), 
        'March' + str(yearLong), 
        'April' + str(yearLong), 
        'May' + str(yearLong), 
        'June' + str(yearLong), 
        'July' + str(yearLong), 
        'August' + str(yearLong), 
        'September' + str(yearLong), 
        'October' + str(yearLong), 
        'November' + str(yearLong), 
        'December' + str(yearLong), 
        'Password' + str(yearLong), 
        'spring' + str(yearLong), 
        'summer' + str(yearLong), 
        'autumn' + str(yearLong), 
        'winter' + str(yearLong), 
        'january' + str(yearLong), 
        'february' + str(yearLong), 
        'march' + str(yearLong), 
        'april' + str(yearLong), 
        'may' + str(yearLong), 
        'june' + str(yearLong), 
        'july' + str(yearLong), 
        'august' + str(yearLong), 
        'september' + str(yearLong), 
        'october' + str(yearLong), 
        'november' + str(yearLong), 
        'december' + str(yearLong), 
        'password' + str(yearLong),
        'spring', 
        'summer', 
        'autumn', 
        'winter', 
        'january', 
        'february', 
        'march', 
        'april', 
        'may', 
        'june', 
        'july', 
        'august', 
        'september', 
        'october', 
        'november', 
        'december', 
        'password'
    ]
    
    for e in password_list:
        if e not in unique_list:
            unique_list.append(e)
        else:
            pass
    
    for password in unique_list:
        if len(password) >= int(size):
            print(password)

    # Fix the issue where the simple passwords from the 'Seasons and months' gets added multiple times.
    output_file = str(datetime.date.today()) + '_generated_passwords.txt'
    print("\n Saved in " + output_file)
    with open(output_file, 'a') as f:
        for password in unique_list:
            f.write(password + '\n')
            
    print(f'\nTotal Passwords Generated: {len(unique_list)}\n')
    
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--company', help='Provide the comapnies name? (e.g. Google, Microsoft, Tesla')
parser.add_argument('-s', '--size', help='Provide a minimum password length', required=False)
parser.add_argument('-i', '--include', help='Include a list of passwords, to be mutated', required=False)
args = parser.parse_args()

if args.include:
    print("\nMutating the given list " + args.include)
    with open(args.include) as file:
        for word in file:
            password_generator(word)

if args.company and args.size:
    password_generator(args.company, args.size)
elif args.company:
    password_generator(args.company)
else:
    parser.print_help()


