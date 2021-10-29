import random

# from scipy import stats
#
# val=stats.binom_test(x=531,n=1000,p=0.5)
# print(val)

# for i in range(530,565):
#     val = stats.binom_test(x=i, n=1000, p=0.5)
#     print('number',i,"result",val)

# list=[]
# string=""
# numberOfTs=0
# numberOfHs=0
#
# x = 1
# list.append('H')
# string = string + 'H'
# for i in range(1,101):
#     if i%5 == 0:
#         x= x*-1
#     if(x==1):
#         list.append('H')
#         numberOfTs = numberOfTs +1
#         string=string+'H'
#     else:
#         list.append('T')
#         numberOfHs = numberOfHs + 1
#         string=string+'T'
#
# prob1=0
# prob2=0
# prob3=0
# prob4=0
#
# prob5=0
# prob6=0
#
# THcount=0
# HTcount=0
# for i in range(1,len(list)):
#     if list[i] == 'H':
#         if list[i-1]== 'T':
#             prob1=prob1+1
#             if list[i - 2] == 'H' and i >= 2:
#                 HTcount=HTcount+1
#         elif list[i-1]=='H':
#             prob2=prob2+1
#             if list[i - 2] == 'T' and i >= 2:
#                 THcount=THcount+1
#     else:
#         if list[i - 1] == 'T':
#             prob3=prob3+1
#             if list[i - 2] == 'H' and i>=2:
#                 HTcount=HTcount+1
#                 prob6 = prob6 + 1
#         elif list[i - 1] == 'H':
#             prob4=prob4+1
#             if list[i - 2] == 'T' and i >= 2:
#                 THcount=THcount+1
#                 prob5 = prob5 + 1
#
#
# pb1=float(prob1/(prob1+prob3))
# pb2=float(prob2/(prob1+prob3))
# pb3=float(prob3/(prob3+prob4))
# pb4=float(prob4/(prob3+prob4))
#
# pb5=float(prob5/(THcount))
# pb6=float(prob6/(HTcount))
#
#
# print(string)
# print(pb1)
# print(pb2)
# print(pb3)
# print(pb4)
# print(pb5)
# print(pb6)
# list=[]
# for i in range(0,500):
#     count=0
#     list2=[]
#     birthdayList=[]
#     x = random.randint(1, 365)
#     list2.append(x)
#     for j in range(1,i+1):
#         x = random.randint(1, 365)
#         if list2.__contains__(x):
#             if birthdayList.__contains__(x):
#                 count=count+1
#             else:
#                 count=count+2
#             birthdayList.append(x)
#         list2.append(x)
#
#     if len(list2)>1:
#      prob = float(count/len(list2))
#      list.append(prob)
#
# for i in range(0,len(list)):
#     if list[i] > 0.5:
#         print('number of students',i,'prob',)
#
#
#

# list=[]
# list2=[]
# birthdayList=[]
# count = 0
# x = random.randint(1, 365)
# list2.append(x)
# birthdayList.append(x)
#
# for i in range(1,368):
#     x = random.randint(1, 365)
#     if not birthdayList.__contains__(x):
#         count = count + 1
#         birthdayList.append(x)
#     list2.append(x)
#
#     prob = float(count / 365)
#     list.append(prob)
#
# print(list)
# for i in range(0,len(list)):
#     if list[i] > 0.5:
#         print('number of students',i,'prob',)
#         list3=list2[0:i]
#         birthdayList2=birthdayList[0:i]
#         print(list3)
#         print(birthdayList2)
#         count=0
#         for j in birthdayList2:
#             count=count+list3.count(j)
#         print(count)
#         print(len(list3))
#         break
#
#
value=1;
for i in range(0,365):
    value = float(value*((365-i)/365))
    current = 1 - value
    if current > 0.5:
        print("number of students:", i, 'prob', current)
        break
