"""WRAPPER PROGRAM
Logan Halstrom
MAE 298 AEROACOUSTICS
HOMEWORK 4 - TURBOMACHINERY NOISE
CREATED: 17 NOV 2016
MODIFIY: 17 NOV 2016

DESCRIPTION: Run data processing and plotting programs with common inputs.
"""

#IMPORT GLOBAL VARIABLES AND PROGRAMS TO WRAP
from hw1_98_globalVars import *
import hw1_00_process as process
import hw1_01_plot as plot


def main(source):
    """input description
    """

    print('\nProcessing Data')
    process.main(source)
    print('\nPlotting Data')
    plot.main()


if __name__ == "__main__":


    Source = 'Boom_F1B2_6.wav'

    main(Source)

