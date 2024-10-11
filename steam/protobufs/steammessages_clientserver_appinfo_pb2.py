# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_clientserver_appinfo.proto
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
    'steammessages_clientserver_appinfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(steammessages_clientserver_appinfo.proto\x1a\x18steammessages_base.proto\"M\n\x17\x43MsgClientAppInfoUpdate\x12\x19\n\x11last_changenumber\x18\x01 \x01(\r\x12\x17\n\x0fsend_changelist\x18\x02 \x01(\x08\"d\n\x18\x43MsgClientAppInfoChanges\x12\x1d\n\x15\x63urrent_change_number\x18\x01 \x01(\r\x12\x19\n\x11\x66orce_full_update\x18\x02 \x01(\x08\x12\x0e\n\x06\x61ppIDs\x18\x03 \x03(\r\"\xab\x01\n\x18\x43MsgClientAppInfoRequest\x12+\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x1d.CMsgClientAppInfoRequest.App\x12\x1f\n\x10supports_batches\x18\x02 \x01(\x08:\x05\x66\x61lse\x1a\x41\n\x03\x41pp\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x15\n\rsection_flags\x18\x02 \x01(\r\x12\x13\n\x0bsection_CRC\x18\x03 \x03(\r\"\xc0\x01\n!CMsgClientPICSChangesSinceRequest\x12\x1b\n\x13since_change_number\x18\x01 \x01(\r\x12\x1d\n\x15send_app_info_changes\x18\x02 \x01(\x08\x12!\n\x19send_package_info_changes\x18\x03 \x01(\x08\x12\x1b\n\x13num_app_info_cached\x18\x04 \x01(\r\x12\x1f\n\x17num_package_info_cached\x18\x05 \x01(\r\"\xe5\x03\n\"CMsgClientPICSChangesSinceResponse\x12\x1d\n\x15\x63urrent_change_number\x18\x01 \x01(\r\x12\x1b\n\x13since_change_number\x18\x02 \x01(\r\x12\x19\n\x11\x66orce_full_update\x18\x03 \x01(\x08\x12J\n\x0fpackage_changes\x18\x04 \x03(\x0b\x32\x31.CMsgClientPICSChangesSinceResponse.PackageChange\x12\x42\n\x0b\x61pp_changes\x18\x05 \x03(\x0b\x32-.CMsgClientPICSChangesSinceResponse.AppChange\x12\x1d\n\x15\x66orce_full_app_update\x18\x06 \x01(\x08\x12!\n\x19\x66orce_full_package_update\x18\x07 \x01(\x08\x1aN\n\rPackageChange\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x15\n\rchange_number\x18\x02 \x01(\r\x12\x13\n\x0bneeds_token\x18\x03 \x01(\x08\x1a\x46\n\tAppChange\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x15\n\rchange_number\x18\x02 \x01(\r\x12\x13\n\x0bneeds_token\x18\x03 \x01(\x08\"\xaf\x03\n CMsgClientPICSProductInfoRequest\x12?\n\x08packages\x18\x01 \x03(\x0b\x32-.CMsgClientPICSProductInfoRequest.PackageInfo\x12\x37\n\x04\x61pps\x18\x02 \x03(\x0b\x32).CMsgClientPICSProductInfoRequest.AppInfo\x12\x16\n\x0emeta_data_only\x18\x03 \x01(\x08\x12\x17\n\x0fnum_prev_failed\x18\x04 \x01(\r\x12(\n OBSOLETE_supports_package_tokens\x18\x05 \x01(\r\x12\x17\n\x0fsequence_number\x18\x06 \x01(\r\x12\x17\n\x0fsingle_response\x18\x07 \x01(\x08\x1aL\n\x07\x41ppInfo\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\x04\x12\x1c\n\x14only_public_obsolete\x18\x03 \x01(\x08\x1a\x36\n\x0bPackageInfo\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\x04\"\xb9\x04\n!CMsgClientPICSProductInfoResponse\x12\x38\n\x04\x61pps\x18\x01 \x03(\x0b\x32*.CMsgClientPICSProductInfoResponse.AppInfo\x12\x16\n\x0eunknown_appids\x18\x02 \x03(\r\x12@\n\x08packages\x18\x03 \x03(\x0b\x32..CMsgClientPICSProductInfoResponse.PackageInfo\x12\x1a\n\x12unknown_packageids\x18\x04 \x03(\r\x12\x16\n\x0emeta_data_only\x18\x05 \x01(\x08\x12\x18\n\x10response_pending\x18\x06 \x01(\x08\x12\x15\n\rhttp_min_size\x18\x07 \x01(\r\x12\x11\n\thttp_host\x18\x08 \x01(\t\x1a\x86\x01\n\x07\x41ppInfo\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x15\n\rchange_number\x18\x02 \x01(\r\x12\x15\n\rmissing_token\x18\x03 \x01(\x08\x12\x0b\n\x03sha\x18\x04 \x01(\x0c\x12\x0e\n\x06\x62uffer\x18\x05 \x01(\x0c\x12\x13\n\x0bonly_public\x18\x06 \x01(\x08\x12\x0c\n\x04size\x18\x07 \x01(\r\x1ay\n\x0bPackageInfo\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x15\n\rchange_number\x18\x02 \x01(\r\x12\x15\n\rmissing_token\x18\x03 \x01(\x08\x12\x0b\n\x03sha\x18\x04 \x01(\x0c\x12\x0e\n\x06\x62uffer\x18\x05 \x01(\x0c\x12\x0c\n\x04size\x18\x06 \x01(\r:\x04\x88\xb5\x18\x00\"F\n CMsgClientPICSAccessTokenRequest\x12\x12\n\npackageids\x18\x01 \x03(\r\x12\x0e\n\x06\x61ppids\x18\x02 \x03(\r\"\xdf\x02\n!CMsgClientPICSAccessTokenResponse\x12N\n\x15package_access_tokens\x18\x01 \x03(\x0b\x32/.CMsgClientPICSAccessTokenResponse.PackageToken\x12\x1d\n\x15package_denied_tokens\x18\x02 \x03(\r\x12\x46\n\x11\x61pp_access_tokens\x18\x03 \x03(\x0b\x32+.CMsgClientPICSAccessTokenResponse.AppToken\x12\x19\n\x11\x61pp_denied_tokens\x18\x04 \x03(\r\x1a\x37\n\x0cPackageToken\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\x04\x1a/\n\x08\x41ppToken\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\x04\"q\n CMsgClientPICSPrivateBetaRequest\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\x04\x12\x11\n\tbeta_name\x18\x03 \x01(\t\x12\x15\n\rpassword_hash\x18\x04 \x01(\x0c\"N\n!CMsgClientPICSPrivateBetaResponse\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\x12\x15\n\rdepot_section\x18\x02 \x01(\x0c\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_appinfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE']._loaded_options = None
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE']._serialized_options = b'\210\265\030\000'
  _globals['_CMSGCLIENTAPPINFOUPDATE']._serialized_start=70
  _globals['_CMSGCLIENTAPPINFOUPDATE']._serialized_end=147
  _globals['_CMSGCLIENTAPPINFOCHANGES']._serialized_start=149
  _globals['_CMSGCLIENTAPPINFOCHANGES']._serialized_end=249
  _globals['_CMSGCLIENTAPPINFOREQUEST']._serialized_start=252
  _globals['_CMSGCLIENTAPPINFOREQUEST']._serialized_end=423
  _globals['_CMSGCLIENTAPPINFOREQUEST_APP']._serialized_start=358
  _globals['_CMSGCLIENTAPPINFOREQUEST_APP']._serialized_end=423
  _globals['_CMSGCLIENTPICSCHANGESSINCEREQUEST']._serialized_start=426
  _globals['_CMSGCLIENTPICSCHANGESSINCEREQUEST']._serialized_end=618
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE']._serialized_start=621
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE']._serialized_end=1106
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE_PACKAGECHANGE']._serialized_start=956
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE_PACKAGECHANGE']._serialized_end=1034
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE_APPCHANGE']._serialized_start=1036
  _globals['_CMSGCLIENTPICSCHANGESSINCERESPONSE_APPCHANGE']._serialized_end=1106
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST']._serialized_start=1109
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST']._serialized_end=1540
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST_APPINFO']._serialized_start=1408
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST_APPINFO']._serialized_end=1484
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST_PACKAGEINFO']._serialized_start=1486
  _globals['_CMSGCLIENTPICSPRODUCTINFOREQUEST_PACKAGEINFO']._serialized_end=1540
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE']._serialized_start=1543
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE']._serialized_end=2112
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE_APPINFO']._serialized_start=1849
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE_APPINFO']._serialized_end=1983
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE_PACKAGEINFO']._serialized_start=1985
  _globals['_CMSGCLIENTPICSPRODUCTINFORESPONSE_PACKAGEINFO']._serialized_end=2106
  _globals['_CMSGCLIENTPICSACCESSTOKENREQUEST']._serialized_start=2114
  _globals['_CMSGCLIENTPICSACCESSTOKENREQUEST']._serialized_end=2184
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE']._serialized_start=2187
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE']._serialized_end=2538
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE_PACKAGETOKEN']._serialized_start=2434
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE_PACKAGETOKEN']._serialized_end=2489
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE_APPTOKEN']._serialized_start=2491
  _globals['_CMSGCLIENTPICSACCESSTOKENRESPONSE_APPTOKEN']._serialized_end=2538
  _globals['_CMSGCLIENTPICSPRIVATEBETAREQUEST']._serialized_start=2540
  _globals['_CMSGCLIENTPICSPRIVATEBETAREQUEST']._serialized_end=2653
  _globals['_CMSGCLIENTPICSPRIVATEBETARESPONSE']._serialized_start=2655
  _globals['_CMSGCLIENTPICSPRIVATEBETARESPONSE']._serialized_end=2733
# @@protoc_insertion_point(module_scope)
