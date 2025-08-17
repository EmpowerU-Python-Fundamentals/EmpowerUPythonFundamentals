class MyClass:

    @staticmethod
    def rename_class(original_class, new_name):
        return type(new_name, original_class.__class__.__bases__, dict(original_class.__class__.__dict__))

