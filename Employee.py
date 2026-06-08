data=[]
emp_ids=[]
emp_numbers=[]
emp_mails=[]
def add_employee():
	n=int(input("no.of employees : "))
	for i in range(n):
		emp_id = input("enter employee id : ")	
		emp_name = input("enter employee name : ")
		emp_mail = input("enter employee mail : ")
		emp_number = int(input("enter employee number : "))
		emp_salary = int(input("enter employee salary : "))
		if emp_id in emp_ids :
				print("employee id is already exists")
		elif emp_mail in emp_mails:
				print("employee mail id is already exists")
		elif emp_number in emp_numbers :
				print("employee number is already exists")
		else :
			employee={"emp_id":emp_id,"emp_name":emp_name,"emp_mail":emp_mail,"emp_number":emp_number,"emp_salary":emp_salary,"total_salary":emp_salary}
			data.append(employee)
			for j in data:
				emp_ids.append(j['emp_id'])
				emp_mails.append(j['emp_mail'])
				emp_numbers.append(j['emp_number'])
				print("data entered is correct")
				print("\n" + "=" * 100)
				print(" " * 40 + "EMPLOYEE DETAILS")
				print("=" * 100)
				print(f"{'EMP ID':<10} | {'NAME':<15} | {'EMAIL':<25} | {'PHONE':<12} | {'SALARY':<10} | {'TOTAL SALARY':<12}")
				print("-" * 100)
				for employee in data:
					print(f"{employee['emp_id']:<10} | {employee['emp_name']:<15} | {employee['emp_mail']:<25} | {employee['emp_number']:<12} | {employee['emp_salary']:<10} | {employee['total_salary']:<12}")
				print("=" * 100)

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
							i[b]=int(input(b+" :"))
							print("\n" + "=" * 100)
							print(" " * 40 + "EMPLOYEE DETAILS")
							print("=" * 100)
							print(f"{'EMP ID':<10} | {'NAME':<15} | {'EMAIL':<25} | {'PHONE':<12} | {'SALARY':<10} | {'TOTAL SALARY':<12}")
							print("-" * 100)
							for employee in data:
								print(f"{employee['emp_id']:<10} | {employee['emp_name']:<15} | {employee['emp_mail']:<25} | {employee['emp_number']:<12} | {employee['emp_salary']:<10} | {employee['total_salary']:<12}")
							print("=" * 100)
							break
						else:
							i[b]=input(b+" :")
							print("\n" + "=" * 100)
							print(" " * 40 + "EMPLOYEE DETAILS")
							print("=" * 100)
							print(f"{'EMP ID':<10} | {'NAME':<15} | {'EMAIL':<25} | {'PHONE':<12} | {'SALARY':<10} | {'TOTAL SALARY':<12}")
							print("-" * 100)
							for employee in data:
								print(f"{employee['emp_id']:<10} | {employee['emp_name']:<15} | {employee['emp_mail']:<25} | {employee['emp_number']:<12} | {employee['emp_salary']:<10} | {employee['total_salary']:<12}")
							print("=" * 100)
							break
def search_employee():
	emp_id2=input("enter employee id : ")
	for i in data:
		if i["emp_id"]==emp_id2 :
			print("\n" + "=" * 100)
			print(" " * 40 + "EMPLOYEE DETAILS")
			print("=" * 100)
			print(f"{'EMP ID':<10} | {'NAME':<15} | {'EMAIL':<25} | {'PHONE':<12} | {'SALARY':<10} | {'TOTAL SALARY':<12}")
			print("-" * 100)
			if i in data:
				print(f"{i['emp_id']:<10} | {i['emp_name']:<15} | {i['emp_mail']:<25} | {i['emp_number']:<12} | {i['emp_salary']:<10} | {i['total_salary']:<12}")
				print("=" * 100)
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
				print("\n" + "=" * 100)
				print(" " * 40 + "EMPLOYEE DETAILS")
				print("=" * 100)
				print(f"{'EMP ID':<10} | {'NAME':<15} | {'EMAIL':<25} | {'PHONE':<12} | {'SALARY':<10} | {'TOTAL SALARY':<12}")	
				print("-" * 100)
				for employee in data:
					print(f"{employee['emp_id']:<10} | {employee['emp_name']:<15} | {employee['emp_mail']:<25} | {employee['emp_number']:<12} | {employee['emp_salary']:<10} | {employee['total_salary']:<12}")
				print("=" * 100)
for i in range(4):
	print("\n" + "=" * 40)
	print("      EMPLOYEE MANAGEMENT SYSTEM")
	print("=" * 40)
	print("1. Add Employee")
	print("2. Update Employee")
	print("3. Search Employee")
	print("4. Salary Employee")
	print("=" * 40)	
	choice = int(input("Enter your choice : "))	
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









