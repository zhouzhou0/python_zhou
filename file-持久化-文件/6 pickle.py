import pickle

#序列号案例
age = 18
with open(r'test.txt','wb') as f :
    pickle.dump(age,f)

#反序列化
with open(r'test.txt','rb') as f :
    age = pickle.load(f)
    print(age)


a = ['coco','xiaoming','xiao dog',[180,183]]
with open(r'test.txt','wb') as  f :
    pickle.dump(a,f)


with open (r'test.txt','rb') as f :
    m = pickle.load(f)
    print(m)##