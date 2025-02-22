"""
Help text strings for CLI utilities

Created on 15 Jan 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""
# pylint: disable=line-too-long

from platform import system

# console escape sequences don't work on standard Windows terminal
if system() == "Windows":
    GREEN = ""
    YELLOW = ""
    BOLD = ""
    NORMAL = ""
else:
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

GNSSDUMP_HELP = (
    f"\n\n{GREEN}{BOLD}GNSSDUMP\n"
    + f"========{NORMAL}\n\n"
    + "gnssdump is a command line utility to stream the "
    + "parsed NMEA or UBX output of a GNSS device to the terminal"
    + " or to designated UBX and/or NMEA protocol handlers.\n\n"
    + f"{GREEN}Usage (either stream, port or filename must be specified):{NORMAL}\n\n"
    + "  Serial stream: gnssdump port=/dev/ttyACM0 baudrate=9600 timeout=3, **kwargs\n"
    + "  File stream: gnssdump filename=gpslog.bin, **kwargs\n"
    + "  Other stream object: gnssdump stream=stream, **kwargs\n"
    + "  Help: gnssdump -h\n\n"
    + f"{GREEN}Optional keyword arguments (default):{NORMAL}\n\n"
    + "  protfilter - 1 = NMEA, 2 = UBX, 3 = both (3)\n"
    + "  msgfilter - comma-separated list of required message identities e.g. NAV-PVT,GNGSA (None)\n"
    + "  format - output format; 1 = parsed, 2 = binary (raw), 4 = hex, 8 = tabular hex (can be OR'd) (1)\n"
    + "  quitonerror - 0 = ignore errors,  1 = log errors and continue, 2 = (re)raise errors (1)\n"
    + "  validate - 1 = validate message checksum, 0 = ignore invalid checksum (1)\n"
    + "  msgmode - 0 = GET, 1 = SET, 2 = POLL (0)\n"
    + "  parsebitfield - boolean True = parse UBX 'X' type attributes as bitfields, False = leave as bytes (True)\n"
    + "  verbosity - log message verbosity 0 = low, 1 = medium, 2 = high (1)\n\n"
    + "  nmeahandler - evaluable expression defining external NMEA handler (None)\n"
    + "  ubxhandler - evaluable expression defining external UBX handler (None)\n"
    + "  errorhandler - evaluable expression defining external error handler (None)\n\n"
    + f"{GREEN}Type Ctrl-C to terminate.{NORMAL}\n\n"
    + f"{YELLOW}© 2022 SEMU Consulting BSD 3-Clause license\n"
    + f"https://github.com/semuconsulting/pyubx2/tree/master#cli{NORMAL}\n\n"
)

UBXDUMP_HELP = (
    "\n\nUBXDUMP\n"
    + "=======\n\n"
    + "ubxdump is a simple command line utility to stream"
    + " the parsed UBX output of a u-blox GNSS device to the terminal.\n\n"
    + "Usage (all args are optional):\n\n"
    + "  ubxdump port=/dev/ttyACM0 baud=9600 timeout=3 "
    + "ubxonly=0 validate=1 output=0 parsebitfield=1 "
    + "filter=*\n\n"
    + "Type Ctrl-C to terminate.\n\n"
    + "© 2021 SEMU Consulting BSD 3-Clause license\n"
    + "https://github.com/semuconsulting/pyubx2/tree/master#cli\n\n"
)
