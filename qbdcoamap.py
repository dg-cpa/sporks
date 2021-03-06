import qbdmap as q
from qbdmap import codeLook as c
from qbdmap import typeLook as t
from qbdmap import acctType as a
import csv

filein = 'QBD Accounts List.csv'

with open(filein) as f, open('outputcoa.csv','w',newline='') as o:
    reader = csv.reader(f)
    writer = csv.writer(o)
    writer.writerow(('*Code','*Name','Report Code','Description','*Type','*Tax Code'))
    count = 0
    try:
        for row in reader:
            
            if row[2] == 'Account' and row[4] == 'Type':
                next
            elif row[4] == 'Non-Posting':
                next
            elif row[2] != '':
                count += 1
                code = str(count)
                codeCount = code.rjust(3,'0')
                accountcode = a(row[4]) + codeCount
                writer.writerow((accountcode,row[2],c(row[4]),row[8],t(row[4]),'Tax Exempt 0%)'))
            else:
                next

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filein, reader.line_num, e))
    writer.writerow(('1000-OS','Bank - Conversion ','ASS.CUR','Outstanding items at conversion','Current Asset','Tax Exempt (0%)'))
    writer.writerow(('1000-AR','Accounts Receivable - System','ASS.CUR.REC.ACR','System Account for receivables','Accounts Receivable','Tax Exempt (0%)'))
    writer.writerow(('1000-AP','Accounts Payable - System','LIA.CUR.PAY.TRA','System Account for payabes','Accounts Payable','Tax Exempt (0%)'))
