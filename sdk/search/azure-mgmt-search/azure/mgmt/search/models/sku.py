# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sku(Model):
    """Defines the SKU of an Azure Search Service, which determines price tier and
    capacity limits.

    :param name: The SKU of the Search service. Valid values include: 'free':
     Shared service. 'basic': Dedicated service with up to 3 replicas.
     'standard': Dedicated service with up to 12 partitions and 12 replicas.
     'standard2': Similar to standard, but with more capacity per search unit.
     'standard3': The largest Standard offering with up to 12 partitions and 12
     replicas (or up to 3 partitions with more indexes if you also set the
     hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports
     1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports
     2TB per partition, up to 12 partitions.'. Possible values include: 'free',
     'basic', 'standard', 'standard2', 'standard3', 'storage_optimized_l1',
     'storage_optimized_l2'
    :type name: str or ~azure.mgmt.search.models.SkuName
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'SkuName'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)