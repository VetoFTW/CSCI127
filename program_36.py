# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 17, 2021

def worldRecord(gender, event):

    time = 0.0
    
    if gender == "men":
        if event == 100:
            time = 9.63
        elif event == 200:
            time = 19.30
        elif event == 400:
            time = 43.03
        else:
            return -1

    elif gender == "women":
        if event == 100:
            time = 10.62
        elif event == 200:
            time = 21.34
        elif event == 400:
            time = 48.25
        else:
            return -1
            
    else:
        return -1

    return(time)

def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+" 's "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()