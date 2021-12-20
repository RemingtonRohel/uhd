#
# TODO: Fill this in with proper copyright
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

""" @package usrp_clock
Python UHD module containing the MultiUSRPClock object
"""

from .. import libpyuhd as lib


MultiUSRPClock = lib.usrp_clock.multi_usrp_clock
