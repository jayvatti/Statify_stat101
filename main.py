from StatifyPy.Statify import Statify

import sys
import os


def main():
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_dir)
    """

    test = Statify('Data.csv', ['x', 'y'])

    '''
    test = Statify('Data.csv', ['x', 'y'])
    test.datasetSummary()

    for value in test.column_values_gen("x"):
        print(value)

    test.scatterPlot(['x','y'], regression=True)
    test.linearRegres(['x','y'], graph=True)
    test.scatterPlot(['y','x'])
    test.dotPlot()
    test.boxPlot(title='Box', label_x='X', label_y='Y')
    test.modify(['x'])
    test.dotPlot()
    test.boxPlot(title='Box', label_x='X', label_y='Y')
    test.modify(['x', 'y'])
    test.linearRegres(['x', 'y'])
    test.modify(['x'])
    test.histogram()
  '''

if __name__ == "__main__":
    main()
