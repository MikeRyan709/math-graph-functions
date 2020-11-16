'''
IMPORTANT: the Matplotlib and Numpy modules MUST be installed via the terminal for this program to run properly
'''

import matplotlib.pyplot as plt #imports the module matplotlib.
import numpy as np #imports the module numpy
from math import sqrt #imports the square root function from the math module

while True:
    function = input("Please select a graph type: ") #users will input  an accepted function


    if function.lower() == "linear" or function.lower() == "line":
        
        print("linear graphs are in the form of f(x) = a*x+b") #shows the equation of the selected graph
      
      #the user inputs the values for the equation and the range 
        a = int(input("please provide a value for a: ")) 
        b = int(input("please provide a value for b: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        
      #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
        x = np.linspace(start_range, end_range,)
        y = a *x + b
        plt.plot(x, y)
        plt.legend(['f(x) = a*x+b'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
        
        
    if function.lower() == "quadratic" or function.lower() == "quad":
        
        print("quadratic graphs are in the form of f(x) = a*x^2 + b*x + c") #gives the equation to the user
    #the user inputs the values for the equation and the range 
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
       
        #calcuations to create, save or dispaly the graph
        x = np.linspace(start_range, end_range,)
        y = a*x**2 + b + c 
        plt.plot(x, y)
        plt.legend(['f(x) = a*x^2 + b*x + c'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ") #asks if the user wishs to save or display the created graph
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the use whishes to continue making graphs
        if cont.upper() == "N":
            break
            
    
    if function.lower() == "cubic" or function.lower() == "cube":
        print("Cubic graphs are in the form of f(x) = a*x^3 + b*x^2 + c*x + d") #prints the equation for the user to see
       
    #the user inputs the values for the equation and the range 
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        d = int(input("Please provide a value for d: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
        x = np.linspace(start_range, end_range,)
        y = (a*x**3) + (b*x**2) + (c*x) + d
        plt.plot(x, y)
        plt.legend(['f(x) = a*x^2 + b*x + c'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
    
   
   
    if function.lower() == "quartic" or function.lower() == "quart":
        print("Quartic graphs are in the form of f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e") #dispalys the equation to the user
     #the user inputs the values for the equation and the range 
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        d = int(input("Please provide a value for d: "))
        e = int(input("please provide a value for e: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
        x = np.linspace(start_range, end_range,)
        y = (a*x**4) + (b*x**3) + (c*x**2) + (d*x) + e
        plt.plot(x, y)
        plt.legend(["f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e"])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ") 
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
    
    
    
    if function.lower() == "exponential" or function.lower() == "exp":
        print("Exponential graphs are in the form of f(x) = a*b^(c*x + d)") #prints the equation to the user
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
        a = int(input("please provide a value for a: "))
        b = int(input("please provide a value for b: "))
        c = int(input("please provide a value for c: "))
        d = int(input("Please provide a value for d: "))
        start_range = int(input("Please input the start of the range: "))
        end_range = int(input("Please input the end of the range: "))
        
        x = np.linspace(start_range, end_range,)
        y = a*b**(c*x + d)
        plt.plot(x, y)
        plt.legend(['f(x) = a*b^(c*x + d)'])
        save_dispaly = input("would you like to display the graph or save it to a file? (S / D): ")
        
        if save_dispaly.upper() == "S":
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
    
    
    if function.lower() == "logarithmic" or function.lower() == "log":
        print("logarithmic graphs are in the form of f(x) = a*log(b*x + c)") #prints the equation to the user
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
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
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
        
    


    if function.lower() == "sine" or function.lower() == "sin":
        print("sine graphs are in the form of f(x) = a*sin(b*x + c)") #prints the equation to the user
        #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
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
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N) :" ) #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
        
    
    
    
    if function.lower() == "cosine" or function.lower() == "cos":
        print("sine graphs are in the form of f(x) = a*cos(b*x + c)") #prints the equation to the user
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
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
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
        
    
    
    
    if function.lower() == "Square root" or function.lower() == "sqrt":
        print("square root graphs are in the form of f(x) = a*sqrt(b*x + c)") #prints the equation to the user
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
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
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break
    
    
    
    if function.lower() == "cube root" or function.lower() == "cbrt":
        print("logarithmic graphs are in the form of f(x) = a*(b*x + c)^(1/3)") #prints the equation to the user
    #equations that will create a graph and ask if the user wishes to save it as a png or dispaly it.
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
            file_name = input("what would you like the file name to be: ") #asking for a name to save the png as.
            plt.savefig(file_name)
        
        elif save_dispaly.upper() == "D":
            plt.show()
        
        cont = input("would you like to continue? (Y/N): ") #asks if the user wishes to create another graph
        if cont.upper() == "N":
            break