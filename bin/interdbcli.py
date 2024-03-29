#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
import interdbclient
from lib.helpers import (IDBCHelper, eprint_exception, eprint,
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
    subparser_inter_prog_infos = subparsers.add_parser("inter-prog-info", help="Utilities for work with Prog-Info interconnections", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_inter_prog_infos.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_inter_prog_infos.add_argument("--profile", type=str, help="Config profile")
    subparser_inter_prog_infos.add_argument("--id", type=str, help="Entity ID")
    subparser_inter_prog_infos.add_argument("--input-file", type=str, help="Input file")
    subparser_inter_prog_infos.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_inter_info_infos = subparsers.add_parser("inter-info-info", help="Utilities for work with Info-Info interconnections", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_inter_info_infos.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_inter_info_infos.add_argument("--profile", type=str, help="Config profile")
    subparser_inter_info_infos.add_argument("--id", type=str, help="Entity ID")
    subparser_inter_info_infos.add_argument("--input-file", type=str, help="Input file")
    subparser_inter_info_infos.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    return parent_parser.parse_args(sys.argv[1:])


class InfoInfsourceClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InfoInfsourcesApi)
        self.base_class = interdbclient.Infsource
        self.list_method = self.api_instance.info_infsources_list
        self.read_method = self.api_instance.info_infsources_read
        self.create_method = self.api_instance.info_infsources_create
        self.update_method = self.api_instance.info_infsources_update
        self.delete_method = self.api_instance.info_infsources_delete


class InfoInfsourceTagClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InfoInfsourcetagsApi)
        self.base_class = interdbclient.InfsourceTag
        self.list_method = self.api_instance.info_infsourcetags_list
        self.read_method = self.api_instance.info_infsourcetags_read
        self.create_method = self.api_instance.info_infsourcetags_create
        self.update_method = self.api_instance.info_infsourcetags_update
        self.delete_method = self.api_instance.info_infsourcetags_delete


class InfoEditionClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InfoEditionsApi)
        self.base_class = interdbclient.InfoEdition
        self.list_method = self.api_instance.info_editions_list
        self.read_method = self.api_instance.info_editions_read
        self.create_method = self.api_instance.info_editions_create
        self.update_method = self.api_instance.info_editions_update
        self.delete_method = self.api_instance.info_editions_delete


class InfoResourceClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InfoResourcesApi)
        self.base_class = interdbclient.InfoResource
        self.list_method = self.api_instance.info_resources_list
        self.read_method = self.api_instance.info_resources_read
        self.create_method = self.api_instance.info_resources_create
        self.update_method = self.api_instance.info_resources_update
        self.delete_method = self.api_instance.info_resources_delete


class ProgPackageClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.ProgPackagesApi)
        self.base_class = interdbclient.Infsource
        self.list_method = self.api_instance.prog_packages_list
        self.read_method = self.api_instance.prog_packages_read
        self.create_method = self.api_instance.prog_packages_create
        self.update_method = self.api_instance.prog_packages_update
        self.delete_method = self.api_instance.prog_packages_delete


class ProgPackageTagClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.ProgPackagetagsApi)
        self.base_class = interdbclient.InfsourceTag
        self.list_method = self.api_instance.prog_packagetags_list
        self.read_method = self.api_instance.prog_packagetags_read
        self.create_method = self.api_instance.prog_packagetags_create
        self.update_method = self.api_instance.prog_packagetags_update
        self.delete_method = self.api_instance.prog_packagetags_delete


class ProgEditionClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.ProgEditionsApi)
        self.base_class = interdbclient.InfoEdition
        self.list_method = self.api_instance.prog_editions_list
        self.read_method = self.api_instance.prog_editions_read
        self.create_method = self.api_instance.prog_editions_create
        self.update_method = self.api_instance.prog_editions_update
        self.delete_method = self.api_instance.prog_editions_delete


class ProgResourceClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.ProgResourcesApi)
        self.base_class = interdbclient.InfoResource
        self.list_method = self.api_instance.prog_resources_list
        self.read_method = self.api_instance.prog_resources_read
        self.create_method = self.api_instance.prog_resources_create
        self.update_method = self.api_instance.prog_resources_update
        self.delete_method = self.api_instance.prog_resources_delete


class InterProgInfoClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InterProginfosApi)
        self.base_class = interdbclient.ProgInfo
        self.list_method = self.api_instance.inter_proginfos_list
        self.read_method = self.api_instance.inter_proginfos_read
        self.create_method = self.api_instance.inter_proginfos_create
        self.update_method = self.api_instance.inter_proginfos_update
        self.delete_method = self.api_instance.inter_proginfos_delete


class InterInfoInfoClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(interdbclient.InterInfoinfosApi)
        self.base_class = interdbclient.InfoInfo
        self.list_method = self.api_instance.inter_infoinfos_list
        self.read_method = self.api_instance.inter_infoinfos_read
        self.create_method = self.api_instance.inter_infoinfos_create
        self.update_method = self.api_instance.inter_infoinfos_update
        self.delete_method = self.api_instance.inter_infoinfos_delete


def main():
    args = parse_args(sys.argv)
    obj = None
    action_process_result = True
    try:
        ICB = None
        if args.group == "info-infsource":
            ICB = InfoInfsourceClientBase(args)
        elif args.group == "info-infsource-tag":
            ICB = InfoInfsourceTagClientBase(args)
        elif args.group == "info-edition":
            ICB = InfoEditionClientBase(args)
        elif args.group == "info-resource":
            ICB = InfoResourceClientBase(args)
        elif args.group == "prog-package":
            ICB = ProgPackageClientBase(args)
        elif args.group == "prog-package-tag":
            ICB = ProgPackageTagClientBase(args)
        elif args.group == "prog-edition":
            ICB = ProgEditionClientBase(args)
        elif args.group == "prog-resource":
            ICB = ProgResourceClientBase(args)
        elif args.group == "inter-prog-info":
            ICB = InterProgInfoClientBase(args)
        elif args.group == "inter-info-info":
            ICB = InterInfoInfoClientBase(args)
        else:
            eprint("Not implemented for group: {}".format(args.group))
            exit(1)
        action_process_result, obj = typical_actions_process(ICB)
    except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
        eprint_exception(e, print_traceback=print_traceback)
    if action_process_result == False:
        eprint("Not implemented for action: {}".format(args.action))
        exit(1)
    if print_result and obj is not None:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()