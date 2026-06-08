data=[]
a={}
b=set(a)
def add_employee():
	n=int(input("no.of employees : "))
	for i in range(n):
		emp_id = input("enter employee id : ")
		emp_name = input("enter employee name : ")
		emp_mail = input("enter employee mail : ")
		emp_number = int(input("enter employee number : "))
		emp_salary = int(input("enter employee salary : "))
		employee={"emp_id":emp_id,"emp_name":emp_name,"emp_mail":emp_mail,"emp_number":emp_number,"emp_salary":emp_salary,"total_salary":emp_salary}
		for j in data:
			for k in j.values():	
				a.append(k)
		if data[i]['emp_id'] in a:
			print("data is matched")

		data.append(employee)
		emp_ids.append(emp_id)

add_employee()
		

		