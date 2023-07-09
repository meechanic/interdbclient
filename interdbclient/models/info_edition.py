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


class InfoEdition(object):
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
        'publisher': 'str',
        'publishing_time': 'str',
        'infsource': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'human_description': 'human_description',
        'machine_description': 'machine_description',
        'edition_number': 'edition_number',
        'publisher': 'publisher',
        'publishing_time': 'publishing_time',
        'infsource': 'infsource'
    }

    def __init__(self, id=None, name=None, human_description=None, machine_description=None, edition_number=None, publisher=None, publishing_time=None, infsource=None, _configuration=None):  # noqa: E501
        """InfoEdition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._human_description = None
        self._machine_description = None
        self._edition_number = None
        self._publisher = None
        self._publishing_time = None
        self._infsource = None
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
        if publisher is not None:
            self.publisher = publisher
        if publishing_time is not None:
            self.publishing_time = publishing_time
        self.infsource = infsource

    @property
    def id(self):
        """Gets the id of this InfoEdition.  # noqa: E501


        :return: The id of this InfoEdition.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InfoEdition.


        :param id: The id of this InfoEdition.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InfoEdition.  # noqa: E501


        :return: The name of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfoEdition.


        :param name: The name of this InfoEdition.  # noqa: E501
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
        """Gets the human_description of this InfoEdition.  # noqa: E501


        :return: The human_description of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._human_description

    @human_description.setter
    def human_description(self, human_description):
        """Sets the human_description of this InfoEdition.


        :param human_description: The human_description of this InfoEdition.  # noqa: E501
        :type: str
        """

        self._human_description = human_description

    @property
    def machine_description(self):
        """Gets the machine_description of this InfoEdition.  # noqa: E501


        :return: The machine_description of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this InfoEdition.


        :param machine_description: The machine_description of this InfoEdition.  # noqa: E501
        :type: str
        """

        self._machine_description = machine_description

    @property
    def edition_number(self):
        """Gets the edition_number of this InfoEdition.  # noqa: E501


        :return: The edition_number of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._edition_number

    @edition_number.setter
    def edition_number(self, edition_number):
        """Sets the edition_number of this InfoEdition.


        :param edition_number: The edition_number of this InfoEdition.  # noqa: E501
        :type: str
        """

        self._edition_number = edition_number

    @property
    def publisher(self):
        """Gets the publisher of this InfoEdition.  # noqa: E501


        :return: The publisher of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this InfoEdition.


        :param publisher: The publisher of this InfoEdition.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def publishing_time(self):
        """Gets the publishing_time of this InfoEdition.  # noqa: E501


        :return: The publishing_time of this InfoEdition.  # noqa: E501
        :rtype: str
        """
        return self._publishing_time

    @publishing_time.setter
    def publishing_time(self, publishing_time):
        """Sets the publishing_time of this InfoEdition.


        :param publishing_time: The publishing_time of this InfoEdition.  # noqa: E501
        :type: str
        """

        self._publishing_time = publishing_time

    @property
    def infsource(self):
        """Gets the infsource of this InfoEdition.  # noqa: E501


        :return: The infsource of this InfoEdition.  # noqa: E501
        :rtype: int
        """
        return self._infsource

    @infsource.setter
    def infsource(self, infsource):
        """Sets the infsource of this InfoEdition.


        :param infsource: The infsource of this InfoEdition.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and infsource is None:
            raise ValueError("Invalid value for `infsource`, must not be `None`")  # noqa: E501

        self._infsource = infsource

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
        if issubclass(InfoEdition, dict):
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
        if not isinstance(other, InfoEdition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfoEdition):
            return True

        return self.to_dict() != other.to_dict()
