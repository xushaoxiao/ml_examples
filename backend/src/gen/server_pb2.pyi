from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServerInfoResponse(_message.Message):
    __slots__ = ("server_name", "server_version", "server_status", "server_start_time", "server_uptime")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    SERVER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_UPTIME_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    server_version: str
    server_status: str
    server_start_time: str
    server_uptime: str
    def __init__(self, server_name: _Optional[str] = ..., server_version: _Optional[str] = ..., server_status: _Optional[str] = ..., server_start_time: _Optional[str] = ..., server_uptime: _Optional[str] = ...) -> None: ...
