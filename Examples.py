# Create in Python 3.8.5
# Import Library
import winreg

# Global variables

sub_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
key = "Run"
path = sub_path + key

############### CREATE KEY ################
def createKey():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # sub_path can be empty
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)

############### SET VALUE EX ################
def setValueEx():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)    # Error if key is emply
    name_value = "Valor"
    value = "soy un valor"
    # Create value
    winreg.SetValueEx(opened_key, name_value, 0, winreg.REG_EXPAND_SZ, value)


############### SET VALUE ################
def setValue():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    name_value = "Valor"
    value = "soy un valor"
    # Create value
    #winreg.SetValue(opened_key, name_value, 0, winreg.REG_EXPAND_SZ, value)
    winreg.SetValue(winreg.HKEY_CURRENT_USER, key ,winreg.REG_SZ,value)




############### DELETE VALUE ################
def deleteValue():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    # Create value
    winreg.DeleteValue(opened_key, name_value)

############### DELETE KEY x86 ################
def deleteKey():
    # This method can not delete keys with subkeys.
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER,sub_path)

############### DELETE KEY x64 ################
def deleteKeyEx():
    # This method can not delete keys with subkeys.
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER,sub_path)

setValueEx()





# Read Documentation:
# https://docs.python.org/3/library/winreg.html