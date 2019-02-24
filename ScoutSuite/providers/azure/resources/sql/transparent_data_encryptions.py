# -*- coding: utf-8 -*-

from azure.mgmt.sql import SqlManagementClient

from ..resources import AzureSimpleResources


class TransparentDataEncryptions(AzureSimpleResources):

    def __init__(self, resource_group_name, server_name, database_name, facade):
        self.resource_group_name = resource_group_name
        self.server_name = server_name
        self.database_name = database_name
        self.facade = facade

    # TODO: make it really async.
    async def get_resources_from_api(self):
        return self.facade.transparent_data_encryptions.get(
            self.resource_group_name, self.server_name, self.database_name)

    def parse_resource(self, encryptions):
        return 'transparent_data_encryption_enabled', encryptions.status == "Enabled"
