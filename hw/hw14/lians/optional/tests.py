import unittest
import functions
import functions_with_errors


class FunctionsTestCase(unittest.TestCase):
    @staticmethod
    def styled_msg(module, name, case, status, *args):
        color = 42 if status == "PASSED" else 41
        parts = [str(a) for a in args if a]
        args_str = ", ".join(parts)
        return f"In module \033[3;33m{module.__name__}\033[0m test \033[1;34m{name}(\033[0m{args_str}\033[34m)\033[0m when {case} is \033[{color}m{status}\033[0m"
    
    def test_greeting(self):
        for module in [functions, functions_with_errors]:
            print("")
            name = "greeting_by_name"
            
            tests = [
                ("empty name", "", "Hello !"),
                ("normal name", "Lians", "Hello Lians!"),
                ("name with spaces before", "  007", "Hello   007!")
            ]            
            for case, value, expected in tests:
                with self.subTest(module=module.__name__, case=case):
                    result = module.greeting_by_name(value)
                    if result != expected:
                        print(self.styled_msg(module, name, case, "FAILED", value))
                    else:
                        print(self.styled_msg(module, name, case, "PASSED", value))

    def test_symbol_position(self):
        text = "Testing different things"  
        for module in [functions, functions_with_errors]:
            print("")
            name = "get_symbol_position"
            
            tests = [
                ("right symbol position", text, "d", 9),
                ("symbol not found", text, "a", "Not found"),
                ("string instead of symbol", text, "ab", "Error! Symbol can be string with only one letter"),
                ("no symbol given", text, None, "Error! Symbol can be string with only one letter"),
            ]            
            for case, value_text, value_symbol, expected in tests:                
                with self.subTest(module=module.__name__, case=case):
                    try:
                        result = module.get_symbol_position(value_text, value_symbol)
                    except TypeError:
                        pass
                    if result == expected:
                        print(self.styled_msg(module, name, case, "PASSED"))
                    else:
                        print(self.styled_msg(module, name, case, "FAILED", text))                      
                    
    def test_merge(self):
        for module in [functions, functions_with_errors]:
            print("")
            name = "merge"   
            tests = [
                ("merged empty dicts", {}, {}, {}),
                ("merged empty dict with normal one", {}, {"a": 0, "b": 1, "c": 2}, {"a": 0, "b": 1, "c": 2}),
                ("merged two non-empty dicts", {"a": 0, "b": 1, "c": 2}, {"c": 3, "d": 4}, {"a": 0, "b": 1, "c": 3, "d": 4})
            ]         
            
            for case, d1, d2, expected in tests:
                with self.subTest(module=module.__name__):
                    d1_before, d2_before = d1.copy(), d2.copy()
                    result = module.merge(d1, d2)
                    if result == expected:
                        print(self.styled_msg(module, name, case, "PASSED", d1_before, d2_before))
                    else:
                        print(self.styled_msg(module, name, case, "FAILED", d1_before, d2_before))
                        
                    for label, current, original in [
                        ("first", d1, d1_before),
                        ("second", d2, d2_before)
                    ]:
                        status = "PASSED" if current == original else "FAILED"
                        print(self.styled_msg(module, name, f"check immutability or the {label} dict", status))


if __name__ == "__main__":
    unittest.main()