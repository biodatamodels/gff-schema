# Auto generated from gff.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-08 17:40
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
from includes.types import Float, Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GFF


# Types
class ControlledTermType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "controlled term type"
    type_model_uri = GFF.ControlledTermType


# Class references
class SeqID(URIorCURIE):
    pass


class GenomeFeatureAttributeSetID(URIorCURIE):
    pass


@dataclass
class Seq(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.Seq
    class_class_curie: ClassVar[str] = "gff:Seq"
    class_name: ClassVar[str] = "seq"
    class_model_uri: ClassVar[URIRef] = GFF.Seq

    ID: Union[str, SeqID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is None:
            raise ValueError("ID must be supplied")
        if not isinstance(self.ID, SeqID):
            self.ID = SeqID(self.ID)

        super().__post_init__(**kwargs)


@dataclass
class GenomeFeatureAttributeSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.GenomeFeatureAttributeSet
    class_class_curie: ClassVar[str] = "gff:GenomeFeatureAttributeSet"
    class_name: ClassVar[str] = "genome feature attribute set"
    class_model_uri: ClassVar[URIRef] = GFF.GenomeFeatureAttributeSet

    ID: Union[str, GenomeFeatureAttributeSetID] = None
    Name: Optional[str] = None
    Parent: Optional[Union[Union[dict, "GenomeFeature"], List[Union[dict, "GenomeFeature"]]]] = empty_list()
    Ontology_term: Optional[Union[Union[str, ControlledTermType], List[Union[str, ControlledTermType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is None:
            raise ValueError("ID must be supplied")
        if not isinstance(self.ID, GenomeFeatureAttributeSetID):
            self.ID = GenomeFeatureAttributeSetID(self.ID)

        if self.Name is not None and not isinstance(self.Name, str):
            self.Name = str(self.Name)

        if self.Parent is None:
            self.Parent = []
        if not isinstance(self.Parent, list):
            self.Parent = [self.Parent]
        self._normalize_inlined_slot(slot_name="Parent", slot_type=GenomeFeature, key_name="seqid", inlined_as_list=True, keyed=False)

        if self.Ontology_term is None:
            self.Ontology_term = []
        if not isinstance(self.Ontology_term, list):
            self.Ontology_term = [self.Ontology_term]
        self.Ontology_term = [v if isinstance(v, ControlledTermType) else ControlledTermType(v) for v in self.Ontology_term]

        super().__post_init__(**kwargs)


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

    seqid: str = None
    source: str = None
    start: int = None
    end: int = None
    type: Optional[Union[str, ControlledTermType]] = None
    strand: Optional[Union[str, "StrandEnum"]] = None
    phase: Optional[int] = None
    has_attributes: Optional[Union[str, GenomeFeatureAttributeSetID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.seqid is None:
            raise ValueError("seqid must be supplied")
        if not isinstance(self.seqid, str):
            self.seqid = str(self.seqid)

        if self.source is None:
            raise ValueError("source must be supplied")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self.start is None:
            raise ValueError("start must be supplied")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is None:
            raise ValueError("end must be supplied")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.type is not None and not isinstance(self.type, ControlledTermType):
            self.type = ControlledTermType(self.type)

        if self.strand is not None and not isinstance(self.strand, StrandEnum):
            self.strand = StrandEnum(self.strand)

        if self.phase is not None and not isinstance(self.phase, int):
            self.phase = int(self.phase)

        if self.has_attributes is not None and not isinstance(self.has_attributes, GenomeFeatureAttributeSetID):
            self.has_attributes = GenomeFeatureAttributeSetID(self.has_attributes)

        super().__post_init__(**kwargs)


# Enumerations
class StrandEnum(EnumDefinitionImpl):
    """
    strand
    """
    _defn = EnumDefinition(
        name="StrandEnum",
        description="strand",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "+",
                PermissibleValue(text="+",
                                 description="Positive") )
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="Negative") )
        setattr(cls, ".",
                PermissibleValue(text=".",
                                 description="Unstranded") )
        setattr(cls, "?",
                PermissibleValue(text="?",
                                 description="Unknown") )

# Slots
class slots:
    pass

slots.gff_attribute = Slot(uri=GFF.gff_attribute, name="gff attribute", curie=GFF.curie('gff_attribute'),
                   model_uri=GFF.gff_attribute, domain=None, range=Optional[str])

slots.gff_column = Slot(uri=GFF.gff_column, name="gff column", curie=GFF.curie('gff_column'),
                   model_uri=GFF.gff_column, domain=None, range=Optional[str])

slots.seqid = Slot(uri=GFF.seqid, name="seqid", curie=GFF.curie('seqid'),
                   model_uri=GFF.seqid, domain=None, range=str)

slots.source = Slot(uri=GFF.source, name="source", curie=GFF.curie('source'),
                   model_uri=GFF.source, domain=None, range=str)

slots.type = Slot(uri=GFF.type, name="type", curie=GFF.curie('type'),
                   model_uri=GFF.type, domain=None, range=Optional[Union[str, ControlledTermType]],
                   pattern=re.compile(r'^SO:\d+'))

slots.start = Slot(uri=GFF.start, name="start", curie=GFF.curie('start'),
                   model_uri=GFF.start, domain=None, range=int)

slots.end = Slot(uri=GFF.end, name="end", curie=GFF.curie('end'),
                   model_uri=GFF.end, domain=None, range=int)

slots.strand = Slot(uri=GFF.strand, name="strand", curie=GFF.curie('strand'),
                   model_uri=GFF.strand, domain=None, range=Optional[Union[str, "StrandEnum"]])

slots.score = Slot(uri=GFF.score, name="score", curie=GFF.curie('score'),
                   model_uri=GFF.score, domain=None, range=Optional[float])

slots.phase = Slot(uri=GFF.phase, name="phase", curie=GFF.curie('phase'),
                   model_uri=GFF.phase, domain=None, range=Optional[int])

slots.Ontology_term = Slot(uri=GFF.Ontology_term, name="Ontology term", curie=GFF.curie('Ontology_term'),
                   model_uri=GFF.Ontology_term, domain=None, range=Optional[Union[Union[str, ControlledTermType], List[Union[str, ControlledTermType]]]])

slots.ID = Slot(uri=GFF.ID, name="ID", curie=GFF.curie('ID'),
                   model_uri=GFF.ID, domain=None, range=URIRef)

slots.Parent = Slot(uri=GFF.Parent, name="Parent", curie=GFF.curie('Parent'),
                   model_uri=GFF.Parent, domain=None, range=Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]])

slots.Derives_from = Slot(uri=GFF.Derives_from, name="Derives from", curie=GFF.curie('Derives_from'),
                   model_uri=GFF.Derives_from, domain=None, range=Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]])

slots.Name = Slot(uri=GFF.Name, name="Name", curie=GFF.curie('Name'),
                   model_uri=GFF.Name, domain=None, range=Optional[str])

slots.Aliases = Slot(uri=GFF.Aliases, name="Aliases", curie=GFF.curie('Aliases'),
                   model_uri=GFF.Aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.gff_coordinate = Slot(uri=GFF.gff_coordinate, name="gff coordinate", curie=GFF.curie('gff_coordinate'),
                   model_uri=GFF.gff_coordinate, domain=None, range=Optional[int])

slots.has_attributes = Slot(uri=GFF.has_attributes, name="has attributes", curie=GFF.curie('has_attributes'),
                   model_uri=GFF.has_attributes, domain=None, range=Optional[Union[str, GenomeFeatureAttributeSetID]])
