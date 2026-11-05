"""Consumer-facing artifact identity, lineage, and publication metadata contracts.

Fixtures exercise real local producer functions, not downstream scientific truth
or third-party RO-Crate validation.
"""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import yaml

from core.artifact_record import build_artifact_record
from core.artifact_lineage import build_artifact_lineage
from core.ro_crate import build_ro_crate


ROOT = Path(__file__).resolve().parents[1]


class CrossRepositoryContract(unittest.TestCase):
    def test_document_producer_lineage_handoff_preserves_identity_not_truth(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "source.md"
            source.write_text("# A declared document\n", encoding="utf-8")
            record = build_artifact_record(source, reproducibility_level="R1")
            self.assertEqual(record["profile"], "auto-doc-engine/artifact-record")
            self.assertFalse(record["scientific_validity_claim"])
            self.assertFalse(record["payloads_embedded"])

            sidecar = root / "record.json"
            sidecar.write_text(json.dumps(record), encoding="utf-8")
            lineage = build_artifact_lineage(sidecar, relations=[("uses", str(source))])
            self.assertEqual(lineage["profile"], "auto-doc-engine/artifact-lineage")
            self.assertEqual(lineage["artifact_record"]["source_profile"], record["profile"])
            self.assertEqual(
                lineage["artifact_record"]["file_sha256"],
                "sha256:" + hashlib.sha256(sidecar.read_bytes()).hexdigest(),
            )
            link = lineage["relations"][0]
            self.assertEqual(link["relation"], "uses")
            self.assertEqual(link["target"]["resolution"], "local-file")
            self.assertFalse(link["scientific_validity_inherited"])
            self.assertFalse(link["reproducibility_inherited"])

            crate = build_ro_crate(root, [source], name="Handoff", description="Structural test")
            self.assertEqual(crate["@context"], "https://w3id.org/ro/crate/1.3/context")
            self.assertTrue(any(x.get("@id") == "source.md" for x in crate["@graph"]))

    def test_codemeta_v4_citation_identity_stays_consistent(self):
        meta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
        cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(meta["@context"], "https://w3id.org/codemeta/4.0")
        self.assertEqual(meta["@type"], "SoftwareSourceCode")
        self.assertEqual(meta["codeRepository"], cff["repository-code"])
        self.assertEqual(meta["identifier"], "https://doi.org/" + cff["identifiers"][0]["value"])
        self.assertNotIn("relatedSoftware", meta)


if __name__ == "__main__":
    unittest.main()
