# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gameservers.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'steammessages_gameservers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsteammessages_gameservers.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"H\n\"CGameServers_GetServerList_Request\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x12\n\x05limit\x18\x02 \x01(\r:\x03\x31\x30\x30\"\x93\x03\n#CGameServers_GetServerList_Response\x12<\n\x07servers\x18\x01 \x03(\x0b\x32+.CGameServers_GetServerList_Response.Server\x1a\xad\x02\n\x06Server\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\x10\n\x08gameport\x18\x02 \x01(\r\x12\x10\n\x08specport\x18\x03 \x01(\r\x12\x0f\n\x07steamid\x18\x04 \x01(\x06\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x12\x0f\n\x07gamedir\x18\x07 \x01(\t\x12\x0f\n\x07version\x18\x08 \x01(\t\x12\x0f\n\x07product\x18\t \x01(\t\x12\x0e\n\x06region\x18\n \x01(\x05\x12\x0f\n\x07players\x18\x0b \x01(\x05\x12\x13\n\x0bmax_players\x18\x0c \x01(\x05\x12\x0c\n\x04\x62ots\x18\r \x01(\x05\x12\x0b\n\x03map\x18\x0e \x01(\t\x12\x0e\n\x06secure\x18\x0f \x01(\x08\x12\x11\n\tdedicated\x18\x10 \x01(\x08\x12\n\n\x02os\x18\x11 \x01(\t\x12\x10\n\x08gametype\x18\x12 \x01(\t\"@\n*CGameServers_GetServerSteamIDsByIP_Request\x12\x12\n\nserver_ips\x18\x01 \x03(\t\"\x90\x01\n%CGameServers_IPsWithSteamIDs_Response\x12>\n\x07servers\x18\x01 \x03(\x0b\x32-.CGameServers_IPsWithSteamIDs_Response.Server\x1a\'\n\x06Server\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\"E\n*CGameServers_GetServerIPsBySteamID_Request\x12\x17\n\x0fserver_steamids\x18\x01 \x03(\x06\"\x80\x02\n\"CGameServers_QueryByFakeIP_Request\x12\x0f\n\x07\x66\x61ke_ip\x18\x01 \x01(\r\x12\x11\n\tfake_port\x18\x02 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\x12Q\n\nquery_type\x18\x04 \x01(\x0e\x32..CGameServers_QueryByFakeIP_Request.EQueryType:\rQuery_Invalid\"S\n\nEQueryType\x12\x11\n\rQuery_Invalid\x10\x00\x12\x0e\n\nQuery_Ping\x10\x01\x12\x11\n\rQuery_Players\x10\x02\x12\x0f\n\x0bQuery_Rules\x10\x03\"\xd0\x03\n\x1b\x43MsgGameServerPingQueryData\x12!\n\tserver_ip\x18\x01 \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x12\n\nquery_port\x18\x02 \x01(\r\x12\x11\n\tgame_port\x18\x03 \x01(\r\x12\x16\n\x0espectator_port\x18\x04 \x01(\r\x12\x1d\n\x15spectator_server_name\x18\x05 \x01(\t\x12\x13\n\x0bserver_name\x18\x06 \x01(\t\x12\x0f\n\x07steamid\x18\x07 \x01(\x06\x12\x0e\n\x06\x61pp_id\x18\x08 \x01(\r\x12\x0f\n\x07gamedir\x18\t \x01(\t\x12\x0b\n\x03map\x18\n \x01(\t\x12\x18\n\x10game_description\x18\x0b \x01(\t\x12\x10\n\x08gametype\x18\x0c \x01(\t\x12\x13\n\x0bnum_players\x18\r \x01(\r\x12\x13\n\x0bmax_players\x18\x0e \x01(\r\x12\x10\n\x08num_bots\x18\x0f \x01(\r\x12\x10\n\x08password\x18\x10 \x01(\x08\x12\x0e\n\x06secure\x18\x11 \x01(\x08\x12\x11\n\tdedicated\x18\x12 \x01(\x08\x12\x0f\n\x07version\x18\x13 \x01(\t\x12\x11\n\tsdr_popid\x18\x14 \x01(\x07\x12\x1b\n\x13sdr_location_string\x18\x15 \x01(\t\"\x95\x01\n\x1e\x43MsgGameServerPlayersQueryData\x12\x37\n\x07players\x18\x01 \x03(\x0b\x32&.CMsgGameServerPlayersQueryData.Player\x1a:\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\r\x12\x13\n\x0btime_played\x18\x03 \x01(\r\"v\n\x1c\x43MsgGameServerRulesQueryData\x12\x31\n\x05rules\x18\x01 \x03(\x0b\x32\".CMsgGameServerRulesQueryData.Rule\x1a#\n\x04Rule\x12\x0c\n\x04rule\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xc2\x01\n%CGameServers_GameServerQuery_Response\x12/\n\tping_data\x18\x01 \x01(\x0b\x32\x1c.CMsgGameServerPingQueryData\x12\x35\n\x0cplayers_data\x18\x02 \x01(\x0b\x32\x1f.CMsgGameServerPlayersQueryData\x12\x31\n\nrules_data\x18\x03 \x01(\x0b\x32\x1d.CMsgGameServerRulesQueryData\"*\n(GameServerClient_QueryServerData_Request\"\xc6\x01\n)GameServerClient_QueryServerData_Response\x12/\n\tping_data\x18\x01 \x01(\x0b\x32\x1c.CMsgGameServerPingQueryData\x12\x35\n\x0cplayers_data\x18\x02 \x01(\x0b\x32\x1f.CMsgGameServerPlayersQueryData\x12\x31\n\nrules_data\x18\x03 \x01(\x0b\x32\x1d.CMsgGameServerRulesQueryData2\xa3\x03\n\x0bGameServers\x12Z\n\rGetServerList\x12#.CGameServers_GetServerList_Request\x1a$.CGameServers_GetServerList_Response\x12l\n\x15GetServerSteamIDsByIP\x12+.CGameServers_GetServerSteamIDsByIP_Request\x1a&.CGameServers_IPsWithSteamIDs_Response\x12l\n\x15GetServerIPsBySteamID\x12+.CGameServers_GetServerIPsBySteamID_Request\x1a&.CGameServers_IPsWithSteamIDs_Response\x12\\\n\rQueryByFakeIP\x12#.CGameServers_QueryByFakeIP_Request\x1a&.CGameServers_GameServerQuery_Response2\x82\x01\n\x10GameServerClient\x12h\n\x0fQueryServerData\x12).GameServerClient_QueryServerData_Request\x1a*.GameServerClient_QueryServerData_Response\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gameservers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_GAMESERVERCLIENT']._loaded_options = None
  _globals['_GAMESERVERCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_CGAMESERVERS_GETSERVERLIST_REQUEST']._serialized_start=95
  _globals['_CGAMESERVERS_GETSERVERLIST_REQUEST']._serialized_end=167
  _globals['_CGAMESERVERS_GETSERVERLIST_RESPONSE']._serialized_start=170
  _globals['_CGAMESERVERS_GETSERVERLIST_RESPONSE']._serialized_end=573
  _globals['_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER']._serialized_start=272
  _globals['_CGAMESERVERS_GETSERVERLIST_RESPONSE_SERVER']._serialized_end=573
  _globals['_CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST']._serialized_start=575
  _globals['_CGAMESERVERS_GETSERVERSTEAMIDSBYIP_REQUEST']._serialized_end=639
  _globals['_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE']._serialized_start=642
  _globals['_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE']._serialized_end=786
  _globals['_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER']._serialized_start=747
  _globals['_CGAMESERVERS_IPSWITHSTEAMIDS_RESPONSE_SERVER']._serialized_end=786
  _globals['_CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST']._serialized_start=788
  _globals['_CGAMESERVERS_GETSERVERIPSBYSTEAMID_REQUEST']._serialized_end=857
  _globals['_CGAMESERVERS_QUERYBYFAKEIP_REQUEST']._serialized_start=860
  _globals['_CGAMESERVERS_QUERYBYFAKEIP_REQUEST']._serialized_end=1116
  _globals['_CGAMESERVERS_QUERYBYFAKEIP_REQUEST_EQUERYTYPE']._serialized_start=1033
  _globals['_CGAMESERVERS_QUERYBYFAKEIP_REQUEST_EQUERYTYPE']._serialized_end=1116
  _globals['_CMSGGAMESERVERPINGQUERYDATA']._serialized_start=1119
  _globals['_CMSGGAMESERVERPINGQUERYDATA']._serialized_end=1583
  _globals['_CMSGGAMESERVERPLAYERSQUERYDATA']._serialized_start=1586
  _globals['_CMSGGAMESERVERPLAYERSQUERYDATA']._serialized_end=1735
  _globals['_CMSGGAMESERVERPLAYERSQUERYDATA_PLAYER']._serialized_start=1677
  _globals['_CMSGGAMESERVERPLAYERSQUERYDATA_PLAYER']._serialized_end=1735
  _globals['_CMSGGAMESERVERRULESQUERYDATA']._serialized_start=1737
  _globals['_CMSGGAMESERVERRULESQUERYDATA']._serialized_end=1855
  _globals['_CMSGGAMESERVERRULESQUERYDATA_RULE']._serialized_start=1820
  _globals['_CMSGGAMESERVERRULESQUERYDATA_RULE']._serialized_end=1855
  _globals['_CGAMESERVERS_GAMESERVERQUERY_RESPONSE']._serialized_start=1858
  _globals['_CGAMESERVERS_GAMESERVERQUERY_RESPONSE']._serialized_end=2052
  _globals['_GAMESERVERCLIENT_QUERYSERVERDATA_REQUEST']._serialized_start=2054
  _globals['_GAMESERVERCLIENT_QUERYSERVERDATA_REQUEST']._serialized_end=2096
  _globals['_GAMESERVERCLIENT_QUERYSERVERDATA_RESPONSE']._serialized_start=2099
  _globals['_GAMESERVERCLIENT_QUERYSERVERDATA_RESPONSE']._serialized_end=2297
  _globals['_GAMESERVERS']._serialized_start=2300
  _globals['_GAMESERVERS']._serialized_end=2719
  _globals['_GAMESERVERCLIENT']._serialized_start=2722
  _globals['_GAMESERVERCLIENT']._serialized_end=2852
_builder.BuildServices(DESCRIPTOR, 'steammessages_gameservers_pb2', _globals)
# @@protoc_insertion_point(module_scope)
