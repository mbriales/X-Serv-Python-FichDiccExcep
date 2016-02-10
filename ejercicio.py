#!/usr/bin/python
# -*- coding: utf-8 -*-
# Miguel Briales Romanillos

# Opens and reads file
File_Users = open("/etc/passwd")  # No tiene "modo" -> Por defecto es "Read"
User_Names = File_Users.readlines()

# Searches user names
User_List = {}
for Users in User_Names:
    if Users.find('#'):   # For delete comments
        # Looks for user
        End_User = Users.find(':*:')
        User = Users[:End_User]
        # Looks for shell
        Users_Reverted = Users[::-1]
        Start_Shell = Users_Reverted.find(':')
        Shell = Users_Reverted[:Start_Shell]
        Shell = Shell[::-1]

# Writes the dictionary
        User_List[User] = Shell

# Prints number of users
print ('Hay ' + str(len(User_List)) + ' usuarios\n')

# Prints "root" and "imaginary" user
try:
    print 'Usuario root: '
    print User_List['root']
    print 'Usuario imaginario %d:' % User_List['imaginario']
# In case an user doesn't exist
except:
    print 'ERROR! El usuario introducido no existe\n'
