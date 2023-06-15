# validation.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import re # regular expression

# ################
# Validation Class
# ################

class Validation():

    def is_numeric(self, val):
        val = str(val) # only str have the isnumeric() method
        ###############
        if "-" in val[0]:
            val = val[1:] #if negative numbers are considered numeric, this includes negatives
        ###############
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False

    def is_phone_number(self, val):
        val = str(val)
        if re.search(r'(^\d{2} \d{4} \d{4})', val): # 02 9999 9999
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False

    def is_email(self, val):
        val = str(val)
        # Check that it has exactly one @ sign,
        # and at least one . in the part after the @
        ############# - changed to include "." after the "@" symbol
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', val):
        ############# - changed to include "." after the "@" symbol
        #if re.search(r'\w+@\w+', val):
            print("Valid email")
            return True
        else:
            print("Invalid email")
            return False


    pass

# ###########
# Main method
# ###########

# The main method is only executed when the file is 'run' (not imported in another file)

if __name__ == '__main__':
    # Instead of writing separate test scripts, could write them here
    # The test scripts would not be executed when the file is imported into another one
    pass