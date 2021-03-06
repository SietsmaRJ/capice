import pandas as pd
from src.main.python.resources.annotaters.vep.template import Template


class MotifEScoreChange(Template):
    def __init__(self):
        super(MotifEScoreChange, self).__init__(
            name='MOTIF_SCORE_CHANGE',
            usable=True
        )

    def process(self, dataset: pd.DataFrame):
        dataset['motifEScoreChng'] = dataset[self.name]
        return dataset
