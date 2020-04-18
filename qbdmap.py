## basic translation for account types
## other expense mapped to mirror legacy reports
qbdtype = {'Bank': 'Bank',
        'Accounts Receivable': 'Accounts Receivable',
        'Other Current Asset': 'Current Asset',
        'Fixed Asset': 'Fixed Asset',
        'Other Assets': 'Non-current Asset',
        'Accounts Payable': 'Accounts Payable',
        'Credit Card': 'Bank',
        'Other Current Liability': 'Current Liability',
        'Long Term Liability': 'Non-current Liability',
        'Equity': 'Equity',
        'Income': 'Revenue',
        'Cost of Goods Sold': 'Direct Costs',
        'Expense': 'Expense',
        'Other Income': 'Other Income',
        'Other Expense': 'Other Income'}

## basic report code map based upon account type
## other expense is mapped to mirror legacy reports
qbdreportcode = {'Bank': 'ASS.CUR.CAS',
        'Accounts Receivable': 'ASS.CUR.REC',
        'Other Current Asset': 'ASS.CUR',
        'Fixed Asset': 'ASS.NCA.FIX',
        'Other Asset': 'ASS.NCA',
        'Accounts Payable': 'LIA.CUR.PAY',
        'Credit Card': 'LIA.CUR.PAY.CRC',
        'Other Current Liability': 'LIA.CUR',
        'Long Term Liability': 'LIA.NCL',
        'Equity': 'EQU',
        'Income': 'REV',
        'Cost of Goods Sold': 'EXP.COS',
        'Expense': 'EXP',
        'Other Income': 'REV.OTH',
        'Other Expense': 'EXP.OTH'}

## defining leading structure of account codes
## relies on account list ordered by A,L,Eq,R,Exp
qbdacctcode = {'Bank': 1,
        'Accounts Receivable': 1,
        'Other Current Asset': 1,
        'Fixed Asset': 1,
        'Other Assets': 1,
        'Accounts Payable': 2,
        'Credit Card': 2,
        'Other Current Liability': 2,
        'Long Term Liability': 2,
        'Equity': 3,
        'Income': 4,
        'Cost of Goods Sold': 5,
        'Expense': 6,
        'Other Income': 7,
        'Other Expense': 8}

def acctType(input):
    try:
        xeroAccount = qbdacctcode[input]
    except:
        xeroAccount = ''
    return str(xeroAccount)

## returning the value associated for Type
## sets any unidentified values to blank
def typeLook(input):
        
        try:
                xeroType = qbdtype[input]
        except:
                xeroType = ''
        return xeroType

## returning the value associated for simplified Code
## sets any unidentified values to blank
def codeLook(input):
        try:
                xeroCode = qbdreportcode[input]
        except:
                xeroCode = ''
        return xeroCode
