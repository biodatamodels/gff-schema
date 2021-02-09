# Introduction

## What

This is a repository for a DRAFT of a computable schema for GFF3

It is designed to separate out the *datamodel* from the *serialization* (TSV)

The schema is specified using a YAML file https://github.com/berkeleybop/gff-schema/blob/main/src/schema/gff.yaml

This is compiled into multiple artefacts including:

 * jsonschema
 * ShEx
 * graphql
 * python object model (dataclasses)
 * SQL DDL (soon)

And also online documentation:

https://berkeleybop.github.io/gff-schema/

## Why

Currently the GFF3 spec and proposed extensions or supplementary specs are specified as text. Text is non-computable which means

 * additional work in implementing validators
 * potential ambiguities in interpretation
 * additional work to create anciliary artefacts - e.g. a SQL schema or a JSON schema

Additionally, GFF3 is a TSV-based format which limits ability to use standard off the shelf validation approaches - e.g. OWL or ShEx validation for RDF, or JSON-Schema for JSON

## Approach

This project is neutral on the question of TSV serialization vs JSON serialization vs RDF vs XML ...

It takes the view that datamodel and serialization are *separate concerns*

We first define a UML-like abstract data model. We can then have as many serializations as we like

 * JSON
 * TSV

The specification of how to map the data model to the TSV becomes a separate (simpler) problem, distinct from specifying the data model itself.

It could be argued this is overkill. GFF3 is designed to be simple,
it's tight coupling to a TSV representation is arguably a feature,
forcing a simplicity. Yet as it is crucial to multiple projects this
arguably is a limitation.

Minimally this project provides clear *data dictionary* of all attributes used in SO, plus computable constraints on each

## Similar Work

 * GFFO
 * FALDO
 * AgBio specs

## Status: PROOF OF CONCEPT

This is currently the work of a 15 minute linkml demo session on a BBOP hangout. Much more needs to be done!!!


## Repository

https://github.com/berkeleybop/gff-schema

