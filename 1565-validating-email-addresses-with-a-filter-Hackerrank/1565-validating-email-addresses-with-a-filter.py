def fun(s):
    if s.count("@")==1 and s.count(".")==1: 
        username,remain=s.split("@")
        website,extension=remain.split(".")
    else:
        return False
    username=username.replace("-","")
    username=username.replace("_","")
    if not username.isalnum():
        return False          
    if not website.isalnum() :
        return False   
    if len(extension)>3 or  not extension.isalpha():
        return False
    
    return True
    # return True if s is a valid email, else return False



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna