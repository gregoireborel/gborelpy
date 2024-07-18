import json
import logging

import apache_beam as beam
from google.cloud import bigquery


class ParseJSON(beam.DoFn):
    def process(self, row):
        data = row.strip()
        try:
            yield json.loads(data, strict=False)
        except Exception as e:
            logging.error("The following error occuried while json parsing : ", str(e))


class GeneratePath(beam.DoFn):
    """
    A DoFn class for generating GCS paths based on input date and predefined event types.

    Attributes:

    bucket : str
        The name of the GCS bucket.
    input_date : str
        A string for the input date.
    event_types : list
        A list of predefined event types for generating paths.

    """

    def __init__(self, bucket, files_prefix, input_date):
        self.bucket = bucket
        self.files_prefix = files_prefix
        self.input_date = input_date

    def process(self, element):
        """
        Generates a GCS path for each event type and yields it.
        """
        path = (
            f"gs://{self.bucket}/{self.files_prefix}/**"
            if self.files_prefix
            else f"gs://{self.bucket}"
        )
        final_path = (
            f"{path}/{self.input_date.get()}**/**" if self.input_date else f"{path}/**"
        )
        yield final_path


class UpsertQueryToBQ(beam.DoFn):
    def __init__(self, project_id, dataset, table, query):
        self.project_id = project_id
        self.dataset = dataset
        self.table = table
        self.QUERY = query

    def setup(self):
        self.bigquery_client = bigquery.Client(project=self.project_id)

    def process(self, element):
        try:
            logging.info(
                "Executing MERGE operation for {}.{}.{} table.".format(
                    self.project_id, self.dataset, self.table
                )
            )
            query_job = self.bigquery_client.query(self.QUERY)
            query_job.result()
            logging.info(
                "MERGE operation completed for {}.{}.{} table.".format(
                    self.project_id, self.dataset, self.table
                )
            )

        except Exception as e:
            logging.error(
                "Error during MERGE operation for {}.{}.{} table: {}".format(
                    self.project_id, self.dataset, self.table, str(e)
                )
            )
