
import pandas as pd

import lambdalogging
from constants import CONTENT_LENGTH, S3_STATUS_CODES, S3_ERROR_CODES, error_code_to_enums, WRITE_GET_OBJECT_RESPONSE, \
    DOWNLOAD_PRESIGNED_URL, S3_MAX_RETRIES, S3, http_status_code_to_s3_status_code
from exceptions import UnsupportedFileException, FileSizeLimitExceededException, S3DownloadException

LOG = lambdalogging.getLogger(__name__)

class ExcelHandling:

    def __init__(self):
        pass

    def _get_excel_data(self, excel_file):
        data = pd.read_excel(excel_file)
        return str(data)
    