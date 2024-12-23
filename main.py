#Wind Component Calculator
#The crosswind component is equal to the speed (V) of the wind multiplied by the sine of the angular difference (XWC = V × Sineθ)
#User inputs, wind direction/speed, runway heading.

#Calculate based off metar at a given airport

import math

#function to calculate angular difference, to reduce repeating code
def angular_difference(wind_direction, runway_heading):
    
    wind_direction = normalise_heading(wind_direction)
    runway_heading = normalise_heading(runway_heading)
    
    angular_difference = (wind_direction - runway_heading) % 360
    #Convert to radians
    
    angular_difference_radians = math.radians(angular_difference)
    
    return angular_difference_radians
    

def crosswind_calculate(speed, angular_difference_radians):
        

    crosswind = speed * math.sin(angular_difference_radians)
    
    #Calculate direction
    
    if crosswind < 0:
        crosswind = abs(crosswind)
        print(f"The crosswind component is: {crosswind:.2f} knots from the left")
        
    else:
        print(f"The crosswind component is: {crosswind:.2f} knots from the right")
   


def tail_head_wind_calculate(speed, angular_difference_radians):
     #Calculate Angular difference
   
    #Headwind or tailwind speed = wind speed × cos (α)
    head_tail_wind = speed * math.cos(angular_difference_radians)
    
    if head_tail_wind < 0:
        print(f"The tailwind component is {head_tail_wind:.2f} knots")
    
    elif head_tail_wind > 0:
        print(f"The head wind component is {head_tail_wind:.2f} knots")
        
    else:
        print("Nil head or tail wind")
    
        
 
#Funcion to allow inputs of 0, returns it as 360
def normalise_heading(heading):
    return 360 if heading == 0 else heading 
        
    

def error_check(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if max_val is None:
                if value < min_val:
                    print(f"Please enter a number greater than or equal to {min_val}")
                    continue
            else:
                if value < min_val or value > max_val:
                    print(f"Please enter a number between {min_val} and {max_val}")
                    continue
        
        except ValueError:
            print("Please enter a number")
            
        else:
            return value
    
    
    
def user_input():
    print("Crosswind Calculator")
    
    #Get user inputs, and run through error check
    speed = error_check("Enter windspeed in knots: ", 0, None) #0 represents the min val of 0, and float(inf) represents max value of infiity
    wind_direction = error_check("Enter Wind Direction in Magnetic: ", 0, 360)
    runway_heading = error_check("Enter Runway Heading in Magnetic: ", 0, 360)
    

    angular_difference_radians = angular_difference(wind_direction, runway_heading)
    crosswind_calculate(speed, angular_difference_radians)
    tail_head_wind_calculate(speed, angular_difference_radians)
    
    
    
user_input()