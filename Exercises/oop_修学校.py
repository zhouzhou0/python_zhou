#创建北京和成都两个校区
#创建Linux/python两个课程
#创建北京校区的python 3期课程和成都校区Linux 1期课程
#管理员创建了北京校区的学员小张，并将其分配在python 3期
#管理员创建了讲师小周，并将其分配给了python 3期
#讲师小周创建了一条python 3期的上课记录 Day02
#讲师小周为Day02 这节课所有所有学员批改了作业，小张得了A，小王得了B
#学员小张查看了自己所报的课程
#学员小张在 查看了 自己在python3 的期末成绩列表然后退出了
#学员小张给了讲师小周好评
Course_list= []
class School():
    def __init__(self,school_name):
        self.school_name = school_name
        self.students_list =[]
        self.teachers_list =[]

        global Course_list
    def hire(self,name):
        self.teachers_list.append(name)

        print('我们学校聘请了一个新老师，名字是{}'.format(name.name))

    def enroll(self,name):
        self.students_list.append(name)

        print('我们学校来了一位新同学：{}'.format(name.name))
class Grande(School):
    def __init__(self,schoole_name,grade_code,grade_course):
        super(Grande,self).__init__(schoole_name)
        self.code=grade_code
        self.course=grade_course
        self.member = []
        Course_list.append(self.course)
        print('我们现在有了{0}的{1}的{2}'.format(self.school_name,self.code,self.course))
    def course_info(self):
        print('课程大纲是{} day01,day02,day03'.format(self.course))
python = Grande('北京',3,'python')
linux = Grande('成都',1,'Linux')
class School_member():
    def __init__(self,name,age,sex,role):
        self.name=name
        self.age=age
        self.sex=sex
        self.role=role
        self.course_list = []
        print('我叫{},我是一个{}'.format(self.name,self.role))
stu_num_id = 00
class Students(School_member):
    def __init__(self,name,age,sex,role,course):
        super(Students,self).__init__(name,age,sex,role)
        global stu_num_id
        stu_num_id += 1
        stu_id =course.school_name+'s'+str(course.code)+str(stu_num_id).zfill(2)
        #zfill 填充的作用，当只有一位数时，前面填充0，只能对str类型操作
        self.id=stu_id
        self.mark_list = []
    def study(self,course):
        print('我来这里学习{},学号是{}'.format(course.course,self.id))

    def pay(self,course):
        print('我交了1000块钱给{}'.format(course.course))
        self.course_list.append(course.course)
    def pralse(self,obj):
        print('{}觉得{}课真棒'.format(self.name,obj.name))
    def mark_check(self):
        for i in self.mark_list.items:
            print(i)
    def out(self):
        print('离开')
tea_num_id = 00
class Teachers(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Teachers,self).__init__(name,age,sex,role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + 'T'+str(course.code)+str(tea_num_id).zfill(2)
        self.id=tea_id
    def teach(self,course):
        print('我来这讲{}课，我id是{}'.format(course.couse,self.id))
    def record(self,date,course,obj,level):
        obj.mark_list['Day'+date] = level


a = Students('小张',18,'M','student',python)
python.enroll(a)
a.study(python)
a.pay(python)

b = Students('小王',22,'f','student',python)
python.enroll(b)

c = Teachers('小周',30,'f','teacher',python)
python.hire(c)
c .record_mark = ('1',python,a,'A')
c.record_mark = ('1',python,b,'B')
c .record_mark = ('2',python,a,'B')
c.record_mark = ('2',python,b,'A')


