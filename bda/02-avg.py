#mapper
import sys
for line in sys.stdin:
    fields = line.strip().split()
    if len(fields)!= 3:
        continue
    salary = int(fields[2])
    print("{0}/t{1}" .format(salary,1))
    
# reducer
import sys
total_sal = 0
employee_count = 0
for line in sys.stdin:
    salary, count = line.strip().split('/t')
    total_sal += int(salary) * int(count)
    employee_count += int(count)
average_sal = total_sal / employee_count
print("Average Salary {0}" .format{average_sal})