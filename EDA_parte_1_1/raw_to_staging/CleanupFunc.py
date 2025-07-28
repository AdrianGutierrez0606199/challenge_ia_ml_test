import pandas as pd
import numpy as np

PHANTOM_NULLS = ['-','','<na>','nA','nan','null','_','vacio', 'NaN']

## define functions for cleaning up the table.
class CleanUp:

    def __init__(self,df):
        self.df = df

    def remove_lead_spaces(self):
        '''Limpia espacios en blanco antes y al final del texto de cada columnas.'''
        for col in self.df:
            if self.df[col].dtype in ['object','str']:
                self.df[col] = self.df[col].str.strip()

    def replace_phantom_nulls(self):
        for col in self.df:
            before = self.df[col].isna().sum()
            self.df[col] = self.df[col].apply(lambda x: pd.NA if pd.isna(x) or x.lower() in PHANTOM_NULLS else x)
            after = self.df[col].isna().sum()
            if before != after:
                print(after, 'phantom nulls replaced in:', col)
        return self.df

    def convert_lower_case(self):
        '''Convierte todas las columnas que no son numericas a minúsculas '''
        for col in self.df:
            if str(self.df[col].dtype) not in ["int", "float","int64","float64"]:
                self.df[col] = self.df[col].apply(lambda x: pd.NA if pd.isna(x) else x.lower())

    def convert_str_to_float(self, cols):
        '''Convierte una lista de campos de str a floats'''
        for col in cols:
            self.df[col] = self.df[col].apply(lambda x: np.nan if pd.isna(x) or x.lower() in PHANTOM_NULLS else float(x.replace(',', '.'))).astype('Float64')

    def convert_str_to_int(self, cols):
        '''Convierte una lista de campos de str a floats'''
        for col in cols:
            self.df[col] = self.df[col].apply(lambda x: np.nan if pd.isna(x) or x.lower() in PHANTOM_NULLS else float(x.replace(',', '.'))).astype('Int64')

    def convert_float_to_int(self, cols):
        '''Convierte una lista de campos de str a floats'''
        for col in cols:
            self.df[col] = self.df[col].astype('Int64')

    def convert_date_cols(self, cols):
        for date_col in cols:
            self.df[date_col] = pd.to_datetime(self.df[date_col], dayfirst=True)

    def rename_cols(self, cols, prefix = '', mode = 'INCLUDE'):
        if mode.lower() not in ['include', 'i']:
            cols = set(self.df.columns) - set(cols)
        renamed_cols = [prefix+'_'+col for col in cols]
        self.df = self.df.rename(columns=dict(zip(cols, renamed_cols)))
        return self.df