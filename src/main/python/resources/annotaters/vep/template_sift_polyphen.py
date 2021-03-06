from src.main.python.resources.annotaters.vep.template import Template
import pandas as pd


class TemplateSiftPolyPhen(Template):
    def __init__(self, name='Template', usable=False):
        super(TemplateSiftPolyPhen, self).__init__(
            name=name,
            usable=usable
        )

    @property
    def columns(self):
        return [None, None]

    @property
    def val_col(self):
        return self.columns[1]

    def process(self, dataframe: pd.DataFrame):
        dataframe[self.columns] = dataframe[self.name].str.split(
            '(',
            expand=True
        )
        dataframe[self.val_col] = dataframe[self.val_col].str.split(
            ')',
            expand=True
        )[0]
        dataframe[self.val_col] = dataframe[self.val_col].astype(float)
        return dataframe
