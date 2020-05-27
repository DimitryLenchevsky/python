import my_module
import new_pkg

print(my_module.MY_CONST)
print(my_module.my_func())
print(new_pkg.pk_var)
print(new_pkg.module1.MY_MEGA_CONST)

from datetime import datetime
print(datetime.now())

#или
#import datetime
#print(datetime.datetime.now())