'''Copy and paste this definition into your notebook. Run it as follows:
return_all_suicides('United States', nameofyourdataframe)
to get breakdown by year of suicides in US stored in dataframe named 'nameofyourdataframe'. 
NOTE: It's case sensitive.'''

def return_all_suicides(country, dataf):
    country_df = dataf[dataf['country']==str(country)]
    country_group = country_df.groupby('year')['suicides_no'].sum()
    print (country_group)
