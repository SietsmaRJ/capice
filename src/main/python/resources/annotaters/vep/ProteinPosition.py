from src.main.python.resources.annotaters.vep.template_position import \
    TemplatePosition


class ProteinPosition(TemplatePosition):
    def __init__(self):
        super(ProteinPosition, self).__init__(
            name='Protein_position',
            usable=True
        )

    @property
    def columns(self):
        return ['protPos', 'relProtPos']
