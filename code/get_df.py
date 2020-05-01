
"""
Programmer: Eric Araujo
Last changes: 2020-04-30

Code for the opinion contagion model paper entitled "Disconnecting for the good: A network-oriented model for social contagion of opinions and social network interventions to increase adherence to social distancing"

These functions are used in the notebook Results_Notebook.ipynb
"""

import pandas as pd


column_change_names = {
    '[run number]': 'run', 
    'beta-gov': 'beta', 
    'sigma': 'sigma', 
    'pop-size': 'population', 
    #'layout-type',
    #'graphics?', 
    #'test?', 
    #'debug?', 
    'nw-type': 'nw_topology', 
    '[step]': 'step',
    'count people with [lockdown?]': 'num_lockdown', 
    'count people with [not lockdown?]': 'num_not_lockdown',
    'mean [opinion] of people': 'opinion_avg',
    'standard-deviation [opinion] of people': 'opinion_std',
    'intervention-type': 'interv_type'
}

f_results = './results/20200429/'


# GET DATA

def get_results_df(csv_f='basic_100_people_end_table.csv'):
    """
    Get the DataFrame of the Simulations for 10k people and No Interventions
    """
    results_df = pd.read_csv(f_results + csv_f, skiprows=6)
    results_df.rename(columns=column_change_names, inplace=True)
    drop_list = ['layout-type', 'graphics?', 'test?', 'debug?' ]
    results_df.drop(columns=drop_list, inplace=True)

    return results_df


def get_interventions_df(csv_f='interv_100_people_end_table.csv'):
    """
    Get the DataFrame of the Simulations for 10k people and No Interventions
    """
    df = pd.read_csv(f_results + csv_f, skiprows=6)
    df.rename(columns=column_change_names, inplace=True)
    drop_list = ['layout-type', 'graphics?', 'test?', 'debug?', 'intervention?' ]
    df.drop(columns=drop_list, inplace=True)

    return df


# OTHER FUNCTIONS
def get_scenarios_step (df):
    """
    Get the DataFrame of the results for all betas and sigmas creating one column for each combination
    """
    beta_list = [0.1, 0.3, 0.5, 0.7, 0.9]
    sigma_list = [1, 5, 10]
    
    f_df = pd.DataFrame()
    
    for beta, sigma in [(x,y) for x in beta_list for y in sigma_list]:
        f_df['({},{})'.format(beta,sigma)] = pd.Series(list(df[(df.beta == beta) & (df.sigma == sigma)].step))
    
    return f_df


def get_opinions (df):
    beta_list = [0.1, 0.3, 0.5, 0.7, 0.9]
    sigma_list = [1, 5, 10]
    
    f_df = pd.DataFrame()
    
    for beta, sigma in [(x,y) for x in beta_list for y in sigma_list]:
        f_df['({},{})'.format(beta,sigma)] = pd.Series(list(df[(df.beta == beta) & (df.sigma == sigma)].opinion_avg))

    return f_df

def get_perc_lockdown (df):
    beta_list = [0.1, 0.3, 0.5, 0.7, 0.9]
    sigma_list = [1, 5, 10]
    
    f_df = pd.DataFrame()
    
    for beta, sigma in [(x,y) for x in beta_list for y in sigma_list]:
        f_df['({},{})'.format(beta,sigma)] = pd.Series(list(df[(df.beta == beta) & (df.sigma == sigma)].num_lockdown))

    return f_df


