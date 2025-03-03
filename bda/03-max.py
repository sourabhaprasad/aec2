# mapper
import sys
for line in sys.stdin:
    line = line.strip()
    column = line.split()
    salary = column[2]
    print("%s/t%s" %(None, salary))
    

# reducer
import sys
max_sal = 0
for line in sys.stdin:
    key, value = line.strip().split('/t', 1)
    try:
        salary = int(value)
    except ValueError:
        continue
    if salary > max_sal:
        max_sal = salary
print(f"Maximum Salary : {max_sal}")