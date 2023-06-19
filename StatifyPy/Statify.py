import numpy as np
import pandas as pd
import statistics
from matplotlib import pyplot as plt
from scipy import stats
import copy

from StatifyPy.ErrorStat import TempError, StatsError

from StatifyPy.statify_plots import Plots
from StatifyPy.calculations import Calculations

from StatifyPy.statify_decorators import Decorators


class Statify:

    @Decorators.gen_decorator("Initialising...", "Instance Created!")
    def __init__(self, file_name, column_list):
        self.file_name = file_name
        self.__column_list = column_list
        self.__dict, self.pdata = self.__read_csv()
        self.__column_dict = {}
        self.modify(column_list)
        self.__plotting_methods = Plots()

    @property
    def returnPD(self):
        return self.pdata

    def __str__(self):
        print(f"Filename = {self.file_name}")
        print(f"Selected Columns = {self.__column_list}")
        print(f"Columns in Data = {self.__dict.keys()}", end='\n\n')
        return ''

    @classmethod
    def space_delimiter(self, space_file_name, csv_file_name):
        try:
            with open(space_file_name) as infile:
                data = infile.read().replace(' ', ',')
                print(data, file=open(csv_file_name, 'w'))
        except Exception as e:
            print(f"{space_file_name} does not EXIST!")
            print(f"Exception: {e}", end="\n\n")

    @Decorators.gen_decorator("Reading CSV file...", "Reading Completed!")
    def __read_csv(self):
        try:
            csv_file = pd.read_csv(self.file_name)
            data_dict = csv_file.to_dict(orient='list')
            return data_dict, csv_file
        except Exception as e:
            print(f"{self.file_name} does not EXIST!")
            print(f"Exception: {e}", end="\n\n")
            return [{"INVALID": [0, 0]}, pd.DataFrame()]

    @Decorators.gen_decorator("Modifying Columns...","Columns Modified!")
    def modify(self, columns):
        self.__column_list = columns
        temp = self.__dict.copy()
        for i in self.__dict.keys():
            if i not in self.__column_list: temp.pop(i)
        self.__column_dict = temp

    def linearRegres(self, indexes, graph=False):
        try:

            if len(indexes) != 2:
                raise TempError('{IDX != 2}', f'INVALID LEN ={len(indexes)}', 'linear_regres')

            result = stats.linregress(self.__column_dict[indexes[0]], self.__column_dict[indexes[1]])

            print("LINEAR REGRESSION:")
            print(f'Slope:      {result.slope}')
            print(f'Intercept:  {result.intercept}')
            print(f'r:          {result.rvalue}')
            print(f'R: (r^2)    {result.rvalue ** 2}', end="\n\n")
            print(f'EQUATION:   y = {result.slope:.6f}x + {result.intercept:.6f}', end="\n\n")
            print("--------------------\n")

            if graph:
                plt.scatter(self.__column_dict[indexes[0]], self.__column_dict[indexes[1]], color='blue', label='Data')
                reg_line = result.intercept + result.slope * np.array(self.__column_dict[indexes[0]])
                plt.plot(self.__column_dict[indexes[0]], reg_line, color='red', label='Linear Regression')
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Linear Regression')
                plt.show()

        except StatsError as e:
            print('ERROR:', e.error, e.args[-1], sep=': ')

    # column rows generator
    def column_keys_gen(self):
        for key in self.__column_dict.keys():
            yield key

    # column values generator
    def column_values_gen(self, column_key):
        if column_key in self.__column_dict:
            for value in self.__column_dict[column_key]:
                yield value
        else:
            print(f"Column '{column_key}' not found.")

    # noinspection PyArgumentList
    @Decorators.plot_name_decorator("Dot Plot")
    def dotPlot(self, label_y="Frequency"):
        self.__plotting_methods.dotPlot(self.pdata, label_y)

    # noinspection PyArgumentList
    @Decorators.plot_name_decorator("Box-Whisker Plot")
    def boxPlot(self, title='Box-Whisker Plot', label_x='Values', label_y='Groups'):
        self.__plotting_methods.boxPlot(self.__column_dict, title, label_x, label_y)

    # noinspection PyArgumentList
    @Decorators.plot_name_decorator("Histogram")
    def histogram(self, label_y='Frequency', bins=0):
        self.__plotting_methods.histogram(self.__column_dict, label_y='Frequency', bins=0)

    # noinspection PyArgumentList
    @Decorators.plot_name_decorator("Scatter Plot")
    def scatterPlot(self, order=None, label_x=None, label_y=None, regression=False):
        if order is None: order = self.__column_list
        if label_x is None: label_x = self.__column_list[0]
        if label_y is None: label_y = self.__column_list[1]
        self.__plotting_methods.scatterPlot(self.__column_dict, order, label_x, label_y, regression)

    # data set summary
    def datasetSummary(self):
        try:
            kwargs = copy.deepcopy(self.__column_dict)
            for i in kwargs.keys():
                print(f"SUMMARY OF '{i}':", end="\n\n")
                kwargs[i].sort()
                print("this graph is 'SKEWED RIGHT'") if (
                        statistics.mean(kwargs[i]) > statistics.median(kwargs[i])) else print(
                    "this graph is 'SKEWED LEFT'")
                print("\n")
                data = np.array(kwargs[i])
                x = pd.Series(data)
                print(f'var      {statistics.variance(kwargs[i])}')
                print(f'10%mean  {stats.trim_mean(kwargs[i], 0.1)}')
                quartiles = np.percentile(data, [25, 50, 75])
                IQR = quartiles[2] - quartiles[0]
                print(f'IQR      {IQR}')
                print(f'summary  ({min(kwargs[i])},{quartiles[0]},{quartiles[1]},{quartiles[2]},{max(kwargs[i])})',
                      end="\n\n")
                print(f'uf       {quartiles[2] + (1.5 * IQR)}')
                print(f'lf       {quartiles[0] - (1.5 * IQR)}', end='\n\n')
                print(x.describe(), end='\n---------------------\n\n')
        except Exception as e:
            print(e.args)

    @staticmethod
    @Decorators.gen_decorator("NormalPDF:\n", "\n\n")
    def normalpdf(x, mean=0, std_dev=1):
        return Calculations.normal_pdf(x, mean, std_dev)

    #testing needed
    @staticmethod
    @Decorators.gen_decorator("NormalCDF:\n","\n\n")
    def normalcdf(x, mean=0, std_dev=1):
        return Calculations.normal_cdf(x, mean, std_dev)

    @staticmethod
    @Decorators.gen_decorator("BinomPDF:\n", "\n\n")
    def binompdf(success, trails, p):
        return Calculations.binomial_pmf(success, trails, p)

    @staticmethod
    @Decorators.gen_decorator("BinomCDF:\n", "\n\n")
    def binomcdf(success, trails, p):
        return Calculations.binomial_cdf(success, trails, p)

    @staticmethod
    @Decorators.gen_decorator("tPDF:\n", "\n\n")
    def tpdf(x,df):
        return Calculations.t_pdf(x, df)

    @staticmethod
    @Decorators.gen_decorator("tCDF:\n", "\n\n")
    def tcdf(lower, upper, df):
        return Calculations.t_cdf(lower,upper,df)

    @staticmethod
    @Decorators.gen_decorator("invNorm:\n", "\n\n")
    def invNorm(p, mean=0, std_dev=1, test="LEFT"):
        return Calculations.inv_norm(p, mean,std_dev, test)

    @staticmethod
    @Decorators.gen_decorator("invT:\n", "\n\n")
    def invT(p, df, test="DEFAULT"):
        return Calculations.inv_t(p,df,test)

    @staticmethod
    @Decorators.gen_decorator("anova:\n","\n\n")
    def anova(data, dependent_variable, factor_variable):
        return Calculations.anova(data,dependent_variable,factor_variable)


if __name__ == "__main__":
    print(__name__)
