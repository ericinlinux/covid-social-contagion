
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
    'mean [opinion] of people': 'opinion_avg'
}

f_results = './results/20200428/'


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



# OTHER FUNCTIONS
def get_scenarios_step (df):
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

def get_immune_infected(df, population="10k", values="perc"):
    """Returns the percentage of people immune and infected at each given time step
    """
    if population == "10k":
        pop = 10000
    else:
        pop = 180000

    if values == "perc":
        return df.groupby(['step']).mean()[['immune_people_num', 'infected_people_num']]*100/pop
    else:
        return df.groupby(['step']).mean()[['immune_people_num', 'infected_people_num']]
        


def get_data_per_population(df, scenario="no_interv", values="perc"):
    """
    Get the whole DF with the data divided by the population
    """
    if scenario == "no_interv":
        if values == "perc":
            return df.groupby(['step']).mean()[['infected_people_num', 
                                                'symptomatic_people_num', 
                                                'hospitilized_people_num', 
                                                'icu_people_num', 
                                                'immune_people_num', 
                                                'deaths_favela', 
                                                'deaths_non_favela', 
                                                'death_by_virus', 
                                                'death_by_no_icus_private',
                                                'death_by_no_icus_public']]*100/global_nointerv_10k['population']
        else:
            return df.groupby(['step']).mean()[['infected_people_num', 
                                                'symptomatic_people_num', 
                                                'hospitilized_people_num', 
                                                'icu_people_num', 
                                                'immune_people_num', 
                                                'deaths_favela', 
                                                'deaths_non_favela', 
                                                'death_by_virus', 
                                                'death_by_no_icus_private',
                                                'death_by_no_icus_public']]/global_nointerv_10k['population']


def get_data_per_infected_population(df, scenario="no_interv", values="perc"):
    """
    Get the whole DF with the data divided by the population
    """
    if scenario == "no_interv":
        if values == "perc":
            return df.groupby(['step']).mean()[['infected_people_num', 
                                                'symptomatic_people_num', 
                                                'hospitilized_people_num', 
                                                'icu_people_num', 
                                                'immune_people_num', 
                                                'deaths_favela', 
                                                'deaths_non_favela', 
                                                'death_by_virus', 
                                                'death_by_no_icus_private',
                                                'death_by_no_icus_public']]*100/global_nointerv_10k['population']
        else:
            return df.groupby(['step']).mean()[['infected_people_num', 
                                                'symptomatic_people_num', 
                                                'hospitilized_people_num', 
                                                'icu_people_num', 
                                                'immune_people_num', 
                                                'deaths_favela', 
                                                'deaths_non_favela', 
                                                'death_by_virus', 
                                                'death_by_no_icus_private',
                                                'death_by_no_icus_public']]/global_nointerv_10k['population']


def get_deaths_by_group(df, scenario="no_interv", debug=False):
    """
    Return the rate of deaths in each group (favela and non favela) as a DF
    """
    if scenario == "no_interv":
        final_scenario_df = get_final_step(df)
        death_df = final_scenario_df[['deaths_favela', 
                                      'deaths_non_favela', 
                                      'death_by_virus',
                                      'death_by_no_icus_private', 
                                      'death_by_no_icus_public'
                                     ]]
        population_favela = global_nointerv_10k['population'] * global_nointerv_10k['favelas_perc_population']/100
        population_nonfavela = global_nointerv_10k['population'] - population_favela
        if debug:
            print(population_favela, population_nonfavela)

        df_perc = pd.DataFrame()
        df_perc['deaths_favela'] = death_df['deaths_favela']*100/population_favela
        df_perc['deaths_non_favela'] = death_df['deaths_non_favela']*100/population_nonfavela

        return df_perc.reset_index()


def get_deaths_in_hospital(df, scenario="no_interv"):
    """
    Return the number of deaths in the hospital
    """
    if scenario == "no_interv":
        final_scenario_df = get_final_step(df)
        hospital_deaths = final_scenario_df[['death_by_virus', 
                                             'death_by_no_icus_private', 
                                             'death_by_no_icus_public'
                                             ]].copy()
        hospital_deaths['total'] = hospital_deaths.sum(axis=1)

    return hospital_deaths

def get_mortality_rates(df, scenario="no_interv"):
    """
    """
    mort_df = pd.DataFrame()

    if scenario == "no_interv":
        f_df = get_final_step(df)
        # Total people infected in the end = infected + immune + dead people
        mort_df['total_infected'] = f_df.infected_people_num + f_df.immune_people_num + \
                                    f_df.deaths_favela + f_df.deaths_non_favela
        # Total deaths
        mort_df['total_deaths'] =   f_df.deaths_favela + f_df.deaths_non_favela
        # Mortality = total deaths / total infected
        mort_df['mortality'] = mort_df.total_deaths*100/mort_df.total_infected
        # Mortality unavoidable = dead by the virus / total infected
        mort_df['mortality_unavoidable'] = f_df.death_by_virus*100/mort_df.total_infected
        # Mortality for lack of ICUs (private)
        mort_df['mortality_no_icus_private'] = f_df.death_by_no_icus_private*100/mort_df.total_infected
        # Mortality for lack of ICUs (public)
        mort_df['mortality_no_icus_public'] = f_df.death_by_no_icus_public*100/mort_df.total_infected

    return mort_df


