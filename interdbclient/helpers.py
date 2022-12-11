import sys
from pathlib import Path
import yaml
import traceback
import interdbclient


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def eprint_exception(e, print_traceback=True, need_exit=True):
    eprint(e)
    if print_traceback:
        eprint(traceback.format_exc())
    if need_exit:
        exit(1)


class IDBCHelper:

    def __init__(self, args):
        self.args = args
        conf_file = "{}/.config/interdbclient/config.yaml".format(str(Path.home()))
        self.conf_file_object = {"profiles": {"main": {"print_traceback": True}}, "current": "main"}
        try:
            with open(conf_file, "r") as f:
                self.conf_file_object = yaml.safe_load(f)
        except Exception as e:
            pass
        if self.args.profile:
            self.conf_file_object["current"] = self.args.profile

    def get_all_confs(self):
        return self.conf_file_object

    def get_args(self):
        return self.args

    def get_current_profile(self):
        return self.conf_file_object.get("current", "main")

    def get_current_confs(self):
        return self.get_all_confs().get("profiles", {}).get(self.get_current_profile(), {})

    def get_current_conf_value(self, conf_param_name):
        return self.get_current_confs().get(conf_param_name, None)

    def get_current_conf_url(self):
        return "{}://{}:{}{}".format(self.get_current_conf_value("scheme"),
                                     self.get_current_conf_value("host"),
                                     self.get_current_conf_value("port"),
                                     self.get_current_conf_value("path"))

    def get_info_infsources_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))

    def get_info_infsourcetags_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.InfoInfsourcetagsApi(interdbclient.ApiClient(configuration))

    def get_info_editions_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))

    def get_info_resources_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))

    def get_prog_packages_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))

    def get_prog_packagetags_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))

    def get_prog_editions_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))

    def get_prog_resources_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))

    def get_inter_proginfos_api_instance(self):
        configuration = interdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))


class InfoInfsourceClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = IDBCHelper(self.args)
        self.api_instance = self.helper.get_info_infsources_api_instance()
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
        self.api_instance = self.helper.get_info_infsourcetags_api_instance()
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
        self.api_instance = self.helper.get_info_editions_api_instance()
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
        self.api_instance = self.helper.get_info_resources_api_instance()
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
        self.api_instance = self.helper.get_prog_packages_api_instance()
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
        self.api_instance = self.helper.get_prog_packagetags_api_instance()
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
        self.api_instance = self.helper.get_prog_editions_api_instance()
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
        self.api_instance = self.helper.get_prog_resources_api_instance()
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
        self.api_instance = self.helper.get_inter_proginfos_api_instance()
        self.base_class = interdbclient.InfoResource
        self.list_method = self.api_instance.inter_proginfos_list
        self.read_method = self.api_instance.inter_proginfos_read
        self.create_method = self.api_instance.inter_proginfos_create
        self.update_method = self.api_instance.inter_proginfos_update
        self.delete_method = self.api_instance.inter_proginfos_delete


def typical_actions_process(CB):
    possible_cmds = ["c", "u", "d", "n"]
    allowed_keys = list(CB.base_class.attribute_map.keys())
    action_process_result = False
    obj = None
    while "id" in allowed_keys:
        allowed_keys.remove("id")
    if CB.args.action == "list" or CB.args.action is None:
        res = CB.list_method()
        if res:
            obj = [i.to_dict() for i in res]
        action_process_result = True
    elif CB.args.action == "get":
        id = int(CB.args.id)
        obj = CB.read_method(id).to_dict()
        action_process_result = True
    elif CB.args.action == "create":
        if not CB.args.input_file:
            eprint("Missing input file")
            return action_process_result, obj
        with open(CB.args.input_file, "r") as f:
            res_pre = yaml.safe_load(f)
        res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
        data = CB.base_class(**res)
        obj = CB.create_method(data).to_dict()
        action_process_result = True
    elif CB.args.action == "update":
        if not CB.args.input_file:
            eprint("Missing input file")
            return action_process_result, obj
        id = int(CB.args.id)
        with open(CB.args.input_file, "r") as f:
            res_pre = yaml.safe_load(f)
        res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
        data = CB.base_class(**res)
        obj = CB.update_method(id, data).to_dict()
        action_process_result = True
    elif CB.args.action == "delete":
        id = int(CB.args.id)
        CB.delete_method(id)
        action_process_result = True
    elif CB.args.action == "bulk-dump":
        default_cmd = ""
        if CB.args.default_cmd not in possible_cmds + [None]:
            eprint("Unknown default cmd: {}, use one of the following {}".format(CB.args.default_cmd,
                                                                                 ", ".join(possible_cmds)))
            return action_process_result, obj
        if CB.args.default_cmd is not None:
            default_cmd = CB.args.default_cmd
        res = CB.list_method()
        if res:
            obj = []
            for i in res:
                new_item = i.to_dict()
                new_item.update({"cmd": default_cmd})
                obj.append(new_item)
        action_process_result = True
    elif CB.args.action == "bulk-upload":
        if not CB.args.input_file:
            eprint("Missing input file")
            return action_process_result, obj
        default_cmd = ""
        if CB.args.default_cmd not in possible_cmds + [None]:
            eprint("Unknown default cmd: {}, use one of the following {}".format(CB. args.default_cmd,
                                                                                 ", ".join(possible_cmds)))
            return action_process_result, obj
        if CB.args.default_cmd is not None:
            default_cmd = CB.args.default_cmd
        with open(CB.args.input_file, "r") as f:
            input_data = yaml.safe_load(f)
        position = 1
        for i in input_data:
            if not isinstance(i, dict) or not "cmd" in i.keys() or not "id" in i.keys():
                eprint("At position number {}: Input data element has unappropriated format".format(position))
                continue
            if i["cmd"] not in possible_cmds + [""]:
                eprint("At position number {}: Input data element contains an unknown command: {}".format(position,
                                                                                                          i["cmd"]))
                continue
            cmd = i.pop("cmd")
            if cmd == "":
                cmd = default_cmd
            if cmd == "c":
                i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                data = CB.base_class(**i_final)
                CB.create_method(data)
            if cmd == "u":
                id = i.pop("id")
                i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                data = CB.base_class(**i_final)
                CB.update_method(id, data)
            if cmd == "d":
                id = i.pop("id")
                CB.delete_method(id)
            position = position + 1
        action_process_result = True
    else:
        pass
    return action_process_result, obj