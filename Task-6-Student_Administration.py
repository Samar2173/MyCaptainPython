import csv

def csvWrite(infoList):
    with open('student_info.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Conteact Number', 'Email-Id'])
        writer.writerow(infoList)

def studInfoCheck(infoList):

    print(f'\nEntered Information is:\nName: {infoList[0]}\nAge: {infoList[1]}\nContact Number: {infoList[2]}\nEmail-Id: {infoList[3]}\n')
    infoCheck = input("Is entered information correct? (yes/no)[Case-Sesitive]: ")

    if(infoCheck == 'yes'):
        csvWrite(infoList)
        
        moreInfo = input("Do you wish to enter information for another student? (yes/no)[Case-Sesitive]: ")
        if (moreInfo == 'yes'):
            return True
        elif (moreInfo == 'no'):
            return False
        else:
            print('Invalid Input Please Try Again!!\n')
            studInfoCheck(infoList)
    
    elif (infoCheck == 'no'):
        print('Please re-enter values')
        return True

    else:
        print('Invalid Input Please Try Again!!\n')
        studInfoCheck(infoList)

def main():
    condition = True
    while(condition):
        studInfo = input(f'Enter Student Information in [Name, Age, Contact-Number, Email-Id] format: ')
        studInfoList = studInfo.split(',')
        condition = studInfoCheck(studInfoList)

if __name__ == '__main__':
    main()