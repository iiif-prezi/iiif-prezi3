from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Configure retry logic (urllib3 - Retry)
# See https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry
_retries = Retry(
    total=3,
    backoff_factor=0.1,
    allowed_methods={'GET'},
    # also default value: adding for clarity
    respect_retry_after_header=True,
    #   413, 429, 503 by default
    # status_forcelist=[502, 503, 504]

)

# Initialize the global DEFAULT_SESSION object which is loaded once
DEFAULT_SESSION = Session()
DEFAULT_SESSION.mount('https://', HTTPAdapter(max_retries=_retries))
DEFAULT_SESSION.mount('http://', HTTPAdapter(max_retries=_retries))
