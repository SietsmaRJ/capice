from src.errors.errors import InputError


class CaddFeatures:
    def __init__(self):
        pass

    @staticmethod
    def supported_cadd_build_genome_builds():
        """
        Function to tell what CADD versions are supported for genome builds.
        :return: dict
        """
        return {37: [1.4]}

    @staticmethod
    def _cadd_feats(version):
        cadd_features = {1.4: ['Ref', 'Alt', 'Type',
                               'Length', 'GC', 'CpG', 'motifECount',
                               'motifEScoreChng', 'motifEHIPos',
                               'oAA', 'nAA', 'cDNApos', 'relcDNApos',
                               'CDSpos', 'relCDSpos',
                               'protPos', 'relProtPos', 'Domain',
                               'Dst2Splice',
                               'Dst2SplType', 'minDistTSS', 'minDistTSE',
                               'SIFTcat', 'SIFTval',
                               'PolyPhenCat', 'PolyPhenVal', 'priPhCons',
                               'mamPhCons', 'verPhCons', 'priPhyloP',
                               'mamPhyloP', 'verPhyloP',
                               'bStatistic', 'targetScan', 'mirSVR-Score',
                               'mirSVR-E', 'mirSVR-Aln', 'cHmmTssA',
                               'cHmmTssAFlnk', 'cHmmTxFlnk',
                               'cHmmTx', 'cHmmTxWk', 'cHmmEnhG',
                               'cHmmEnh', 'cHmmZnfRpts', 'cHmmHet',
                               'cHmmTssBiv', 'cHmmBivFlnk',
                               'cHmmEnhBiv', 'cHmmReprPC', 'cHmmReprPCWk',
                               'cHmmQuies', 'GerpRS', 'GerpRSpval', 'GerpN',
                               'GerpS', 'TFBS',
                               'TFBSPeaks', 'TFBSPeaksMax', 'tOverlapMotifs',
                               'motifDist', 'Segway', 'EncH3K27Ac',
                               'EncH3K4Me1', 'EncH3K4Me3',
                               'EncExp', 'EncNucleo', 'EncOCC',
                               'EncOCCombPVal',
                               'EncOCDNasePVal', 'EncOCFairePVal',
                               'EncOCpolIIPVal',
                               'EncOCctcfPVal', 'EncOCmycPVal',
                               'EncOCDNaseSig',
                               'EncOCFaireSig', 'EncOCpolIISig',
                               'EncOCctcfSig', 'EncOCmycSig',
                               'Grantham', 'Dist2Mutation', 'Freq100bp',
                               'Rare100bp', 'Sngl100bp', 'Freq1000bp',
                               'Rare1000bp', 'Sngl1000bp',
                               'Freq10000bp', 'Rare10000bp',
                               'Sngl10000bp', 'dbscSNV-ada_score',
                               'dbscSNV-rf_score']}
        return cadd_features[version]

    @staticmethod
    def _impute_values(version, genome_build):
        key = str(version) + '_' + str(genome_build)
        impute_values = {'1.4_37': {'Ref': 'N', 'Alt': 'N',
                                    'Consequence': 'UNKNOWN',
                                    'GC': 0.42,
                                    'CpG': 0.02, 'motifECount': 0,
                                    'motifEScoreChng': 0,
                                    'motifEHIPos': 0,
                                    'oAA': 'unknown',
                                    'nAA': 'unknown', 'cDNApos': 0,
                                    'relcDNApos': 0, 'CDSpos': 0,
                                    'relCDSpos': 0, 'protPos': 0,
                                    'relProtPos': 0,
                                    'Domain': 'UD',
                                    'Dst2Splice': 0,
                                    'Dst2SplType': 'unknown',
                                    'minDistTSS': 5.5,
                                    'minDistTSE': 5.5,
                                    'SIFTcat': 'UD', 'SIFTval': 0,
                                    'PolyPhenCat': 'unknown',
                                    'PolyPhenVal': 0,
                                    'priPhCons': 0.115,
                                    'mamPhCons': 0.079,
                                    'verPhCons': 0.094,
                                    'priPhyloP': -0.033,
                                    'mamPhyloP': -0.038,
                                    'verPhyloP': 0.017,
                                    'bStatistic': 800,
                                    'targetScan': 0,
                                    'mirSVR-Score': 0,
                                    'mirSVR-E': 0, 'mirSVR-Aln': 0,
                                    'cHmmTssA': 0.0667,
                                    'cHmmTssAFlnk': 0.0667,
                                    'cHmmTxFlnk': 0.0667,
                                    'cHmmTx': 0.0667,
                                    'cHmmTxWk': 0.0667,
                                    'cHmmEnhG': 0.0667,
                                    'cHmmEnh': 0.0667,
                                    'cHmmZnfRpts': 0.0667,
                                    'cHmmHet': 0.667,
                                    'cHmmTssBiv': 0.667,
                                    'cHmmBivFlnk': 0.0667,
                                    'cHmmEnhBiv': 0.0667,
                                    'cHmmReprPC': 0.0667,
                                    'cHmmReprPCWk': 0.0667,
                                    'cHmmQuies': 0.0667,
                                    'GerpRS': 0, 'GerpRSpval': 0,
                                    'GerpN': 1.91, 'GerpS': -0.2,
                                    'TFBS': 0, 'TFBSPeaks': 0,
                                    'TFBSPeaksMax': 0,
                                    'tOverlapMotifs': 0,
                                    'motifDist': 0,
                                    'Segway': 'unknown',
                                    'EncH3K27Ac': 0,
                                    'EncH3K4Me1': 0,
                                    'EncH3K4Me3': 0, 'EncExp': 0,
                                    'EncNucleo': 0, 'EncOCC': 5,
                                    'EncOCCombPVal': 0,
                                    'EncOCDNasePVal': 0,
                                    'EncOCFairePVal': 0,
                                    'EncOCpolIIPVal': 0,
                                    'EncOCctcfPVal': 0,
                                    'EncOCmycPVal': 0,
                                    'EncOCDNaseSig': 0,
                                    'EncOCFaireSig': 0,
                                    'EncOCpolIISig': 0,
                                    'EncOCctcfSig': 0,
                                    'EncOCmycSig': 0,
                                    'Grantham': 0,
                                    'Dist2Mutation': 0,
                                    'Freq100bp': 0, 'Rare100bp': 0,
                                    'Sngl100bp': 0,
                                    'Freq1000bp': 0,
                                    'Rare1000bp': 0,
                                    'Sngl1000bp': 0,
                                    'Freq10000bp': 0,
                                    'Rare10000bp': 0,
                                    'Sngl10000bp': 0,
                                    'dbscSNV-ada_score': 0,
                                    'dbscSNV-rf_score': 0}
                         }
        if key not in impute_values.keys():
            raise InputError('CADD version genome build '
                             'not found in impute values.')
        return impute_values[key]

    def get_cadd_features(self, cadd_build):
        """
        Function to get the list of CADD features of specified version.
        :return: list
        """
        return self._cadd_feats(cadd_build)

    def get_impute_values(self, cadd_build, genome_build):
        """
        Function to get all default CADD values to fill gaps.
        :return: dict
        """
        return self._impute_values(cadd_build, genome_build)