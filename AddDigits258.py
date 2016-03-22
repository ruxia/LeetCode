class Solution(object):
    def addDigits(self, num):
        while(num>9):
            num=sum(int(i) for i in str(num))
        return num

if __name__ == '__main__':
    s=Solution()
    print(s.addDigits(123))