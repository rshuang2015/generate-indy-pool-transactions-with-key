import os

# Current network
NETWORK_NAME = os.environ.get('NETWORK_NAME', 'sandbox')

# Disable stdout logging
enableStdOutLogging = os.environ.get('ENABLE_STDOUT_LOGGING', False)

# Directory to store ledger.
LEDGER_DIR = os.environ.get('LEDGER_DIR', '/var/lib/indy')

# Directory to store logs.
LOG_DIR = os.environ.get('LOG_DIR', '/var/log/indy')

# Directory to store keys.
KEYS_DIR = os.environ.get('KEYS_DIR', '/var/lib/indy')

# Directory to store genesis transactions files.
GENESIS_DIR = os.environ.get('GENESIS_DIR', '/var/lib/indy')

# Directory to store backups.
BACKUP_DIR = os.environ.get('BACKUP_DIR', '/var/lib/indy/backup')

# Directory to store plugins.
PLUGINS_DIR = os.environ.get('PLUGINS_DIR', '/var/lib/indy/plugins')

# Directory to store node info.
NODE_INFO_DIR = os.environ.get('NODE_INFO_DIR', '/var/lib/indy')
