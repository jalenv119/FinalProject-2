import sys


class calc:
    def add(values):
#return all negative numbers added together if none in list return 0
        neg_sum = 0 

        for num in values:
            if num < 0:
                neg_sum += num

        return neg_sum

    def subtract(values):
#return the difference of all positive numbers in the list in none return 0
        pos_diff = None 

        for num in values:
            if num > 0:
                if pos_diff is None:
                    pos_diff = num
                else:
                    pos_diff -= num
        if pos_diff is None:
            return 0
    
        return pos_diff

    def multiply(values):
#return product of all non 0 numbers if none return 0
        multi_sum = 1 
        no_zeros = False
        for num in values:
            if num != 0:
                multi_sum *= num
                no_zeros = True
        if not no_zeros:
            return 0
        return multi_sum

    def divide(values):
    #return results if 1st num 0 result should be 0 unless there are others then use sys.exit and display message cannot divide by 0
        divi_sum = 1
        zeros = 0

        for num in values:
            if num == 0:
                zeros += 1
                if zeros > 1:
                    print('Cannot divide by 0')
                    sys.exit(1)
            else:
                divi_sum /= num

        if zeros == 1:
            return 0
        return divi_sum
    