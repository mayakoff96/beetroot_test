class Mathematician:

    @staticmethod
    def square_nums(nums) -> list:
        """Method makes square numbers"""
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums) -> list:
        """Method removes positive numbers from a list"""
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(dates) -> list:
        """Method filters years which are not leap years"""
        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        return [date for date in dates if is_leap_year(date)]


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90 ]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))