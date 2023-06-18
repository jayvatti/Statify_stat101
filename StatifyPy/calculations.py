#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:16:09 2023

@author: sujayvatti
"""

import numpy as np
from scipy.stats import norm, binom, t
from statsmodels.formula.api import ols
import statsmodels.api as sm

from StatifyPy.ErrorStat import TempError


class Calculations:
    @staticmethod
    def normal_pdf(x, mean=0, std_dev=1):
        return norm.pdf(x, mean, std_dev)

    @staticmethod
    def normal_cdf(x, mean=0, std_dev=1):
        return norm.cdf(x, mean, std_dev)

    @staticmethod
    def binomial_pmf(k, n, p):
        # success: k
        # trails: n
        # probability: p
        return binom.pmf(k, n, p)

    @staticmethod
    def binomial_cdf(k, n, p):
        # success: k
        # trails: n
        # probability: p
        return binom.cdf(k, n, p)

    @staticmethod
    def t_pdf(x, df):
        return t.pdf(x, df)

    @staticmethod
    def t_cdf(lower,upper, df):
        return t.cdf(upper, df) - t.cdf(lower, df)

    # _d = default

    @staticmethod
    def inv_normal_d(p, mean=0, std_dev=1):
        return norm.ppf(p, mean, std_dev)

    @staticmethod
    def inv_t_d(p, df):
        return t.ppf(p, df)

    @staticmethod
    def inv_norm(p, mean=0, std_dev=1, test="DEFAULT"):
        try:
            if test == "LEFT" or test == "DEFAULT":
                return Calculations.inv_normal_d(p, mean, std_dev)
            elif test == "RIGHT":
                return Calculations.inv_normal_d(1 - p, mean, std_dev)
            elif test == "CENTER":
                # p is alpha
                return Calculations.inv_normal_d(p / 2, mean, std_dev), Calculations.inv_normal_d(1 - p / 2, mean, std_dev)
            else:
                raise TempError("test != [LEFT,RIGHT,CENTER]", f"INVALID TEST: {test} not DEFINED", "INV_NORM")

        except TempError as e:
            print('ERROR:', e.error, e.args[-1], e.temp, sep=': ')

    @staticmethod
    def inv_t(p, df, test="DEFAULT"):
        try:
            if test == "LEFT" or test == "DEFAULT":
                return Calculations.inv_t_d(p, df)
            elif test == "RIGHT":
                return Calculations.inv_t_d(1 - p, df)
            elif test == "CENTER":
                # p is alpha
                return Calculations.inv_t_d(p / 2, df), Calculations.inv_t_d(1 - p / 2, df)
            else:
                raise TempError("test != [LEFT,RIGHT,CENTER]", f"INVALID TEST: {test} not DEFINED", "INV_T")

        except TempError as e:
            print('ERROR:', e.error, e.args[-1], e.temp, sep=': ')

    @staticmethod
    def anova(data, dependent_variable, factor_variable):
        formula = dependent_variable + ' ~ ' + factor_variable
        model = ols(formula, data=data).fit()
        anova_table = sm.stats.anova_lm(model)
        return anova_table



