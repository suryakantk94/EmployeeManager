import pandas as pd
import xlwt

from django.shortcuts import render,redirect
from manager.models import Employee
from manager.forms import EmployeeForm
from datetime import datetime
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemployee.html", {'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees':employees})

def showinexcel(request):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Employee Details")
    
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.num_format_str = "D-MMMM-YYYY"
    font_style.name = "Times New Roman"
    font_style1 = xlwt.XFStyle()
    font_style1.font.colour_index = xlwt.Style.colour_map['light_blue']
    
    # pattern = xlwt.Pattern()
    # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']
    # font_style.pattern = pattern
    columns = ['Employee ID', 'Name', 'Contact', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)    #eg - (0,0, 'Employee ID')

    rows = Employee.objects.all().values_list('eid', 'ename', 'econtact', 'eemail')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style1)
    
    ws.write(row_num+5,0,datetime.now(),font_style)        

    wb.save("EmpDetails.xls")
    return render(request, "index.html")



def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {'employee':employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')




