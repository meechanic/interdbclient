#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
from interdbclient.helpers import (IDBCHelper, eprint_exception, eprint,
                                   InfoInfsourceClientBase, InfoInfsourceTagClientBase, InfoResourceClientBase, InfoEditionClientBase,
                                   ProgPackageClientBase, ProgPackageTagClientBase, ProgResourceClientBase, ProgEditionClientBase,
                                   InterProgInfoClientBase,
                                   typical_actions_process)
from interdbclient.rest import ApiException

yaml.Dumper.ignore_aliases = lambda *args : True
print_traceback = True
print_result = True


def parse_args(argv):
    self_name = os.path.basename(argv[0])
    epilog = '''\
available item-level cmds for bulk actions:
  c    create item
  u    update item
  d    delete item
  n    do nothing'''
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for the interdb database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    # info
    subparser_info_infsources = subparsers.add_parser("info-infsource", help="Utilities for work with Info Infsources", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_info_infsources.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_info_infsources.add_argument("--profile", type=str, help="Config profile")
    subparser_info_infsources.add_argument("--id", type=str, help="Entity ID")
    subparser_info_infsources.add_argument("--input-file", type=str, help="Input file")
    subparser_info_infsources.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_info_infsource_tags = subparsers.add_parser("info-infsource-tag", help="Utilities for work with Info InfsourceTags", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_info_infsource_tags.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_info_infsource_tags.add_argument("--profile", type=str, help="Config profile")
    subparser_info_infsource_tags.add_argument("--id", type=str, help="Entity ID")
    subparser_info_infsource_tags.add_argument("--input-file", type=str, help="Input file")
    subparser_info_infsource_tags.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_info_editions = subparsers.add_parser("info-edition", help="Utilities for work with Info Editions", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_info_editions.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_info_editions.add_argument("--profile", type=str, help="Config profile")
    subparser_info_editions.add_argument("--id", type=str, help="Entity ID")
    subparser_info_editions.add_argument("--input-file", type=str, help="Input file")
    subparser_info_editions.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_info_resources = subparsers.add_parser("info-resource", help="Utilities for work with Info Resources", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_info_resources.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_info_resources.add_argument("--profile", type=str, help="Config profile")
    subparser_info_resources.add_argument("--id", type=str, help="Entity ID")
    subparser_info_resources.add_argument("--input-file", type=str, help="Input file")
    subparser_info_resources.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    # prog
    subparser_prog_packages = subparsers.add_parser("prog-package", help="Utilities for work with Prog Packages", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_prog_packages.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_prog_packages.add_argument("--profile", type=str, help="Config profile")
    subparser_prog_packages.add_argument("--id", type=str, help="Entity ID")
    subparser_prog_packages.add_argument("--input-file", type=str, help="Input file")
    subparser_prog_packages.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_prog_package_tags = subparsers.add_parser("prog-package-tag", help="Utilities for work with Prog PackageTags", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_prog_package_tags.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_prog_package_tags.add_argument("--profile", type=str, help="Config profile")
    subparser_prog_package_tags.add_argument("--id", type=str, help="Entity ID")
    subparser_prog_package_tags.add_argument("--input-file", type=str, help="Input file")
    subparser_prog_package_tags.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_prog_editions = subparsers.add_parser("prog-edition", help="Utilities for work with Prog Editions", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_prog_editions.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_prog_editions.add_argument("--profile", type=str, help="Config profile")
    subparser_prog_editions.add_argument("--id", type=str, help="Entity ID")
    subparser_prog_editions.add_argument("--input-file", type=str, help="Input file")
    subparser_prog_editions.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_prog_resources = subparsers.add_parser("prog-resource", help="Utilities for work with Prog Resources", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_prog_resources.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_prog_resources.add_argument("--profile", type=str, help="Config profile")
    subparser_prog_resources.add_argument("--id", type=str, help="Entity ID")
    subparser_prog_resources.add_argument("--input-file", type=str, help="Input file")
    subparser_prog_resources.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    # inter
    subparser_inter_prog_infos = subparsers.add_parser("inter-prog-info", help="Utilities for work with Prog Resources", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_inter_prog_infos.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_inter_prog_infos.add_argument("--profile", type=str, help="Config profile")
    subparser_inter_prog_infos.add_argument("--id", type=str, help="Entity ID")
    subparser_inter_prog_infos.add_argument("--input-file", type=str, help="Input file")
    subparser_inter_prog_infos.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    obj = None
    if args.group == "info-infsource":
        action_process_result = False
        try:
            ICB = InfoInfsourceClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "info-infsource-tag":
        action_process_result = False
        try:
            ICB = InfoInfsourceTagClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "info-edition":
        action_process_result = False
        try:
            ICB = InfoEditionClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "info-resource":
        action_process_result = False
        try:
            ICB = InfoResourceClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "prog-package":
        action_process_result = False
        try:
            ICB = ProgPackageClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "prog-package-tag":
        action_process_result = False
        try:
            ICB = ProgPackageTagClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "prog-edition":
        action_process_result = False
        try:
            ICB = ProgEditionClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "prog-resource":
        action_process_result = False
        try:
            ICB = ProgResourceClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "inter-prog-info":
        action_process_result = False
        try:
            ICB = InterProgInfoClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    else:
        eprint("Not implemented for group: {}".format(args.group))
        exit(1)
    if print_result and obj is not None:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()