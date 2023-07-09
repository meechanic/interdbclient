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


class ProgEdition(object):
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
        'edition_number': 'str',
        'package': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'human_description': 'human_description',
        'machine_description': 'machine_description',
        'edition_number': 'edition_number',
        'package': 'package'
    }

    def __init__(self, id=None, name=None, human_description=None, machine_description=None, edition_number=None, package=None, _configuration=None):  # noqa: E501
        """ProgEdition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._human_description = None
        self._machine_description = None
        self._edition_number = None
        self._package = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if human_description is not None:
            self.human_description = human_description
        if machine_description is not None:
            self.machine_description = machine_description
        if edition_number is not None:
            self.edition_number = edition_number
        self.package = package

    @property
    def id(self):
        """Gets the id of this ProgEdition.  # noqa: E501


        :return: The id of this ProgEdition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProgEdition.


        :param id: The id of this ProgEdition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProgEdition.  # noqa: E501


        :return: The name of this ProgEdition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProgEdition.


        :param name: The name of this ProgEdition.  # noqa: E501
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
        """Gets the human_description of this ProgEdition.  # noqa: E501


        :return: The human_description of this ProgEdition.  # noqa: E501
        :rtype: str
        """
        return self._human_description

    @human_description.setter
    def human_description(self, human_description):
        """Sets the human_description of this ProgEdition.


        :param human_description: The human_description of this ProgEdition.  # noqa: E501
        :type: str
        """

        self._human_description = human_description

    @property
    def machine_description(self):
        """Gets the machine_description of this ProgEdition.  # noqa: E501


        :return: The machine_description of this ProgEdition.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this ProgEdition.


        :param machine_description: The machine_description of this ProgEdition.  # noqa: E501
        :type: str
        """

        self._machine_description = machine_description

    @property
    def edition_number(self):
        """Gets the edition_number of this ProgEdition.  # noqa: E501


        :return: The edition_number of this ProgEdition.  # noqa: E501
        :rtype: str
        """
        return self._edition_number

    @edition_number.setter
    def edition_number(self, edition_number):
        """Sets the edition_number of this ProgEdition.


        :param edition_number: The edition_number of this ProgEdition.  # noqa: E501
        :type: str
        """

        self._edition_number = edition_number

    @property
    def package(self):
        """Gets the package of this ProgEdition.  # noqa: E501


        :return: The package of this ProgEdition.  # noqa: E501
        :rtype: int
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this ProgEdition.


        :param package: The package of this ProgEdition.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and package is None:
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

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
        if issubclass(ProgEdition, dict):
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
        if not isinstance(other, ProgEdition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgEdition):
            return True

        return self.to_dict() != other.to_dict()
