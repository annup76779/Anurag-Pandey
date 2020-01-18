def pattern2(row):
    '''
    this is the function to print the diamond for the desired width.
    :param row: this the desired width for the diamond
    :return: return the diamond
    '''
    help(pattern2)
    s=1
    '''
    i=1--s=1
    i=2--s=3
    i=3-- print 5 stars and s=3
    i=4--s=3
    i=5-- s=1
    '''
    c = row / 2
    d = int(c)-1
    for i in range(1,row+1):
        if i<c:
            print(" "*d,star(s))
            s+=2
            d-=1
        elif i==(c+0.5):
            print(star(row))
            s=s-2
            d=0
        else:
            print(" "*d,star(s))
            s=s-2
            d+=1
def star(s):
    return "*"*s
def hollowRect(row):
    '''
    this function is to print the hollow rectangle for the no. of stars given by the users
    :param row: the no. of stars for giving the desired output
    :return:return the hollow rectangle
    '''
    help(hollowRect)
    k=row-2
    for i in range(1, row + 1):
        if i == 1:
            for j in range(1, row + 1):
                print("* ", end="")
            print()
        elif i == row:
            for j in range(1, row + 1):
                print("* ", end="")
            print()
        else:
            print("*", end="")
            for j in range(1, 3):
                if j == 1:
                    print("  " * k, end="")
                else:
                    print(" *")
def main():
    row=int(input("enter the no. of row but the rows should be odd \n#special case of pattern"))
    try:
        a=row%2
        assert a!=0 and row!=0
        pattern2(row)
        hollowRect(row)
    except:
        print('Worng selection of rows for the perfect diamond.')
if __name__=="__main__":
    main()
    print('Hello Pandey ji ke bhaiya!s')
