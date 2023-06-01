"""
1. Scatter Plot: Test the scatterPlot() method to ensure proper visualization.
2. Histogram: Test the histogram() method to ensure proper visualization.
3. Box Plot: Test the boxPlot() method to ensure proper visualization.
4. Linear Regression: Test the linearRegres() method to ensure the calculation and output are correct.
5. Data Summary: Test the datasetSummary() method to ensure proper summary statistics and information are displayed.

TESTS COMPLETED:

1. Splitting: Successfully tested splitting the dataset based on column selection.
2. Formatting: Successfully tested formatting the dataset for use with plotting methods.
3. Pickle DUMP: Successfully tested dumping the Statify object using the pickle module.
4. Pickle LOAD: Successfully tested loading the Statify object using the pickle module.
5. Archive: Successfully tested the archiving functionality for the dataset.
6. Archive_data: Successfully tested the data retrieval from the archived dataset.
"""


from StatifyPy import Statify

test = Statify('Data.csv',['x','y'])

test.datasetSummary()

test.dotPlot()
test.boxPlot(title='Box', label_x= 'X', label_y='Y')


test.modify(['x'])
test.dotPlot()
test.boxPlot(title='Box', label_x= 'X', label_y='Y')


#test.linearRegres(['x','y'])  #error because modified to [x] only

test.modify(['x','y'])

print(test._Statify__column_dict)
test.linearRegres(['x','y'])

'''
for value in test.column_values_gen("x"):
    print(value)
'''

test.scatterPlot(['x','y'], regression=True)
test.linearRegres(['x','y'], graph=True)
test.scatterPlot(['y','x'])





