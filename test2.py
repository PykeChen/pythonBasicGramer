""" 实例002：“个税计算”
题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

程序分析 分区间计算即可。 """

monthPay = int(input('输入当月利润，我会帮你计算出发放的奖金数哦:\n'))
UNITS_W = 10000


def calculateBonus(profit):
    print('calculateBonus profit  = ' + str(profit))
    if profit <= 10 * UNITS_W:
        bonus = profit * 0.1
    elif profit <= 20 * UNITS_W:
        bonus = 10 * UNITS_W * 0.1 + (profit - 10 * UNITS_W) * 0.075
    elif profit <= 40 * UNITS_W:
        bonus = calculateBonus(20 * UNITS_W) + (profit - 20 * UNITS_W) * 0.05
    elif profit <= 60 * UNITS_W:
        bonus = calculateBonus(40 * UNITS_W) + (profit - 40 * UNITS_W) * 0.03
    elif profit <= 100 * UNITS_W:
        bonus = calculateBonus(60 * UNITS_W) + (profit - 60 * UNITS_W) * 0.015
    else:
        bonus = calculateBonus(100 * UNITS_W) + (profit - 100 * UNITS_W) * 0.01
    return bonus


lastValue = calculateBonus(monthPay)
print('last bonus{}'.format(lastValue))
