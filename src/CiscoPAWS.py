__author__ = 'Melvin Douglas'
__version__ = '12'
__email__ = 'melvin.douglas@hotmail.com'
__status__ = 'Production'

import os
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth
import urllib3
#from loguru import logger

class APIVersionService:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/platform-services/services/APIVersionService?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
    def list_services(self):
        values = []
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                values.append(port.binding._operations.values())
        return values
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.client.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result
    def getAPIVersion(self, data, serialize=False):
        return self._callSoap_func('getAPIVersion', data, serialize)

class CancelUpgradeService:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/platform-services/services/CancelUpgradeService?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
    def list_services(self):
        values = []
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                values.append(port.binding._operations.values())
        return values
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.client.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result
    def cancelUpgrade(self, data, serialize=False):
        return self._callSoap_func('cancelUpgrade', data, serialize)

class ClusterNodesService:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/platform-services/services/ClusterNodesService?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
    def list_services(self):
        values = []
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                values.append(port.binding._operations.values())
        return values
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.client.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result
    def getClusterNodes(self, data, serialize=False):
        return self._callSoap_func('getClusterNodes', data, serialize)
    def getClusterStatus(self, data, serialize=False):
        return self._callSoap_func('getClusterStatus', data, serialize)
    def getMyClusterNode(self, data, serialize=False):
        return self._callSoap_func('getMyClusterNode', data, serialize)
    def isClusterReplicationOK(self, data, serialize=False):
        return self._callSoap_func('isClusterReplicationOK', data, serialize)
    def IsNodeReplicationOK(self, data, serialize=False):
        return self._callSoap_func('IsNodeReplicationOK', data, serialize)

#DataExportService dataExport
#DataExportStatusService dataExportStatus
#DeploymentModeService getDeploymentMode
#HardwareInformationService getHardwareInformation
#HardwareModelService getHardwareModel
#MaintenanceService scheduleBackup startBackup getBackupProgress
#NetworkService checkNetworkChangeStatus setHostname setIpAddress setNetworkInfo getNetworkInfo
#NetworkDiagnosticService checkNetworkStatus
#OptionsService getActiveOptions getInactiveOptions
#PlatformConfigExportService platformConfigExport
#PrepareRemoteUpgradeService prepareRemoteUpgrade
#ProductService getInstalledProducts getProductName
#RestartSystemService restartSystem
#RestartSystemStatusService getRestartSystemStatus 
#SSOService getStatus enableSSO clearTestStatus uploadIdPMetadata downloadIdPMetadata downloadSPMetadata downloadSPExtendedMetadata
#StartUpgradeService startUpgrade
#SwitchVersionService switchVersions
#SwitchVersionStatusService getSwitchVersionStatus
#UffDbImportExportService uffDbImportExport
#UpgradeFilterService upgradeFilter
#UpgradeProgressStageService getCurrentUpgradeProgressStage
#UpgradeStageService getUpgradeStage
#UpgradeTypeService getUpgradeType
#UpgradeValidService isUpgradeValid 
#VersionService getActiveVersion getInActiveVersion



class MaintenanceService:
    def __init__(self, username, password, hostname, tls_verify=True, timeout=10):
        self.last_exception = None
        wsdl = f'https://{hostname}/platform-services/services/MaintenanceService?wsdl'
        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)
        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])
    def list_services(self):
        values = []
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                values.append(port.binding._operations.values())
        return values
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.client.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result
    def scheduleBackup(self, data, serialize=False):
        return self._callSoap_func('scheduleBackup', data, serialize)
    def startBackup(self, data, serialize=False):
        return self._callSoap_func('startBackup', data, serialize)
    def getBackupProgress(self, data, serialize=False):
        return self._callSoap_func('getBackupProgress', data, serialize)
