#-------------------------------------------
#Andrew Lee
#File name: CheckFloat.py
#-------------------------------------------

#Check if value is a float/real function
def CheckFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False      

""" aklshdah """