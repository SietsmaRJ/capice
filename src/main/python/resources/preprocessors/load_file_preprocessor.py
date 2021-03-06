import pandas as pd
from src.main.python.core.logger import Logger


class LoadFilePreProcessor:
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.log = Logger().logger

    def process(self):
        """
        Function to start the LoadFilePreProcessor to correct the input file of
        each column starting with % and the renaming of certain columns,
        like #CHROM to Chr.

        Returns
        -------
        dataset :   pandas.DataFrame
                    Processed dataset with corrected % sign and renamed columns.
        """
        self.log.debug('Starting correcting % sign.')
        self._correct_percentage_sign()
        self.log.debug('% sign corrected, starting renaming of columns.')
        self._col_renamer()
        self.dataset['Chr'] = self.dataset['Chr'].astype(str)
        self.log.info('LoadFilePreProcessor successful.')
        return self.dataset

    def _correct_percentage_sign(self):
        new_columns = []
        for column in self.dataset.columns:
            if column.startswith('%'):
                new_columns.append(column.split('%')[1])
            elif column.startswith('#'):
                new_columns.append(column.split('#')[1])
            else:
                new_columns.append(column)
        self.dataset.columns = new_columns

    def _col_renamer(self):
        """
        Function to rename "Gene, Feature, SYMBOL, INTRON and EXON" to
        "GeneID, FeatureID, GeneName, Intron and Exon".
        """
        self.dataset.rename(
            columns={
                'CHROM': 'Chr',
                'POS': 'Pos',
                'REF': 'Ref',
                'ALT': 'Alt',
                'SYMBOL_SOURCE': 'SourceID',
                'Feature': 'FeatureID',
                'SYMBOL': 'GeneName',
                'INTRON': 'Intron',
                'EXON': 'Exon'
            }, inplace=True
        )
