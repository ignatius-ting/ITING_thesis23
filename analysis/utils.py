import pandas as pd
from Bio import Entrez
import xml.etree.ElementTree as ET


class PubmedQuery:
    def __init__(self, query, api_key, email='itin0003@student.monash.edu'):
        self.query = query
        self.email = email
        self.id_list = []
        self.xml_string = ""
        self.api_key = api_key

    def _define_email(self):
        Entrez.email = self.email

    def _define_api_key(self):
        Entrez.api_key = self.api_key

    def _get_ids(self):
        self._define_email()
        handle = Entrez.esearch(db='pubmed', term=self.query, retmax=1)
        record = Entrez.read(handle)
        handle.close()
        self.id_list = record['IdList']

    def _get_xml(self):
        fetch_handle = Entrez.efetch(db='pubmed', id=self.id_list)
        xml_raw = fetch_handle.read()
        self.xml_string = xml_raw.decode('utf-8')

    def _find_nodes_by_name(self, node, target_name):
        found_nodes = []
        if node.tag == target_name:
            found_nodes.append(node)
        for child in node:
            found_nodes.extend(self._find_nodes_by_name(child, target_name))
        return found_nodes
    
    def _parse_abstract_text(self, node):
        return ''.join(node.itertext()).strip()

    def get_abstracts(self, target_name='AbstractText'):
        self._get_ids()
        self._get_xml()
        root = ET.fromstring(self.xml_string)
        found_nodes = self._find_nodes_by_name(root, target_name)
        abstracts = [self._parse_abstract_text(node) for node in found_nodes]
        return abstracts

