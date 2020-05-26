#Project Euler Number 17

num2words1 = {'0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', \
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', \
            '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', \
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}


num2words2 = {2: 'Twenty', 3:'Thirty' 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

suffix = 'thousand'
main = 'hundred'


length = 0
for i in range(1, 1001):
    i = str(i)
    if int(i) < 20: length += len(num2words1[i])
    elif int(i) > 20 and int(i) < 100: length += len(num2words2[i[0]]) + len(num2words1[i[1]])
    elif int(i) > 100 and int(i) < 1001: length += len(num2words2i[0]) + len(main) + len(num2words1[i[1]] + 
        
    


