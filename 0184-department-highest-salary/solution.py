import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department,left_on='departmentId',right_on='id',suffixes=('_emp','_dept'))
    df['max_salary']= df.groupby('departmentId')['salary'].transform('max')
    res = df[df['salary'] == df['max_salary']]
    return res [['name_dept', 'name_emp','salary']].rename(columns={'name_dept' : 'Department', 'name_emp' : 'Employee', 'salary' : 'Salary'})
