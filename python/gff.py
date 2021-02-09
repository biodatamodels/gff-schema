# Auto generated from gff.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-08 17:00
# Schema: GFF
#
# id: https://w3id.org/gff
# description: Playing around with GFF spec
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
DEFAULT_ = GFF


# Types

# Class references
class GenomeFeatureID(URIorCURIE):
    pass


@dataclass
class GenomeFeature(YAMLRoot):
    """
    A feature localized to an interval along a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.GenomeFeature
    class_class_curie: ClassVar[str] = "gff:GenomeFeature"
    class_name: ClassVar[str] = "genome feature"
    class_model_uri: ClassVar[URIRef] = GFF.GenomeFeature

    ID: Union[str, GenomeFeatureID] = None
    seqid: str = None
    start: int = None
    end: int = None
    type: Optional[str] = None
    strand: Optional[str] = None
    phase: Optional[int] = None
    Name: Optional[str] = None
    Parent: Optional[Union[Union[str, GenomeFeatureID], List[Union[str, GenomeFeatureID]]]] = empty_list()
    Ontology_term: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is None:
            raise ValueError("ID must be supplied")
        if not isinstance(self.ID, GenomeFeatureID):
            self.ID = GenomeFeatureID(self.ID)

        if self.seqid is None:
            raise ValueError("seqid must be supplied")
        if not isinstance(self.seqid, str):
            self.seqid = str(self.seqid)

        if self.start is None:
            raise ValueError("start must be supplied")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is None:
            raise ValueError("end must be supplied")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, int):
            self.phase = int(self.phase)

        if self.Name is not None and not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Parent is None:
            self.Parent = []
        if not isinstance(self.Parent, list):
            self.Parent = [self.Parent]
        self.Parent = [v if isinstance(v, GenomeFeatureID) else GenomeFeatureID(v) for v in self.Parent]

        if self.Ontology_term is None:
            self.Ontology_term = []
        if not isinstance(self.Ontology_term, list):
            self.Ontology_term = [self.Ontology_term]
        self.Ontology_term = [v if isinstance(v, str) else str(v) for v in self.Ontology_term]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.seqid = Slot(uri=GFF.seqid, name="seqid", curie=GFF.curie('seqid'),
                   model_uri=GFF.seqid, domain=None, range=str)

slots.type = Slot(uri=GFF.type, name="type", curie=GFF.curie('type'),
                   model_uri=GFF.type, domain=None, range=Optional[str])

slots.start = Slot(uri=GFF.start, name="start", curie=GFF.curie('start'),
                   model_uri=GFF.start, domain=None, range=int)

slots.end = Slot(uri=GFF.end, name="end", curie=GFF.curie('end'),
                   model_uri=GFF.end, domain=None, range=int)

slots.strand = Slot(uri=GFF.strand, name="strand", curie=GFF.curie('strand'),
                   model_uri=GFF.strand, domain=None, range=Optional[str])

slots.phase = Slot(uri=GFF.phase, name="phase", curie=GFF.curie('phase'),
                   model_uri=GFF.phase, domain=None, range=Optional[int])

slots.gff_attribute = Slot(uri=GFF.gff_attribute, name="gff attribute", curie=GFF.curie('gff_attribute'),
                   model_uri=GFF.gff_attribute, domain=None, range=Optional[str])

slots.Ontology_term = Slot(uri=GFF.Ontology_term, name="Ontology term", curie=GFF.curie('Ontology_term'),
                   model_uri=GFF.Ontology_term, domain=None, range=Optional[Union[str, List[str]]])

slots.ID = Slot(uri=GFF.ID, name="ID", curie=GFF.curie('ID'),
                   model_uri=GFF.ID, domain=None, range=URIRef)

slots.Parent = Slot(uri=GFF.Parent, name="Parent", curie=GFF.curie('Parent'),
                   model_uri=GFF.Parent, domain=None, range=Optional[Union[Union[str, GenomeFeatureID], List[Union[str, GenomeFeatureID]]]])

slots.Name = Slot(uri=GFF.Name, name="Name", curie=GFF.curie('Name'),
                   model_uri=GFF.Name, domain=None, range=Optional[str])

slots.gff_coordinate = Slot(uri=GFF.gff_coordinate, name="gff coordinate", curie=GFF.curie('gff_coordinate'),
                   model_uri=GFF.gff_coordinate, domain=None, range=Optional[int])
