# coding: utf-8

"""
    InterDB API

    InterDB API  # noqa: E501

    OpenAPI spec version: v1
    Contact: meechanic.design@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from interdbclient.configuration import Configuration


class Package(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'human_description': 'str',
        'machine_description': 'str',
        'main_prog_language': 'str',
        'supercategory': 'str',
        'category': 'str',
        'subcategory': 'str',
        'license_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'human_description': 'human_description',
        'machine_description': 'machine_description',
        'main_prog_language': 'main_prog_language',
        'supercategory': 'supercategory',
        'category': 'category',
        'subcategory': 'subcategory',
        'license_type': 'license_type'
    }

    def __init__(self, id=None, name=None, human_description=None, machine_description=None, main_prog_language=None, supercategory=None, category=None, subcategory=None, license_type=None, _configuration=None):  # noqa: E501
        """Package - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._human_description = None
        self._machine_description = None
        self._main_prog_language = None
        self._supercategory = None
        self._category = None
        self._subcategory = None
        self._license_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if human_description is not None:
            self.human_description = human_description
        if machine_description is not None:
            self.machine_description = machine_description
        if main_prog_language is not None:
            self.main_prog_language = main_prog_language
        if supercategory is not None:
            self.supercategory = supercategory
        if category is not None:
            self.category = category
        if subcategory is not None:
            self.subcategory = subcategory
        if license_type is not None:
            self.license_type = license_type

    @property
    def id(self):
        """Gets the id of this Package.  # noqa: E501


        :return: The id of this Package.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Package.


        :param id: The id of this Package.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Package.  # noqa: E501


        :return: The name of this Package.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Package.


        :param name: The name of this Package.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def human_description(self):
        """Gets the human_description of this Package.  # noqa: E501


        :return: The human_description of this Package.  # noqa: E501
        :rtype: str
        """
        return self._human_description

    @human_description.setter
    def human_description(self, human_description):
        """Sets the human_description of this Package.


        :param human_description: The human_description of this Package.  # noqa: E501
        :type: str
        """

        self._human_description = human_description

    @property
    def machine_description(self):
        """Gets the machine_description of this Package.  # noqa: E501


        :return: The machine_description of this Package.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this Package.


        :param machine_description: The machine_description of this Package.  # noqa: E501
        :type: str
        """

        self._machine_description = machine_description

    @property
    def main_prog_language(self):
        """Gets the main_prog_language of this Package.  # noqa: E501


        :return: The main_prog_language of this Package.  # noqa: E501
        :rtype: str
        """
        return self._main_prog_language

    @main_prog_language.setter
    def main_prog_language(self, main_prog_language):
        """Sets the main_prog_language of this Package.


        :param main_prog_language: The main_prog_language of this Package.  # noqa: E501
        :type: str
        """

        self._main_prog_language = main_prog_language

    @property
    def supercategory(self):
        """Gets the supercategory of this Package.  # noqa: E501


        :return: The supercategory of this Package.  # noqa: E501
        :rtype: str
        """
        return self._supercategory

    @supercategory.setter
    def supercategory(self, supercategory):
        """Sets the supercategory of this Package.


        :param supercategory: The supercategory of this Package.  # noqa: E501
        :type: str
        """

        self._supercategory = supercategory

    @property
    def category(self):
        """Gets the category of this Package.  # noqa: E501


        :return: The category of this Package.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Package.


        :param category: The category of this Package.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def subcategory(self):
        """Gets the subcategory of this Package.  # noqa: E501


        :return: The subcategory of this Package.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this Package.


        :param subcategory: The subcategory of this Package.  # noqa: E501
        :type: str
        """

        self._subcategory = subcategory

    @property
    def license_type(self):
        """Gets the license_type of this Package.  # noqa: E501


        :return: The license_type of this Package.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this Package.


        :param license_type: The license_type of this Package.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Package, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Package):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Package):
            return True

        return self.to_dict() != other.to_dict()
