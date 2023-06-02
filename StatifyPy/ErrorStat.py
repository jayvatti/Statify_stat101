class StatsError(Exception):
    def __init__(self, error, message):
        Exception.__init__(self, error, message)
        self.error = error


class PlotError(StatsError):
    def __init__(self, error, message, plot):
        StatsError.__init__(self, error, message)
        self.plot = plot


class FileError(StatsError):
    def __init__(self, error, message, csv_file_name, space_file_name=''):
        StatsError.__init__(self, error, message)
        self.csv_file_name = csv_file_name
        self.space_file_name = space_file_name


class TempError(StatsError):
    def __init__(self, error, message, temp):
        StatsError.__init__(self, error, message)
        self.temp = temp

