from html.parser import HTMLParser
#chois 1
def findHowManyNumber(num, count=0):
  if not num == 0:
    N_num = num // 10
    print(num)
    count+=1
    return findHowManyNumber(N_num,count)
  return count
#choise 2
def getgreaterNum(list,index=0):
  #i can solve it by only one line just list.sort() return list[len(list)-1] XD
  if index+1<len(list):
    a=list[index]
    b=list[index+1]
    list[index]= max(a,b)
    list[index+1]=min(a,b)
    index+=1
    return getgreaterNum(list,index)
  elif len(list)==0:
    return 0
  max_=0
  for x in range(len(list)):
    if list[x] > max_:
      max_=list[x]
    if list[x]==max_ and not x==0:
      Nindex=0
      getgreaterNum(list, Nindex)
  return list[0]
#choice 3
def find(list,ob,index=0):
  if index<len(list) :
    item=list[index]
    if item[0]==ob:
      return index
    else:
      index+=1
      return find(list,ob,index)
  return -1
    
def  getHtmlTag(s,index=0,list=[],open_tag=0,close_tag=0):
  t_list=s[s.find('<',index):s.find('>',index+1)+1]
  if  s.find('<',index)>=0 and find(list,t_list)==-1:
    if t_list[1]=='/':
      if find(list,t_list[0]+t_list[2:]) == -1:
          return 'invalid syntaxt '
      else:
        close_tag+=1
        index=s.find('>',index)+1
        return getHtmlTag(s,index,list,open_tag, close_tag)
    open_tag+=1
    list.append([t_list,1])
    index=s.find('>',index)+1
    return getHtmlTag(s,index,list,open_tag, close_tag)
  elif find(list,t_list)>=0:
      open_tag+=1
      list[find(list,t_list)][1]+=1
      index=s.find('>',index)+1
      return getHtmlTag(s,index,list,open_tag, close_tag)
  if open_tag>close_tag or close_tag>open_tag:
    return 'invalid syntax '
  return list
    
  
def main():
  input_=int(input('please choose your option\n1. Count Digits\n2. Find Max\n3. Count Tags\n4. Exit\n:'))
  if input_==4:
    print('good night')
  elif input_==1:
    digit=int(input('input a number: '))
    print(findHowManyNumber(digit))
    main()
  elif input_==2:
    list=[int(input(f"inter digit for index {x+1}:")) for x in range(int(input('how many number you want to store: ')))]
    print(getgreaterNum(list))
    main()
  elif input_==3:
    option=int(input('\n1. Code: \n2. file path: '))
    if option==1:
      print(getHtmlTag(input('Write your code: ')))
      main()
    elif option==2:
      try:
        with open(input('Enter the path file with it extention\nexample"c:\\USER\\Desctop\\file.text"": ')) as file:
          print(getHtmlTag(file.read()))
          main()
      except FileNotFoundError:
       print("The file not found :(")
       main()
      
main()
 
