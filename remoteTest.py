import time

import logging
from einder import Client
from einder import keys

# Enable logging.
logging.basicConfig(level=logging.DEBUG)

# Replace IP with the IP of your set-top box. The port parameter is optional,
# by default its 5900.
c = Client("192.168.178.80", port=5900)

c.send_key(keys.POWER)


# Wait a few seconds to let the set-top box have some time to start.
time.sleep(5)

# Select channel 501.

# For selecting a channel einder.Client offers a small helper function.

# No watch some TV...

c.disconnect()