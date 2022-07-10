company_data = {}

while True:
    company_info = input()
    if company_info == "End":
        break

    company_info = company_info.split(' -> ')
    company = company_info[0]
    company_id = company_info[-1]

    if company not in company_data.keys():
        company_data[company] = []
    if company_id not in company_data[company]:
        company_data[company].append(company_id)

for company_name, employee_id in company_data.items():
    print(company_name)
    print('\n'.join(f"-- {o}" for o in employee_id))
