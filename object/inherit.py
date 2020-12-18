# 交通工具(基底類別)
class Transportation:
    # 建構式
    def __init__(self):
        self.color = "white"  # 顏色屬性
    # 駕駛方法

    def drive(self):
        print("drive method is called.")
# 汽車子類別


class Car(Transportation):
    # 加速方法
    def accelerate(self):
        print("accelerate is method called.")

# 飛機子類別


class Airplane(Transportation):
    # 飛行方法
    def fly(self):
        print("fly method is called.")


mazda = Car()
mazda.drive()
print(mazda.color)
