import rand_math
import rand_zimu


print("请选择游戏\n1.数字游戏\n2.字母游戏\n")
game = input("输入1或输入2")
if game=="1":
    palygame=rand_math.NumGame.num_game()
elif game=="2":
    palygame=rand_zimu.zimu_game()
    palygame.B()
else:
    print("输入错误") #