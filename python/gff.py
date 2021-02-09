# Auto generated from gff.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-08 18:39
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
from biolinkml.utils.metamodelcore import Bool, URIorCURIE
from includes.types import Boolean, Float, Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
GFVO = CurieNamespace('gfvo', 'http://www.biointerchange.org/gfvo#')
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
class GffDocument(YAMLRoot):
    """
    Collection of GFF features and metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.GffDocument
    class_class_curie: ClassVar[str] = "gff:GffDocument"
    class_name: ClassVar[str] = "gff document"
    class_model_uri: ClassVar[URIRef] = GFF.GffDocument

    gff_version: Optional[str] = None
    feature_ontology_URI: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    attribute_ontology_URI: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    source_ontology_URI: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    species: Optional[Union[str, URIorCURIE]] = None
    sequence_region: Optional[Union[dict, "SequenceRegionValue"]] = None
    genome_build: Optional[Union[dict, "GenomeBuildValue"]] = None
    sequences: Optional[Union[Union[str, SeqID], List[Union[str, SeqID]]]] = empty_list()
    features: Optional[Union[Union[dict, "GenomeFeature"], List[Union[dict, "GenomeFeature"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gff_version is not None and not isinstance(self.gff_version, str):
            self.gff_version = str(self.gff_version)

        if self.feature_ontology_URI is None:
            self.feature_ontology_URI = []
        if not isinstance(self.feature_ontology_URI, list):
            self.feature_ontology_URI = [self.feature_ontology_URI]
        self.feature_ontology_URI = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.feature_ontology_URI]

        if self.attribute_ontology_URI is None:
            self.attribute_ontology_URI = []
        if not isinstance(self.attribute_ontology_URI, list):
            self.attribute_ontology_URI = [self.attribute_ontology_URI]
        self.attribute_ontology_URI = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.attribute_ontology_URI]

        if self.source_ontology_URI is None:
            self.source_ontology_URI = []
        if not isinstance(self.source_ontology_URI, list):
            self.source_ontology_URI = [self.source_ontology_URI]
        self.source_ontology_URI = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.source_ontology_URI]

        if self.species is not None and not isinstance(self.species, URIorCURIE):
            self.species = URIorCURIE(self.species)

        if self.sequence_region is not None and not isinstance(self.sequence_region, SequenceRegionValue):
            self.sequence_region = SequenceRegionValue(**self.sequence_region)

        if self.genome_build is not None and not isinstance(self.genome_build, GenomeBuildValue):
            self.genome_build = GenomeBuildValue(**self.genome_build)

        if self.sequences is None:
            self.sequences = []
        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences]
        self.sequences = [v if isinstance(v, SeqID) else SeqID(v) for v in self.sequences]

        if self.features is None:
            self.features = []
        if not isinstance(self.features, list):
            self.features = [self.features]
        self._normalize_inlined_slot(slot_name="features", slot_type=GenomeFeature, key_name="seqid", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Seq(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.Seq
    class_class_curie: ClassVar[str] = "gff:Seq"
    class_name: ClassVar[str] = "seq"
    class_model_uri: ClassVar[URIRef] = GFF.Seq

    ID: Union[str, SeqID] = None
    has_sequence_string: Optional[Union[str, "SequenceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is None:
            raise ValueError("ID must be supplied")
        if not isinstance(self.ID, SeqID):
            self.ID = SeqID(self.ID)

        if self.has_sequence_string is not None and not isinstance(self.has_sequence_string, SequenceEnum):
            self.has_sequence_string = SequenceEnum(self.has_sequence_string)

        super().__post_init__(**kwargs)


class Metadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.Metadata
    class_class_curie: ClassVar[str] = "gff:Metadata"
    class_name: ClassVar[str] = "metadata"
    class_model_uri: ClassVar[URIRef] = GFF.Metadata


@dataclass
class SequenceRegionValue(Metadata):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.SequenceRegionValue
    class_class_curie: ClassVar[str] = "gff:SequenceRegionValue"
    class_name: ClassVar[str] = "sequence region value"
    class_model_uri: ClassVar[URIRef] = GFF.SequenceRegionValue

    seqid: str = None
    start: int = None
    end: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        super().__post_init__(**kwargs)


@dataclass
class GenomeBuildValue(Metadata):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GFF.GenomeBuildValue
    class_class_curie: ClassVar[str] = "gff:GenomeBuildValue"
    class_name: ClassVar[str] = "genome build value"
    class_model_uri: ClassVar[URIRef] = GFF.GenomeBuildValue

    source: Optional[str] = None
    name: Optional[str] = None
    species: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

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
class PhaseEnum(EnumDefinitionImpl):
    """
    phase
    """
    _defn = EnumDefinition(
        name="PhaseEnum",
        description="phase",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="zero") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="one") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="two") )

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
                                 description="Positive",
                                 meaning=FALDO.ForwardStrandPosition) )
        setattr(cls, "-",
                PermissibleValue(text="-",
                                 description="Negative",
                                 meaning=FALDO.ReverseStrandPosition) )
        setattr(cls, ".",
                PermissibleValue(text=".",
                                 description="Unstranded",
                                 meaning=FALDO.BothStrandsPosition) )
        setattr(cls, "?",
                PermissibleValue(text="?",
                                 description="Unknown") )

class SequenceEnum(EnumDefinitionImpl):
    """
    type of sequence
    """
    NA = PermissibleValue(text="NA",
                           description="nucleic acid")
    AA = PermissibleValue(text="AA",
                           description="amino acid")

    _defn = EnumDefinition(
        name="SequenceEnum",
        description="type of sequence",
    )

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

slots.Note = Slot(uri=GFF.Note, name="Note", curie=GFF.curie('Note'),
                   model_uri=GFF.Note, domain=None, range=Optional[str])

slots.Aliases = Slot(uri=GFF.Aliases, name="Aliases", curie=GFF.curie('Aliases'),
                   model_uri=GFF.Aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.Dbxref = Slot(uri=GFF.Dbxref, name="Dbxref", curie=GFF.curie('Dbxref'),
                   model_uri=GFF.Dbxref, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]],
                   pattern=re.compile(r'^\S+:\S+'))

slots.Is_circular = Slot(uri=GFF.Is_circular, name="Is circular", curie=GFF.curie('Is_circular'),
                   model_uri=GFF.Is_circular, domain=None, range=Optional[Union[bool, Bool]])

slots.Target = Slot(uri=GFF.Target, name="Target", curie=GFF.curie('Target'),
                   model_uri=GFF.Target, domain=None, range=Optional[str])

slots.Gap = Slot(uri=GFF.Gap, name="Gap", curie=GFF.curie('Gap'),
                   model_uri=GFF.Gap, domain=None, range=Optional[str])

slots.gff_coordinate = Slot(uri=GFF.gff_coordinate, name="gff coordinate", curie=GFF.curie('gff_coordinate'),
                   model_uri=GFF.gff_coordinate, domain=None, range=Optional[int])

slots.has_attributes = Slot(uri=GFF.has_attributes, name="has attributes", curie=GFF.curie('has_attributes'),
                   model_uri=GFF.has_attributes, domain=None, range=Optional[Union[str, GenomeFeatureAttributeSetID]])

slots.has_metadata = Slot(uri=GFF.has_metadata, name="has metadata", curie=GFF.curie('has_metadata'),
                   model_uri=GFF.has_metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.ontology_URI = Slot(uri=GFF.ontology_URI, name="ontology URI", curie=GFF.curie('ontology_URI'),
                   model_uri=GFF.ontology_URI, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_sequence_string = Slot(uri=GFF.has_sequence_string, name="has sequence string", curie=GFF.curie('has_sequence_string'),
                   model_uri=GFF.has_sequence_string, domain=None, range=Optional[Union[str, "SequenceEnum"]])

slots.gffDocument__gff_version = Slot(uri=GFF.gff_version, name="gffDocument__gff_version", curie=GFF.curie('gff_version'),
                   model_uri=GFF.gffDocument__gff_version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^3\.\d+\.\d+$'))

slots.gffDocument__feature_ontology_URI = Slot(uri=GFF.feature_ontology_URI, name="gffDocument__feature_ontology_URI", curie=GFF.curie('feature_ontology_URI'),
                   model_uri=GFF.gffDocument__feature_ontology_URI, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gffDocument__attribute_ontology_URI = Slot(uri=GFF.attribute_ontology_URI, name="gffDocument__attribute_ontology_URI", curie=GFF.curie('attribute_ontology_URI'),
                   model_uri=GFF.gffDocument__attribute_ontology_URI, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gffDocument__source_ontology_URI = Slot(uri=GFF.source_ontology_URI, name="gffDocument__source_ontology_URI", curie=GFF.curie('source_ontology_URI'),
                   model_uri=GFF.gffDocument__source_ontology_URI, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.gffDocument__species = Slot(uri=GFF.species, name="gffDocument__species", curie=GFF.curie('species'),
                   model_uri=GFF.gffDocument__species, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.gffDocument__sequence_region = Slot(uri=GFF.sequence_region, name="gffDocument__sequence_region", curie=GFF.curie('sequence_region'),
                   model_uri=GFF.gffDocument__sequence_region, domain=None, range=Optional[Union[dict, SequenceRegionValue]])

slots.gffDocument__genome_build = Slot(uri=GFF.genome_build, name="gffDocument__genome_build", curie=GFF.curie('genome_build'),
                   model_uri=GFF.gffDocument__genome_build, domain=None, range=Optional[Union[dict, GenomeBuildValue]])

slots.gffDocument__sequences = Slot(uri=GFF.sequences, name="gffDocument__sequences", curie=GFF.curie('sequences'),
                   model_uri=GFF.gffDocument__sequences, domain=None, range=Optional[Union[Union[str, SeqID], List[Union[str, SeqID]]]])

slots.gffDocument__features = Slot(uri=GFF.features, name="gffDocument__features", curie=GFF.curie('features'),
                   model_uri=GFF.gffDocument__features, domain=None, range=Optional[Union[Union[dict, GenomeFeature], List[Union[dict, GenomeFeature]]]])

slots.genomeBuildValue__source = Slot(uri=GFF.source, name="genomeBuildValue__source", curie=GFF.curie('source'),
                   model_uri=GFF.genomeBuildValue__source, domain=None, range=Optional[str])

slots.genomeBuildValue__name = Slot(uri=GFF.name, name="genomeBuildValue__name", curie=GFF.curie('name'),
                   model_uri=GFF.genomeBuildValue__name, domain=None, range=Optional[str])

slots.genomeBuildValue__species = Slot(uri=GFF.species, name="genomeBuildValue__species", curie=GFF.curie('species'),
                   model_uri=GFF.genomeBuildValue__species, domain=None, range=Optional[str])
