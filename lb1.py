

def toBinary(number):
    binar = [0] * number;

    i = 0;
    while (number > 0):
        binar[i] = number % 2;
        number = int(number / 2);
        i += 1;

    ans = [0] * i;
    counter =0;
    for j in range(i - 1, -1, -1):
        ans[counter] = binar[j];
        counter+=1;

    return ans;

def remainderToBinary(remainder, places):
    binar = [0]*places;
    for i in range(places-1):
        remainder = remainder*2;
        if remainder > 1:
            binar[i] = 1;
            remainder -=1;
        else:
            binar[i] = 0;

    return binar;

def toOctal(number):
    oct = [0] * number;

    i = 0;
    while (number > 0):
        oct[i] = number % 8;
        number = int(number / 8);
        i += 1;

    ans = [0] * i;
    counter = 0;

    for j in range(i - 1, -1, -1):
        ans[counter] = oct[j];
        counter += 1;

    return ans;

def toHexademical(number):
    negative =0;
    if number<0:
        number = abs(number);
        negative = 1;
    x = (number % 16)
    digits = "0123456789ABCDEF"
    rest = number // 16
    if (rest == 0):
        return digits[x]

    if negative:
        negative = 0;
        return '-'+toHexademical(rest) + digits[x];
    return toHexademical(rest) + digits[x]

def floatToBinary(number, places =4):
    dec,remainder = str(number).split(".");
    dec = int(dec);
    remainder = "0." + remainder;
    remainder = float(remainder);
    res = toBinary(dec);
    res +='.';
    res += remainderToBinary(remainder, places)
    return res;

def floatToNotation(number):
    degree = 0;
    while(number>9):
        number/=10;
        degree+=1;
    return str(number)+"*10^"+str(degree);

print(toBinary(531))
print(toOctal(531))
print(toHexademical(3256))
print(toHexademical(-3657))
print(floatToBinary(698.412, 9))
print(floatToNotation(698.412))