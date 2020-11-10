import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

while True:
    function = input("Please select a graph type: ")

    if function.lower() == "logarithmic" or function.lower() == "log":
        print("logarithmic graphs are in the form of f(x) = a*log(b*x + c)")
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        
        x = np.linspace(start_range, end_range)
        plt.yscale('log')
        plt.plot(x, np.log(b*x+c) *a, lw = 2., label = r'$f(x)=\log(x)$')
        plt.legend()
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ")
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ")
        if cont.upper() == "N":
            break
        
    


    if function.lower() == "sine" or function.lower() == "sin":
        print("sine graphs are in the form of f(x) = a*sin(b*x + c)")
        a = float(input("please provide a value for a: "))
        b = float(input("please provide a value for b: "))
        c = float(input("please provide a value for c: "))
        start_range =float(input("Please input the start of the range: "))
        end_range = float(input("Please input the end of the range: "))
        
        x = np.linspace(start_range, end_range,)
        y = np.sin(b*x + c) * a
        plt.plot(x, y,)
        plt.legend('sin(x)')
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ")
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N) :" )
        if cont.upper() == "N":
            break
        
    
    
    
    if function.lower() == "cosine" or function.lower() == "cos":
        print("sine graphs are in the form of f(x) = a*cos(b*x + c)")
        a = float(input("please provide a value for a: "))
        b = float(input("please provide a value for b: "))
        c = float(input("please provide a value for c: "))
        start_range =float(input("Please input the start of the range: "))
        end_range = float(input("Please input the end of the range: "))
        
        x = np.linspace(start_range, end_range,)
        y = np.cos(b*x + c) * a
        plt.plot(x, y)
        plt.legend(['cos(x)'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ")
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ")
        if cont.upper() == "N":
            break
        
    
    
    
    if function.lower() == "Square root" or function.lower() == "sqrt":
        print("square root graphs are in the form of f(x) = a*sqrt(b*x + c)")
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        x = np.linspace(start_range, end_range,)
        z = (b * x + c)
        y = np.sqrt(z) *a
        plt.plot(x, y)
        plt.legend(['f(x) = a*sqrt(b*x + c)'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ")
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ")
        if cont.upper() == "N":
            break
    
    
    
    if function.lower() == "cube root" or function.lower() == "cbrt":
        print("logarithmic graphs are in the form of f(x) = a*(b*x + c)^(1/3)")
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        x = np.linspace(start_range, end_range,)
        y = a*(b*x + c)**(1/3)
        plt.plot(x, y)
        plt.legend(['f(x) = a*(b*x + c)^(1/3)'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ")
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ")
        if cont.upper() == "N":
            break