# oop.py

class MyClass:
    'MyClass store information such as: name, occupation, field, nationality' # __doc__
    my_name = 'la'
    my_occupation = 'teacher'
    my_special_field = 'Python'
    _gender = 'male'    # protected (convention/traditional), should only access in class/subclass
    __my_nationality = 'Lao'        # name mangling/private => _MyClass__my_nationality

    def __init__(self, my_name='', my_occupation='', my_special_field=''):
        self.my_name = my_name
        self.my_occupation = my_occupation
        self.my_special_field = my_special_field

    def get_info(self):
        print(self.my_name)
        print(self.my_occupation)
        print(self.my_special_field)
    
    def how_to_success(self):
        print('To success, just keep coding...')

    def how_long(self, years=1):
        print('To success, just keep coding', years, 'year(s)')

print(MyClass.my_name)
print(MyClass.my_occupation)
print(MyClass.my_special_field)

my_first_instance = MyClass('first name', 'first student', 'JS')
print('\nMY FIRST INSTANCE >_')
print(my_first_instance.my_name)
print(my_first_instance.my_occupation)
print(my_first_instance.my_special_field)
print(my_first_instance._gender)
# this is not directly modify __my_nationality it just create new attr
my_first_instance.__my_nationality = 'Thai' 
print('NEWLY CREATE ATTR', my_first_instance.__my_nationality)
print('ENCAPSULATED PRIVATE MANGLING NAME', MyClass._MyClass__my_nationality)
my_first_instance.how_to_success()
my_first_instance.how_long(2)

print('\nMY SECOND INSTANCE >_')
my_second_instance = MyClass()
my_second_instance.my_name = 'second name'
my_second_instance.my_occupation = 'second student'
my_second_instance.my_special_field = 'PHP'
my_second_instance.get_info()
my_second_instance.how_to_success()
my_second_instance.how_long(3)
my_second_instance.new_attribute = 'this is newly add attribute'
print('NEWLY ADD ATTRIBUTE: ', my_second_instance.new_attribute)

# class inheritance
class MySubClass(MyClass):
    def get_info(self):
        return super().get_info()
    
    def my_skill(self, skill_list=[]):
        print('skills: ', skill_list)
    
print('\nMY SUB CLASS >_')
my_sub_class_instance = MySubClass('sub name', 'sub teacher', 'Flutter')
my_sub_class_instance.get_info()
my_sub_class_instance.my_skill(['HTML', 'CSS', 'Django'])

# getattr()
print('\ngetattr() METHOD: ', getattr(my_second_instance, 'new_attribute'))

# hasattr()
print('\nhasattr() METHOD: ', hasattr(my_second_instance, 'new_attribute'))

# setattr()
setattr(my_second_instance, 'last_attribute', 'this is last attribute')
print('\nsetattr() METHOD: ', getattr(my_second_instance, 'last_attribute'))

# delattr()
delattr(my_second_instance, 'last_attribute')
print('\ndelattr() METHOD: ', hasattr(my_second_instance, 'last_attribute'))

# built-in attribute
print('\nBUILT-IN ATTR NAME', MyClass.__name__)
print('BUILT-IN ATTR DOC', MyClass.__doc__)
print('BUILT-IN ATTR DICT', MyClass.__dict__)
print('BUILT-IN ATTR MODULE', MyClass.__module__)