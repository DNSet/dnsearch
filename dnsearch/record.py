# coding:utf-8

from dnslib import A
from dnslib import AAAA
from dnslib import CNAME
from dnslib import DNSRecord
from dnslib import QTYPE
from dnslib import RR

from dnsearch.domain import Name


class Record():
    def __init__(self, name: Name, data: str):
        self.__name: str = str(name)
        self.__data: str = data

    @property
    def name(self) -> str:
        return self.__name

    @property
    def data(self) -> str:
        return self.__data


class RecordA(Record):
    RTYPE: int = QTYPE.A

    def __init__(self, name: Name, ipv4: str):
        super().__init__(name=name, data=ipv4)

    def to_rr(self, ttl: int = 0) -> RR:
        """DNS Resource Record"""
        return RR(self.name, self.RTYPE, rdata=A(self.data), ttl=ttl)


class Resources():
    def __init__(self, domain_name: str):
        self.__name: Name = Name(domain_name)

    @property
    def name(self) -> Name:
        return self.__name
