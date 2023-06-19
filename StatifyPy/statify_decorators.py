import inspect


class Decorators:

    # wrapper that accepts a param(plot_name)
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

    # wrapper that accepts a param(before,after)
    @staticmethod
    def gen_decorator(before, after):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"{before}")
                result = func(*args, **kwargs)
                print(f"{after}!", end='\n\n')
                return result

            return wrapper

        return decorator

    @staticmethod
    # wrapper that accepts a param(before,after): HELP REPLICATOR
    # IN PROGRESS 
    def arg_kwarg_decorator(before, after):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"{before}")
                sig = inspect.signature(func)
                param_names = list(sig.parameters.keys())
                print("Parameter names:", param_names)
                if kwargs:  # If kwargs is not empty, print it
                    print(kwargs)
                else:  # If kwargs is empty, print args
                    print(args)
                result = func(*args, **kwargs)
                print(f"{after}!", end='\n\n')
                return result

            return wrapper

        return decorator
