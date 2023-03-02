class cal1:
    def dsum(x,y):
        return x+y
    def dminus(x,y):
        return x-y

class cal2:
    def dpow(x,y):
        ans = 1
        for i in range(y):
            ans = x*ans
        return ans

if __name__ == '__main__':
    print(cal1.dsum(1,2))
    print(cal2.dpow(2,3))
    
