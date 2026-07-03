import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f4f8')
        
        self.employees = []
        self.employee_id_counter = 1
        
        self.create_widgets()
        
    def create_widgets(self):
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title = tk.Label(
            header_frame,
            text="EMPLOYEE MANAGEMENT SYSTEM",
            font=('Arial', 24, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title.pack(pady=20)
        
        main_frame = tk.Frame(self.root, bg='#f0f4f8')
        main_frame.pack(fill='both', expand=True, padx=20, pady=15)
        
        left_frame = tk.Frame(main_frame, bg='white', relief='ridge', bd=2)
        left_frame.pack(side='left', fill='y', padx=(0, 10), pady=10)
        
        tk.Label(
            left_frame,
            text="Add New Employee",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#2c3e50'
        ).pack(pady=(15, 10))
        
        tk.Label(left_frame, text="Name:", font=('Arial', 11), bg='white').pack(anchor='w', padx=20)
        self.name_entry = tk.Entry(left_frame, font=('Arial', 11), width=30)
        self.name_entry.pack(padx=20, pady=(0, 10))
        
        tk.Label(left_frame, text="Age:", font=('Arial', 11), bg='white').pack(anchor='w', padx=20)
        self.age_entry = tk.Entry(left_frame, font=('Arial', 11), width=30)
        self.age_entry.pack(padx=20, pady=(0, 10))
        
        tk.Label(left_frame, text="Department:", font=('Arial', 11), bg='white').pack(anchor='w', padx=20)
        self.department_var = tk.StringVar()
        self.department_dropdown = ttk.Combobox(
            left_frame,
            textvariable=self.department_var,
            values=['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'Operations', 'R&D'],
            font=('Arial', 11),
            width=27,
            state='readonly'
        )
        self.department_dropdown.pack(padx=20, pady=(0, 10))
        self.department_dropdown.set('Select Department')
        
        tk.Label(left_frame, text="Salary:", font=('Arial', 11), bg='white').pack(anchor='w', padx=20)
        self.salary_entry = tk.Entry(left_frame, font=('Arial', 11), width=30)
        self.salary_entry.pack(padx=20, pady=(0, 15))
        
        self.add_btn = tk.Button(
            left_frame,
            text="Add Employee",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            width=25,
            height=1,
            command=self.add_employee
        )
        self.add_btn.pack(pady=10)
        
        separator = tk.Frame(main_frame, bg='#bdc3c7', width=2)
        separator.pack(side='left', fill='y', padx=10)
        
        right_frame = tk.Frame(main_frame, bg='white', relief='ridge', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0), pady=10)
        
        tk.Label(
            right_frame,
            text="Employee Records",
            font=('Arial', 16, 'bold'),
            bg='white',
            fg='#2c3e50'
        ).pack(pady=(15, 10))
        
        search_frame = tk.Frame(right_frame, bg='white')
        search_frame.pack(pady=(0, 10))
        
        tk.Label(search_frame, text="Search:", font=('Arial', 11), bg='white').pack(side='left', padx=(20, 5))
        self.search_entry = tk.Entry(search_frame, font=('Arial', 11), width=20)
        self.search_entry.pack(side='left', padx=5)
        self.search_entry.bind('<KeyRelease>', self.search_employee)
        
        delete_frame = tk.Frame(right_frame, bg='white')
        delete_frame.pack(pady=(0, 10))
        
        tk.Label(delete_frame, text="Delete ID:", font=('Arial', 11), bg='white').pack(side='left', padx=(20, 5))
        self.delete_entry = tk.Entry(delete_frame, font=('Arial', 11), width=10)
        self.delete_entry.pack(side='left', padx=5)
        
        self.delete_btn = tk.Button(
            delete_frame,
            text="Delete",
            font=('Arial', 10),
            bg='#e74c3c',
            fg='white',
            command=self.delete_employee
        )
        self.delete_btn.pack(side='left', padx=5)
        
        action_frame = tk.Frame(right_frame, bg='white')
        action_frame.pack(pady=(0, 10))
        
        self.show_all_btn = tk.Button(
            action_frame,
            text="Show All",
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            width=15,
            command=self.show_all
        )
        self.show_all_btn.pack(side='left', padx=5)
        
        self.stats_btn = tk.Button(
            action_frame,
            text="Statistics",
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            width=15,
            command=self.show_stats
        )
        self.stats_btn.pack(side='left', padx=5)
        
        self.clear_btn = tk.Button(
            action_frame,
            text="Clear All",
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=15,
            command=self.clear_all
        )
        self.clear_btn.pack(side='left', padx=5)
        
        table_frame = tk.Frame(right_frame, bg='white')
        table_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        scroll_y = tk.Scrollbar(table_frame)
        scroll_y.pack(side='right', fill='y')
        
        scroll_x = tk.Scrollbar(table_frame, orient='horizontal')
        scroll_x.pack(side='bottom', fill='x')
        
        columns = ('ID', 'Name', 'Age', 'Department', 'Salary', 'Date Added')
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show='headings',
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
            height=15
        )
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')
        
        self.tree.column('Name', width=150)
        self.tree.column('Department', width=120)
        self.tree.column('Salary', width=100)
        
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        
        self.tree.pack(fill='both', expand=True)
        
        self.status_bar = tk.Label(
            self.root,
            text="Ready | Total Employees: 0",
            font=('Arial', 10),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='sunken',
            anchor='w'
        )
        self.status_bar.pack(side='bottom', fill='x')
        
    def add_employee(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        department = self.department_var.get()
        salary = self.salary_entry.get().strip()
        
        if not name or not age or not salary:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return
        
        if department == "Select Department":
            messagebox.showwarning("Warning", "Please select a department!")
            return
        
        try:
            age = int(age)
            if age < 18 or age > 70:
                messagebox.showwarning("Warning", "Age must be between 18 and 70!")
                return
        except:
            messagebox.showwarning("Warning", "Please enter a valid age!")
            return
        
        try:
            salary = int(salary)
            if salary < 10000:
                messagebox.showwarning("Warning", "Salary must be at least 10,000!")
                return
        except:
            messagebox.showwarning("Warning", "Please enter a valid salary!")
            return
        
        employee = {
            'ID': self.employee_id_counter,
            'Name': name,
            'Age': age,
            'Department': department,
            'Salary': salary,
            'Date Added': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.employees.append(employee)
        self.employee_id_counter += 1
        
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.department_var.set('Select Department')
        self.salary_entry.delete(0, tk.END)
        
        self.refresh_table()
        self.update_status()
        messagebox.showinfo("Success", f"Employee '{name}' added successfully! (ID: {self.employee_id_counter-1})")
    
    def delete_employee(self):
        employee_id_str = self.delete_entry.get().strip()
        
        if not employee_id_str:
            messagebox.showwarning("Warning", "Please enter an Employee ID!")
            return
        
        try:
            employee_id = int(employee_id_str)
        except:
            messagebox.showwarning("Warning", "Please enter a valid ID!")
            return
        
        for i, employee in enumerate(self.employees):
            if employee['ID'] == employee_id:
                del self.employees[i]
                self.delete_entry.delete(0, tk.END)
                self.refresh_table()
                self.update_status()
                messagebox.showinfo("Success", f"Employee ID {employee_id} deleted successfully!")
                return
        
        messagebox.showwarning("Warning", f"Employee ID {employee_id} not found!")
    
    def search_employee(self, event=None):
        search_term = self.search_entry.get().strip().lower()
        
        if not search_term:
            self.refresh_table()
            return
        
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        found = False
        for employee in self.employees:
            if search_term in employee['Name'].lower() or str(employee['ID']) == search_term:
                self.tree.insert('', 'end', values=(
                    employee['ID'],
                    employee['Name'],
                    employee['Age'],
                    employee['Department'],
                    f"{employee['Salary']:,}",
                    employee['Date Added']
                ))
                found = True
        
        if found:
            self.status_bar.config(text=f"Searching... Found matching employees")
        else:
            self.status_bar.config(text=f"No employees found for '{search_term}'")
    
    def show_all(self):
        self.search_entry.delete(0, tk.END)
        self.refresh_table()
        self.update_status()
    
    def show_stats(self):
        if not self.employees:
            messagebox.showinfo("Statistics", "No employees added yet!")
            return
        
        total = len(self.employees)
        avg_age = sum(e['Age'] for e in self.employees) / total
        avg_salary = sum(e['Salary'] for e in self.employees) / total
        
        departments = {}
        for e in self.employees:
            departments[e['Department']] = departments.get(e['Department'], 0) + 1
        
        most_popular_dept = max(departments, key=departments.get)
        
        stats_msg = f"""
EMPLOYEE STATISTICS

Total Employees: {total}
Average Age: {avg_age:.1f} years
Average Salary: {avg_salary:,.0f}
Most Popular Department: {most_popular_dept} ({departments[most_popular_dept]} employees)

Department Distribution:
"""
        for dept, count in departments.items():
            stats_msg += f"   {dept}: {count} employee(s)\n"
        
        messagebox.showinfo("Statistics", stats_msg)
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all records?"):
            self.employees.clear()
            self.employee_id_counter = 1
            self.refresh_table()
            self.update_status()
            messagebox.showinfo("Success", "All employees cleared!")
    
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for employee in self.employees:
            self.tree.insert('', 'end', values=(
                employee['ID'],
                employee['Name'],
                employee['Age'],
                employee['Department'],
                f"{employee['Salary']:,}",
                employee['Date Added']
            ))
    
    def update_status(self):
        total = len(self.employees)
        self.status_bar.config(text=f"Ready | Total Employees: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()