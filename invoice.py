worked_hours = int(input("How many hours did you work this month? "))
hourly_rate = 45

total_invoice = worked_hours * hourly_rate

print("--------------------")
print("---INVOICE #1---")

print(f"{'Worked hours':12} | {worked_hours:>12.1f}")
print(f"{'Total':12} | {total_invoice:>12.2f}")
print("--------------------")

