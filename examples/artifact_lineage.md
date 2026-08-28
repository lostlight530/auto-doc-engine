# Artifact lineage example

Generate a normal artifact record first, then describe its relationship to earlier/related artifacts without modifying the original record.

```bash
python core/artifact_lineage.py output/report.artifact.json \
  --relation revision-of=archive/report-v1.artifact.json \
  --relation uses=data/source-dataset.json \
  --output output/report.lineage.json
```

Supported declared relations:

```text
derived-from
revision-of
supersedes
uses
related-to
```

Local target files receive SHA-256 identity. URI/opaque references are preserved without network dereference.

```text
revision-of != semantic equivalence
supersedes != deletion of history
uses != evidence sufficiency
lineage != scientific validity
```
