#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
from infodbclient.helpers import (IDBCHelper, eprint_exception, eprint, InfsourceClientBase, InfsourceTagClientBase,
                                  ResourceClientBase, EditionClientBase, typical_actions_process)
from infodbclient.rest import ApiException

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
                                            description="Client for information sources database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    subparser_packages = subparsers.add_parser("infsources", help="Utilities for work with Infsources", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_packages.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_packages.add_argument("--profile", type=str, help="Config profile")
    subparser_packages.add_argument("--id", type=str, help="Entity ID")
    subparser_packages.add_argument("--input-file", type=str, help="Input file")
    subparser_packages.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_packages = subparsers.add_parser("infsource-tags", help="Utilities for work with InfsourceTags", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_packages.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_packages.add_argument("--profile", type=str, help="Config profile")
    subparser_packages.add_argument("--id", type=str, help="Entity ID")
    subparser_packages.add_argument("--input-file", type=str, help="Input file")
    subparser_packages.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_replicas = subparsers.add_parser("editions", help="Utilities for work with Replicas", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_replicas.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_replicas.add_argument("--profile", type=str, help="Config profile")
    subparser_replicas.add_argument("--id", type=str, help="Entity ID")
    subparser_replicas.add_argument("--input-file", type=str, help="Input file")
    subparser_replicas.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_modules = subparsers.add_parser("resources", help="Utilities for work with Modules", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_modules.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_modules.add_argument("--profile", type=str, help="Config profile")
    subparser_modules.add_argument("--id", type=str, help="Entity ID")
    subparser_modules.add_argument("--input-file", type=str, help="Input file")
    subparser_modules.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    idbch = IDBCHelper(args)
    obj = None
    if args.group == "infsources":
        action_process_result = False
        try:
            ICB = InfsourceClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "infsource-tags":
        action_process_result = False
        try:
            ICB = InfsourceTagClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "editions":
        action_process_result = False
        try:
            ICB = EditionClientBase(args)
            action_process_result, obj = typical_actions_process(ICB)
        except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
            eprint_exception(e, print_traceback=print_traceback)
        if action_process_result == False:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "resources":
        action_process_result = False
        try:
            ICB = ResourceClientBase(args)
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