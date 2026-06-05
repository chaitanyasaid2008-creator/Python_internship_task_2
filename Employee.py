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
		print(f"{'emp_id':<10} | {'emp_name':<12} | {'emp_mail':<10} | {'emp_number':<10} | {'emp_salary':<15}")
		print("-" * 67)
		for employee in data:
			    print(f"{employee['emp_id']:<10} | {employee['emp_name']:<12} | {employee['emp_mail']:<10} | {employee['emp_number']:<10} | {employee['emp_salary']:<15}")
			    
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
							print(f"{'emp_id':<10} | {'emp_name':<12} | {'emp_mail':<10} | {'emp_number':<10} | {'emp_salary':<15}")
							print("-" * 67)
							for employee in data:
								print(f"{employee['emp_id']:<10} | {employee['emp_name']:<12} | {employee['emp_mail']:<10} | {employee['emp_number']:<10} | {employee['emp_salary']:<15}")

							break
						else:
							i[b]=input(b )
							print(f"{'emp_id':<10} | {'emp_name':<12} | {'emp_mail':<10} | {'emp_number':<10} | {'emp_salary':<15}")
							print("-" * 67)
							for employee in data:
								print(f"{employee['emp_id']:<10} | {employee['emp_name']:<12} | {employee['emp_mail']:<10} | {employee['emp_number']:<10} | {employee['emp_salary']:<15}")

							break
				
def search_employee():
	emp_id2=input("enter employee id : ")
	for i in data:
		if i["emp_id"]==emp_id2 :
			print("employee details : ",i)
			print(f"{'emp_id':<10} | {'emp_name':<12} | {'emp_mail':<10} | {'emp_number':<10} | {'emp_salary':<15}")
			print("-" * 67)
			for employee in data:
				print(f"{employee['emp_id']:<10} | {employee['emp_name']:<12} | {employee['emp_mail']:<10} | {employee['emp_number']:<10} | {employee['emp_salary']:<15}")

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
				print(f"{'emp_id':<10} | {'emp_name':<12} | {'emp_mail':<10} | {'emp_number':<10} | {'emp_salary':<15} | {'total_salary':<15}")
				print("-" * 80)
				for employee in data:
					print(f"{employee['emp_id']:<10} | {employee['emp_name']:<12} | {employee['emp_mail']:<10} | {employee['emp_number']:<10} | {employee['emp_salary']:<15} | {employee['total_salary']:<15}")

for i in range(4):
	choice=int(input("\n 1.add_employees \n 2.update_employees \n 3.search_employees \n 4.salary_employees \n"))
	while choice:
		if choice==1 :
			add_employee()
			break
		elif choice==2 :
			upd_employee()
			break
		elif choice==3 :
			search_employee()
			break
		elif choice==4 :
			salary_employee()
			break
		else :
			print("invalid choice")


		
	





















