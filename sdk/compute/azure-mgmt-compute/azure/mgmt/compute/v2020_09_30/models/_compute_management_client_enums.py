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

from enum import Enum


class GallerySharingPermissionTypes(str, Enum):

    private = "Private"
    groups = "Groups"


class SharingProfileGroupTypes(str, Enum):

    subscriptions = "Subscriptions"
    aad_tenants = "AADTenants"


class OperatingSystemTypes(str, Enum):

    windows = "Windows"
    linux = "Linux"


class AggregatedReplicationState(str, Enum):

    unknown = "Unknown"
    in_progress = "InProgress"
    completed = "Completed"
    failed = "Failed"


class ReplicationState(str, Enum):

    unknown = "Unknown"
    replicating = "Replicating"
    completed = "Completed"
    failed = "Failed"


class OperatingSystemStateTypes(str, Enum):

    generalized = "Generalized"
    specialized = "Specialized"


class HyperVGeneration(str, Enum):

    v1 = "V1"
    v2 = "V2"


class StorageAccountType(str, Enum):

    standard_lrs = "Standard_LRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"


class HostCaching(str, Enum):

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"


class SharingUpdateOperationTypes(str, Enum):

    add = "Add"
    remove = "Remove"
    reset = "Reset"


class Permissions(str, Enum):

    permissions = "Permissions"


class ReplicationStatusTypes(str, Enum):

    replication_status = "ReplicationStatus"


class SharedToValues(str, Enum):

    tenant = "tenant"