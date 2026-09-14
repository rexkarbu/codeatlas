"""Script to apply enriched curriculum to data_fundamentals.py and data_ecosystem.py.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

import data_fundamentals as df
import data_ecosystem as de

import curriculum_part1_logic_control_func as p1
import curriculum_part2_data_algo_paradigm as p2
import curriculum_part3_architecture_quality_memory as p3
import curriculum_part4a_io_system_networking as p4a
import curriculum_part4b_apis_storage_security_cs as p4b

import curriculum_ecosystem_part1 as ep1
import curriculum_ecosystem_part2_platforms_data_arch as ep2
import curriculum_ecosystem_part3_infra_cloud_security_devops as ep3
import curriculum_ecosystem_part4_data_ai_practices as ep4


def apply():
    f_curr = {
        **p1.CURRICULUM_PART1,
        **p2.CURRICULUM_PART2,
        **p3.CURRICULUM_PART3,
        **p4a.CURRICULUM_PART4A,
        **p4b.CURRICULUM_PART4B,
    }
    e_curr = {
        **ep1.ECOSYSTEM_CURRICULUM_PART1,
        **ep2.ECOSYSTEM_CURRICULUM_PART2,
        **ep3.ECOSYSTEM_CURRICULUM_PART3,
        **ep4.ECOSYSTEM_CURRICULUM_PART4,
    }

    print(f"Loaded {len(f_curr)} fundamental curriculum topics")
    print(f"Loaded {len(e_curr)} ecosystem curriculum topics")

    # Update fundamental topics
    updated_fundamentals = []
    for t in df.FUNDAMENTAL_TOPICS:
        t_id = t["id"]
        assert t_id in f_curr, f"Missing curriculum for fundamental topic {t_id}"
        c = f_curr[t_id]
        item = dict(t)
        item["summary"] = c.get("summary", item["summary"])
        item["explanation_simple"] = c["explanation_simple"]
        item["problem_context"] = c["problem_context"]
        item["explanation_technical"] = c["explanation_technical"]
        item["misconceptions"] = c["misconceptions"]
        item["when_to_use"] = c["when_to_use"]
        item["why_vibecoding_matters"] = c["why_vibecoding_matters"]
        item["reflection_questions"] = c["reflection_questions"]
        updated_fundamentals.append(item)

    # Update ecosystem topics
    updated_ecosystem = []
    for t in de.ECOSYSTEM_TOPICS:
        t_id = t["id"]
        assert t_id in e_curr, f"Missing curriculum for ecosystem topic {t_id}"
        c = e_curr[t_id]
        item = dict(t)
        item["summary"] = c.get("summary", item["summary"])
        item["explanation_simple"] = c["explanation_simple"]
        item["problem_context"] = c["problem_context"]
        item["explanation_technical"] = c["explanation_technical"]
        item["misconceptions"] = c["misconceptions"]
        item["when_to_use"] = c["when_to_use"]
        item["why_vibecoding_matters"] = c["why_vibecoding_matters"]
        item["reflection_questions"] = c["reflection_questions"]
        updated_ecosystem.append(item)

    print(f"Enriched {len(updated_fundamentals)} fundamental topics")
    print(f"Enriched {len(updated_ecosystem)} ecosystem topics")

    # Write updated data_fundamentals.py
    f_py = (
        '"""Fundamental Topics (47 topics) for CodeAtlas with 8 structured pedagogical dimensions."""\n\n'
        + "true = True\nfalse = False\nnull = None\n\n"
        + "FUNDAMENTAL_TOPICS = "
        + json.dumps(updated_fundamentals, indent=4, ensure_ascii=False)
        + "\n"
    )
    (ROOT / "data_fundamentals.py").write_text(f_py, encoding="utf-8")
    print(f"Updated {ROOT / 'data_fundamentals.py'}")

    # Write updated data_ecosystem.py
    e_py = (
        '"""Ecosystem Topics (52 topics) for CodeAtlas with 8 structured pedagogical dimensions."""\n\n'
        + "true = True\nfalse = False\nnull = None\n\n"
        + "ECOSYSTEM_TOPICS = "
        + json.dumps(updated_ecosystem, indent=4, ensure_ascii=False)
        + "\n"
    )
    (ROOT / "data_ecosystem.py").write_text(e_py, encoding="utf-8")
    print(f"Updated {ROOT / 'data_ecosystem.py'}")


if __name__ == "__main__":
    apply()
