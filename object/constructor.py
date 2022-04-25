class Student(object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能觀看《熊熊》.' % self.name)
        else:
            print('%s正在觀看電影.' % self.name)


def main():
    # 創學生物件並指定姓名和年齡
    stu1 = Student('alice', 8)
    # 给物件study消息
    stu1.study('Python')
    # 给物件watch_av消息
    stu1.watch_movie()

    stu2 = Student('ben', 15)
    stu2.study('數學')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
