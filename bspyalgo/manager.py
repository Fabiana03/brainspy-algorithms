# -*- coding: utf-8 -*-
"""Contains the platforms used in all SkyNEt experiments to be optimized by Genetic Algo.

The classes in Platform must have a method self.evaluate() which takes as arguments
the inputs inputs_wfm, the gene pool and the targets target_wfm. It must return
outputs as numpy array of shape (len(pool), inputs_wfm.shape[-1]).

Created on Wed Aug 21 11:34:14 2019

@author: HCRuiz
"""
# import logging
# from bspyalgo.algorithms.genetic.ga import GA
# from bspyalgo.algorithms.gradient.gd import GD
#from bspyalgo.utils.io import load_configs
from bspyalgo.algorithms.gradient.core.losses import choose_loss_function
from bspyalgo.algorithms.genetic.core.fitness import choose_fitness_function
from bspyalgo.algorithms.gradient.core.optim import get_optimizer as get_gd_optimizer
from bspyalgo.algorithms.genetic.core.optim import get_optimizer as get_ga_optimizer
from bspyalgo.algorithms.gradient.fitter import train as gd
from bspyalgo.algorithms.genetic.fitter import train as ga
# TODO: Add chip platform
# TODO: Add simulation platform
# TODO: Target wave form as argument can be left out if output dimension is known internally


# def get_algorithm(configs, is_main=False):
#     if(isinstance(configs, str)):       # Enable to load configs as a path to configurations or as a dictionary
#         configs = load_configs(configs)

#     if configs['algorithm'] == 'genetic':
#         return GA(configs, is_main=is_main)
#     elif configs['algorithm'] == 'gradient_descent':
#         return get_gd(configs, is_main=is_main)
#     else:
#         raise NotImplementedError(f"Algorithm {configs['algorithm']} is not recognised. Please try again with 'genetic' or 'gradient_descent'")


# def get_gd(configs, is_main=False):
#     if configs['processor']['platform'] == 'hardware':
#         raise NotImplementedError('Hardware platform not implemented')
#         # TODO: Implement the lock in algorithm class
#     elif configs['processor']['platform'] == 'simulation':
#         return GD(configs, is_main=is_main)
#     else:
#         raise NotImplementedError('Platform not implemented')


def get_criterion(configs):
    if configs['type'] == 'gradient':
        return choose_loss_function(configs['criterion'])
    elif configs['type'] == 'genetic':
        return choose_fitness_function(configs['criterion'])
    else:
        assert False, 'Unrecognised algorithm field in configs. It must have the value gradient or the value genetic.'


def get_optimizer(parameters, configs):
    if configs['type'] == 'gradient':
        return get_gd_optimizer(parameters, configs)
    elif configs['type'] == 'genetic':
        return get_ga_optimizer(parameters, configs)
    else:
        assert False, 'Unrecognised algorithm field in configs. It must have the value gradient or the value genetic.'


def get_algorithm(configs):
    if configs['type'] == 'gradient':
        return gd
    elif configs['type'] == 'genetic':
        return ga
    else:
        assert False, 'Unrecognised algorithm field in configs. It must have the value gradient or the value genetic.'