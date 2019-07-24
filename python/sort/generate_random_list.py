import random
import math


class GenerateRandomList:
    """
        生成随机列表
    """

    def integer_list(self, number, lower_limit, upper_limit):
        """
            生成一个整数列表

            通过random库中的randint()方法生成随机整数并添加到列表中

            Args:
                number:列表中的元素个数
                lower_limit:随机数的下限
                upper_limit:随机数的上限

            Return:
                一个拥有随机整数元素的列表

            Raises:
                没有判断参数的类型，如果不是整数则报错;
                没有判断lower_limit参数小于upper_limit;
        """
        return_list = list()
        for i in range(number):
            return_list.append(int(random.randint(lower_limit, upper_limit)))
        return return_list

    def generate_nearly_ordered_list(self, number, exchange_number=0):
        """
            近乎有序的整数列表

            生成一个有序列表，根据参数或者列表元素的个数来随机交换n次两个元素的位置；

            Args:
                number:列表元素的个数;
                exchange_number:元素位置交换的次数，默认为0，如果为0则交换次数为列表元素个数的五分之一;
        """
        return_list = list(range(0, number))
        exchange_number = math.ceil(number/5) if exchange_number == 0 else exchange_number
        for i in range(exchange_number):
            posx = random.randint(0, number-1)
            posy = random.randint(0, number-1)
            return_list[posx], return_list[posy] = return_list[posy], return_list[posx]
        return return_list


if __name__ == "__main__":
    test = GenerateRandomList()
    print(test.integer_list(10, 0, 10))
    print(test.generate_nearly_ordered_list(10, 10))
