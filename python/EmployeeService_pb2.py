# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EmployeeService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x45mployeeService.proto\x12\x10\x65mployee_service\"G\n\x0c\x45mployeeData\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\x02\"\x1d\n\x0bStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x18\n\nEmployeeID\x12\n\n\x02id\x18\x01 \x01(\r\"0\n\x13\x45mployeeTitleUpdate\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05title\x18\x02 \x01(\t\"\x0e\n\x0c\x45mptyMessage\"I\n\x10\x45mployeeDataList\x12\x35\n\remployee_data\x18\x01 \x03(\x0b\x32\x1e.employee_service.EmployeeData2\xec\x04\n\x0f\x45mployeeService\x12Q\n\x0e\x43reateEmployee\x12\x1e.employee_service.EmployeeData\x1a\x1d.employee_service.StatusReply\"\x00\x12W\n\x15GetEmployeeDataFromID\x12\x1c.employee_service.EmployeeID\x1a\x1e.employee_service.EmployeeData\"\x00\x12]\n\x13UpdateEmployeeTitle\x12%.employee_service.EmployeeTitleUpdate\x1a\x1d.employee_service.StatusReply\"\x00\x12O\n\x0e\x44\x65leteEmployee\x12\x1c.employee_service.EmployeeID\x1a\x1d.employee_service.StatusReply\"\x00\x12X\n\x10ListAllEmployees\x12\x1e.employee_service.EmptyMessage\x1a\".employee_service.EmployeeDataList\"\x00\x12Q\n\rHighestSalary\x12\x1e.employee_service.EmptyMessage\x1a\x1e.employee_service.EmployeeData\"\x00\x12P\n\x0cLowestSalary\x12\x1e.employee_service.EmptyMessage\x1a\x1e.employee_service.EmployeeData\"\x00\x42\x37\n\x1bio.grpc.examples.iotserviceB\x0fIoTServiceProtoP\x01\xa2\x02\x04TEMPb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EmployeeService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.iotserviceB\017IoTServiceProtoP\001\242\002\004TEMP'
  _globals['_EMPLOYEEDATA']._serialized_start=43
  _globals['_EMPLOYEEDATA']._serialized_end=114
  _globals['_STATUSREPLY']._serialized_start=116
  _globals['_STATUSREPLY']._serialized_end=145
  _globals['_EMPLOYEEID']._serialized_start=147
  _globals['_EMPLOYEEID']._serialized_end=171
  _globals['_EMPLOYEETITLEUPDATE']._serialized_start=173
  _globals['_EMPLOYEETITLEUPDATE']._serialized_end=221
  _globals['_EMPTYMESSAGE']._serialized_start=223
  _globals['_EMPTYMESSAGE']._serialized_end=237
  _globals['_EMPLOYEEDATALIST']._serialized_start=239
  _globals['_EMPLOYEEDATALIST']._serialized_end=312
  _globals['_EMPLOYEESERVICE']._serialized_start=315
  _globals['_EMPLOYEESERVICE']._serialized_end=935
# @@protoc_insertion_point(module_scope)