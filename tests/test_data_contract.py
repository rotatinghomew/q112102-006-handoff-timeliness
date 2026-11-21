import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'policy': ['edition', 'valid_from', 'category', 'resident_limit', 'priority'], 'calendar': ['date', 'start', 'end', 'zone'], 'cases': ['case', 'category', 'accepted_at'], 'work': ['task', 'case', 'depends', 'department', 'responsibility'], 'actions': ['event', 'task', 'kind', 'reference', 'department', 'at'], 'amendments': ['id', 'target', 'field', 'replace', 'filed_at'], 'ledger': ['id', 'case', 'task', 'department', 'start', 'end', 'state']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
