from src.command_line_supporter import ArgumentSupporter
from src.input_checker import InputChecker, LogChecker
from src.utilities.utilities import convert_cla_to_str, convert_cla_to_int,\
    convert_cla_to_float, convert_cla_to_full_string
from src.global_manager import CapiceManager
from src.main import Main

__program__ = 'CAPICE'
__author__ = 'Shuang Li, Robert Sietsma and Molgenis'
__license__ = 'LGPL-3.0'
__version__ = 2.0
__description__ = "{} (version: {}) is a program developed and maintained by {}. " \
                  "The program facilitates a pathogenicity prediction for a CADD annotated VCF file. " \
                  "This program is developed under the {} license and is provided 'as-is' without any warranty " \
                  "or indemnification of any kind.".format(__program__, __version__, __author__, __license__)


def main():
    cla = ArgumentSupporter(description=__description__)

    # Getting all arguments.

    input_loc = convert_cla_to_str(cla.get_argument('input'))
    output_loc = convert_cla_to_str(cla.get_argument('output'))
    log_loc = convert_cla_to_str(cla.get_argument('log_file'))
    genome_build = convert_cla_to_int(cla.get_argument('genome_build'))
    cadd_build = convert_cla_to_float(cla.get_argument('cadd_build'))
    verbose = cla.get_argument('verbose')
    force = cla.get_argument('force')
    overwrite_impute = convert_cla_to_full_string(cla.get_argument('overwrite_impute_file'))
    overwrite_model = convert_cla_to_full_string(cla.get_argument('overwrite_model_file'))

    # Checking the log arguments

    lc = LogChecker(log_loc=log_loc, output_loc=output_loc, verbose=verbose)
    log_loc = lc.check_log_loc()

    # Initializing the manager

    manager = CapiceManager()
    manager.set_now()
    manager.set_log_loc(log_loc=log_loc)
    manager.set_verbose(verbose=verbose)
    manager.set_overwrite_impute(overwrite_impute)
    manager.set_overwrite_model(overwrite_model)

    # Checking the input arguments.

    input_checker = InputChecker()

    input_checker.check_arguments(input_loc=input_loc, output_loc=output_loc)

    capice_main = Main(__program__=__program__,
                       __author__=__author__,
                       __version__=__version__,
                       input_loc=input_loc,
                       output_loc=output_loc,
                       genome_build=genome_build,
                       cadd_build=cadd_build,
                       force=force,
                       verbose=verbose)
    capice_main.run()


if __name__ == '__main__':
    main()
