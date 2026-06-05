data=[]
def add_employee():
	n=int(input("no.of employees : "))
	for i in range(n):
		emp_id = input("enter employee id : ")
		emp_name = input("enter employee name : ")
		emp_mail = input("enter employee mail : ")
		emp_number = int(input("enter employee number : "))
		emp_salary = int(input("enter employee salary : "))
		employee ={"emp_id":emp_id,"emp_name":emp_name,"emp_mail":emp_mail,"emp_number":emp_number,"emp_salary":emp_salary}
		data.append(employee)


def upd_employee():
	m=int(input("no.of employees updation :"))
	for l in range(m):
		emp_id1 = input("enter employee id : ")
		for i in data:
			if i["emp_id"]==emp_id1:
				n=int(input("no.of changes : "))
				for j in range(n) :
					for k in i.keys():
						b=input("enter a change : ")	
						if b in ['emp_number','emp_salary']:
							i[b]=int(input(b ))
							break
						else:
							i[b]=input(b )
							break				
			


def search_employee():
	emp_id2=input("enter employee id : ")
	for i in data:
		if i["emp_id"]==emp_id2 :
			print("employee details : ",i)


def salary_employee():
	m=int(input("no.of employees :"))
	for j in range(m):
		emp_id2=input("enter employee id : ")
		bonus=int(input("enter the bonus amount : "))
		for i in data :
			if i["emp_id"]==emp_id2:
				print("employee salary :",i["emp_salary"])
				print("total salary :",i["emp_salary"]+bonus)
				i["total_salary"]=i["emp_salary"]+bonus
m=int(input("enter no.of choices :"))
for i in range(m):
	choice=int(input("\n 1.add_employees \n 2.update_employees \n 3.search_employees \n 4.salary_employees \n"))
	if choice==1 :
		add_employee()
		print(data)
	elif choice==2 :
		upd_employee()
		print(data)
	elif choice==3 :
		search_employee()
		print(data)
	elif choice==4 :
		salary_employee()
		print(data)
	else :
		print("invalid choice")


		
	





















