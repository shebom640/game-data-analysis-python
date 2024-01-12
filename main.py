# TO INSTALL REQUIRED DEPENDENCIES RUN:
# python3 -m pip install pandas matplotlib seaborn plotly

from models.data_frame_info import data_frame_info
from models.bar_plot import bar_plot
from models.pie_chart import pie_chart
from models.box_plot import box_plot
from models.line_plot import line_plot
from models.three_dimensional_plot import three_dimensional_plot

print("File 1: Data Frame Info \nFile 2: Bar Plot \nFile 3: Pie Chart Plot \nFile 4: Box Plot \nFile 5: Line Plot \nFile 6: 3D Plot")

user_input = input("Enter File Number to run: ")

if user_input == '1':
    print('Data Frame Info')
    data_frame_info()
elif user_input == '2':
    print('Bar Plot')
    bar_plot()
elif user_input == '3':
    print('Pie Chart Plot')
    pie_chart()
elif user_input == '4':
    print('Box Plot')
    box_plot()
elif user_input == '5':
    print('Line Plot')
    line_plot()
elif user_input == '6':
    print('3D Plot')
    three_dimensional_plot()
else: 
    print("Error occured!")
    print("Choose between 1 to 6 [Both Inclusive]")
