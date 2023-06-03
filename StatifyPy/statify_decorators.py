

class Decorators:
    @staticmethod
    def plot_name_decorator(plot_name):
        def decorator(plot_func):
            def wrapper(*args, **kwargs):
                print(f"Plotting {plot_name}...")
                result = plot_func(*args, **kwargs)
                print(f"{plot_name} plotted!", end='\n\n\n')
                return result

            return wrapper
        return decorator

    @staticmethod
    def gen_decorator(before, after):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"{before}...")
                result = func(*args, **kwargs)
                print(f"{after}!", end='\n\n')
                return result
            return wrapper
        return decorator


