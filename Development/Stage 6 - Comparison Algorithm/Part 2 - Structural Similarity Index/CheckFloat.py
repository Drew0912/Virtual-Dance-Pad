def CheckFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False            
        