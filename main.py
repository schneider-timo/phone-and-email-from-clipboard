    #! python 3
    #  searches for E-Mail Adresses and Phone Numbers from clipboard
     
    import pyperclip, re
    from pathlib import Path
     
    matchFile = Path(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt')
    # example Germany: 0123 45678 901 | 0123 45678901 | 012345678901
    phoneRegex = re.compile(r'''                                
        (\d{4}\s?\d{5}\s?\d{3})
        ''', re.VERBOSE)
    # example: muster@mail-muster.com
    mailRegex = re.compile(r'''                                 
        (\S*@\S*\.\w{2,})   
    ''', re.VERBOSE)
    def findPhoneNumber(text):
        matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'w')
        matchFile.write('Phone numbers:\n')
        matchFile.close()
     
        phoneNumber = phoneRegex.findall(text)
        # if phoneNumber is empty, return nothing found
        if len(phoneNumber)<1:                                  
            print("no phone number found")
            matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'a')
            matchFile.write('No phone numbers found.\n')
            matchFile.close()
        # print the matches and write them to a text file
        else:                                                   
            print("Phone Numbers:")
            for match in phoneNumber:
                print("    ",match)
                matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'a')
                matchFile.write('   ')
                matchFile.write(match)
                matchFile.write('\n')
                matchFile.close()
        return phoneNumber 
    # same thing for the mails    
    def findMail(text):                                         
        matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'a')
        matchFile.write('Mail Addresses found:\n')
        matchFile.close()
        mailAddress = mailRegex.findall(text)
        if len(mailAddress)<1:
            print("no mail found")
            matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'a')
            matchFile.write('No mail addresses found.')
            matchFile.close()
        else:
            print("Mail Address:")
            for match in mailAddress:
                matchFile = open(Path.home() / 'code/privat/Python/automateTheBoringStuff/matches.txt', 'a')
                print("    ",match)
                matchFile.write('   ')
                matchFile.write(match)
                matchFile.write('\n')
                matchFile.close()
     
    mess = pyperclip.paste()
    findPhoneNumber(mess)
    findMail(mess)
    print('Check the \'matches\' file for the phone numbers and e-mail addresses found.')
