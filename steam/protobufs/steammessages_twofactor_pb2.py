# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_twofactor.proto
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
    'steammessages_twofactor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsteammessages_twofactor.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\".\n\x17\x43TwoFactor_Time_Request\x12\x13\n\x0bsender_time\x18\x01 \x01(\x04\"\xa5\x02\n\x18\x43TwoFactor_Time_Response\x12\x13\n\x0bserver_time\x18\x01 \x01(\x04\x12\x1e\n\x16skew_tolerance_seconds\x18\x02 \x01(\x04\x12\x17\n\x0flarge_time_jink\x18\x03 \x01(\x04\x12\x1f\n\x17probe_frequency_seconds\x18\x04 \x01(\r\x12-\n%adjusted_time_probe_frequency_seconds\x18\x05 \x01(\r\x12$\n\x1chint_probe_frequency_seconds\x18\x06 \x01(\r\x12\x14\n\x0csync_timeout\x18\x07 \x01(\r\x12\x19\n\x11try_again_seconds\x18\x08 \x01(\r\x12\x14\n\x0cmax_attempts\x18\t \x01(\r\",\n\x19\x43TwoFactor_Status_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\x8d\x03\n\x1a\x43TwoFactor_Status_Response\x12\r\n\x05state\x18\x01 \x01(\r\x12\x1b\n\x13inactivation_reason\x18\x02 \x01(\r\x12\x1a\n\x12\x61uthenticator_type\x18\x03 \x01(\r\x12\x1d\n\x15\x61uthenticator_allowed\x18\x04 \x01(\x08\x12\x19\n\x11steamguard_scheme\x18\x05 \x01(\r\x12\x11\n\ttoken_gid\x18\x06 \x01(\t\x12\x17\n\x0f\x65mail_validated\x18\x07 \x01(\x08\x12\x19\n\x11\x64\x65vice_identifier\x18\x08 \x01(\t\x12\x14\n\x0ctime_created\x18\t \x01(\r\x12%\n\x1drevocation_attempts_remaining\x18\n \x01(\r\x12\x18\n\x10\x63lassified_agent\x18\x0b \x01(\t\x12$\n\x1c\x61llow_external_authenticator\x18\x0c \x01(\x08\x12\x18\n\x10time_transferred\x18\r \x01(\r\x12\x0f\n\x07version\x18\x0e \x01(\r\"\xca\x01\n#CTwoFactor_AddAuthenticator_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x1a\n\x12\x61uthenticator_time\x18\x02 \x01(\x04\x12\x15\n\rserial_number\x18\x03 \x01(\x06\x12\x1a\n\x12\x61uthenticator_type\x18\x04 \x01(\r\x12\x19\n\x11\x64\x65vice_identifier\x18\x05 \x01(\t\x12\x14\n\x0chttp_headers\x18\x07 \x03(\t\x12\x12\n\x07version\x18\x08 \x01(\r:\x01\x31\"\xa4\x02\n$CTwoFactor_AddAuthenticator_Response\x12\x15\n\rshared_secret\x18\x01 \x01(\x0c\x12\x15\n\rserial_number\x18\x02 \x01(\x06\x12\x17\n\x0frevocation_code\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x13\n\x0bserver_time\x18\x05 \x01(\x04\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x06 \x01(\t\x12\x11\n\ttoken_gid\x18\x07 \x01(\t\x12\x17\n\x0fidentity_secret\x18\x08 \x01(\x0c\x12\x10\n\x08secret_1\x18\t \x01(\x0c\x12\x0e\n\x06status\x18\n \x01(\x05\x12\x19\n\x11phone_number_hint\x18\x0b \x01(\t\x12\x14\n\x0c\x63onfirm_type\x18\x0c \x01(\x05\"d\n\x1c\x43TwoFactor_SendEmail_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\nemail_type\x18\x02 \x01(\r\x12\x1f\n\x17include_activation_code\x18\x03 \x01(\x08\"\x1f\n\x1d\x43TwoFactor_SendEmail_Response\"\xc0\x01\n+CTwoFactor_FinalizeAddAuthenticator_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x1a\n\x12\x61uthenticator_code\x18\x02 \x01(\t\x12\x1a\n\x12\x61uthenticator_time\x18\x03 \x01(\x04\x12\x17\n\x0f\x61\x63tivation_code\x18\x04 \x01(\t\x12\x14\n\x0chttp_headers\x18\x05 \x03(\t\x12\x19\n\x11validate_sms_code\x18\x06 \x01(\x08\"d\n,CTwoFactor_FinalizeAddAuthenticator_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bserver_time\x18\x03 \x01(\x04\x12\x0e\n\x06status\x18\x04 \x01(\x05\"\\\n%CTwoFactor_UpdateTokenVersion_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"(\n&CTwoFactor_UpdateTokenVersion_Response\"\x9e\x01\n&CTwoFactor_RemoveAuthenticator_Request\x12\x17\n\x0frevocation_code\x18\x02 \x01(\t\x12\x19\n\x11revocation_reason\x18\x05 \x01(\r\x12\x19\n\x11steamguard_scheme\x18\x06 \x01(\r\x12%\n\x1dremove_all_steamguard_cookies\x18\x07 \x01(\x08\"v\n\'CTwoFactor_RemoveAuthenticator_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bserver_time\x18\x03 \x01(\x04\x12%\n\x1drevocation_attempts_remaining\x18\x05 \x01(\r\"9\n7CTwoFactor_RemoveAuthenticatorViaChallengeStart_Request\"K\n8CTwoFactor_RemoveAuthenticatorViaChallengeStart_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\"~\n:CTwoFactor_RemoveAuthenticatorViaChallengeContinue_Request\x12\x10\n\x08sms_code\x18\x01 \x01(\t\x12\x1a\n\x12generate_new_token\x18\x02 \x01(\x08\x12\x12\n\x07version\x18\x03 \x01(\r:\x01\x31\"\xb5\x02\n:CRemoveAuthenticatorViaChallengeContinue_Replacement_Token\x12\x15\n\rshared_secret\x18\x01 \x01(\x0c\x12\x15\n\rserial_number\x18\x02 \x01(\x06\x12\x17\n\x0frevocation_code\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x13\n\x0bserver_time\x18\x05 \x01(\x04\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x06 \x01(\t\x12\x11\n\ttoken_gid\x18\x07 \x01(\t\x12\x17\n\x0fidentity_secret\x18\x08 \x01(\x0c\x12\x10\n\x08secret_1\x18\t \x01(\x0c\x12\x0e\n\x06status\x18\n \x01(\x05\x12\x19\n\x11steamguard_scheme\x18\x0b \x01(\r\x12\x0f\n\x07steamid\x18\x0c \x01(\x06\"\xa6\x01\n;CTwoFactor_RemoveAuthenticatorViaChallengeContinue_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12V\n\x11replacement_token\x18\x02 \x01(\x0b\x32;.CRemoveAuthenticatorViaChallengeContinue_Replacement_Token2\xd1\x07\n\tTwoFactor\x12@\n\tQueryTime\x12\x18.CTwoFactor_Time_Request\x1a\x19.CTwoFactor_Time_Response\x12\x46\n\x0bQueryStatus\x12\x1a.CTwoFactor_Status_Request\x1a\x1b.CTwoFactor_Status_Response\x12_\n\x10\x41\x64\x64\x41uthenticator\x12$.CTwoFactor_AddAuthenticator_Request\x1a%.CTwoFactor_AddAuthenticator_Response\x12J\n\tSendEmail\x12\x1d.CTwoFactor_SendEmail_Request\x1a\x1e.CTwoFactor_SendEmail_Response\x12w\n\x18\x46inalizeAddAuthenticator\x12,.CTwoFactor_FinalizeAddAuthenticator_Request\x1a-.CTwoFactor_FinalizeAddAuthenticator_Response\x12\x65\n\x12UpdateTokenVersion\x12&.CTwoFactor_UpdateTokenVersion_Request\x1a\'.CTwoFactor_UpdateTokenVersion_Response\x12h\n\x13RemoveAuthenticator\x12\'.CTwoFactor_RemoveAuthenticator_Request\x1a(.CTwoFactor_RemoveAuthenticator_Response\x12\x9b\x01\n$RemoveAuthenticatorViaChallengeStart\x12\x38.CTwoFactor_RemoveAuthenticatorViaChallengeStart_Request\x1a\x39.CTwoFactor_RemoveAuthenticatorViaChallengeStart_Response\x12\xa4\x01\n\'RemoveAuthenticatorViaChallengeContinue\x12;.CTwoFactor_RemoveAuthenticatorViaChallengeContinue_Request\x1a<.CTwoFactor_RemoveAuthenticatorViaChallengeContinue_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_twofactor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CTWOFACTOR_TIME_REQUEST']._serialized_start=93
  _globals['_CTWOFACTOR_TIME_REQUEST']._serialized_end=139
  _globals['_CTWOFACTOR_TIME_RESPONSE']._serialized_start=142
  _globals['_CTWOFACTOR_TIME_RESPONSE']._serialized_end=435
  _globals['_CTWOFACTOR_STATUS_REQUEST']._serialized_start=437
  _globals['_CTWOFACTOR_STATUS_REQUEST']._serialized_end=481
  _globals['_CTWOFACTOR_STATUS_RESPONSE']._serialized_start=484
  _globals['_CTWOFACTOR_STATUS_RESPONSE']._serialized_end=881
  _globals['_CTWOFACTOR_ADDAUTHENTICATOR_REQUEST']._serialized_start=884
  _globals['_CTWOFACTOR_ADDAUTHENTICATOR_REQUEST']._serialized_end=1086
  _globals['_CTWOFACTOR_ADDAUTHENTICATOR_RESPONSE']._serialized_start=1089
  _globals['_CTWOFACTOR_ADDAUTHENTICATOR_RESPONSE']._serialized_end=1381
  _globals['_CTWOFACTOR_SENDEMAIL_REQUEST']._serialized_start=1383
  _globals['_CTWOFACTOR_SENDEMAIL_REQUEST']._serialized_end=1483
  _globals['_CTWOFACTOR_SENDEMAIL_RESPONSE']._serialized_start=1485
  _globals['_CTWOFACTOR_SENDEMAIL_RESPONSE']._serialized_end=1516
  _globals['_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_REQUEST']._serialized_start=1519
  _globals['_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_REQUEST']._serialized_end=1711
  _globals['_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_RESPONSE']._serialized_start=1713
  _globals['_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_RESPONSE']._serialized_end=1813
  _globals['_CTWOFACTOR_UPDATETOKENVERSION_REQUEST']._serialized_start=1815
  _globals['_CTWOFACTOR_UPDATETOKENVERSION_REQUEST']._serialized_end=1907
  _globals['_CTWOFACTOR_UPDATETOKENVERSION_RESPONSE']._serialized_start=1909
  _globals['_CTWOFACTOR_UPDATETOKENVERSION_RESPONSE']._serialized_end=1949
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATOR_REQUEST']._serialized_start=1952
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATOR_REQUEST']._serialized_end=2110
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATOR_RESPONSE']._serialized_start=2112
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATOR_RESPONSE']._serialized_end=2230
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGESTART_REQUEST']._serialized_start=2232
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGESTART_REQUEST']._serialized_end=2289
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGESTART_RESPONSE']._serialized_start=2291
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGESTART_RESPONSE']._serialized_end=2366
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGECONTINUE_REQUEST']._serialized_start=2368
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGECONTINUE_REQUEST']._serialized_end=2494
  _globals['_CREMOVEAUTHENTICATORVIACHALLENGECONTINUE_REPLACEMENT_TOKEN']._serialized_start=2497
  _globals['_CREMOVEAUTHENTICATORVIACHALLENGECONTINUE_REPLACEMENT_TOKEN']._serialized_end=2806
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGECONTINUE_RESPONSE']._serialized_start=2809
  _globals['_CTWOFACTOR_REMOVEAUTHENTICATORVIACHALLENGECONTINUE_RESPONSE']._serialized_end=2975
  _globals['_TWOFACTOR']._serialized_start=2978
  _globals['_TWOFACTOR']._serialized_end=3955
_builder.BuildServices(DESCRIPTOR, 'steammessages_twofactor_pb2', _globals)
# @@protoc_insertion_point(module_scope)
