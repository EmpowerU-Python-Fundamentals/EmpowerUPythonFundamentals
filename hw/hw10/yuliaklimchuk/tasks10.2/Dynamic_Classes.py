# Note: Proposed function should allow only names with alphanumeric chars 
# (upper & lower letters plus ciphers), but starting only with upper case letter. 
# In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases,
#  but let's stick with that, that Timmy yet has to learn them.


def class_name_changer(cls, new_name):

    if not (new_name and new_name[0].isupper() and new_name.isalnum()):
        return "Class name must start with an uppercase letter and contain only alphanumeric characters."
    cls.__name__ = new_name
    return cls