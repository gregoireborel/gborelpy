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

    def __init__(self, bucket, input_date, event_types):
        self.bucket = bucket
        self.input_date = input_date
        self.event_types = event_types

    def process(self, element):
        """
        Generates a GCS path for each event type and yields it.
        """
        for event_type in self.event_types:
            yield f"gs://{self.bucket}/{self.event_type}/{self.input_date.get()}**/**"

