import json
import logging

import apache_beam as beam


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
    input_date : ValueProvider
        A ValueProvider for the input date.
    event_types : list
        A list of predefined event types for generating paths.

    """

    def __init__(self, bucket, input_date):
        self.bucket = bucket
        self.input_date = input_date

    def process(self, element):
        """
        Generates a GCS path for each event type and yields it.
        """
        filename = (
            f"gs://{self.bucket}/Campaign Engagement/{self.input_date.get()}**/**"
        )
        yield filename
