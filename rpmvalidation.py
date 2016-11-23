# -*- coding: utf-8 -*-
# RPM Tests for Fedora Modularity
# Copyright (C) 2016  Stephen Gallagher
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import os
import rpm

from avocado import Test


class rpmvalidation(Test):
    # Provide a list of acceptable file paths based on
    # http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
    fhs_base_paths = [
        '/bin',
        '/boot',
        '/dev',
        '/etc',
        '/home',
        '/lib',
        '/lib64',
        '/media',
        '/mnt',
        '/opt',
        '/proc',
        '/root',
        '/run',
        '/sbin',
        '/sys',
        '/srv',
        '/tmp',
        '/usr/bin',
        '/usr/include',
        '/usr/lib',
        '/usr/libexec',
        '/usr/lib64',
        '/usr/local',
        '/usr/sbin',
        '/usr/share',
        '/usr/src',
        '/var/account',
        '/var/cache',
        '/var/crash',
        '/var/games',
        '/var/lib',
        '/var/lock',
        '/var/log',
        '/var/mail',
        '/var/opt',
        '/var/run',
        '/var/spool',
        '/var/tmp',
        '/var/yp'
    ]

    fhs_paths = [ os.path.realpath(path) for path in fhs_base_paths]

    def _compare_fhs(self, filepath):
        realpath = os.path.realpath(filepath)
        for path in self.fhs_paths:
            self.log.debug("Comparing %s to %s" % (realpath, path))
            if realpath.startswith(path):
                return True

        return False

    def test(self):
        rpmpath = self.params.get('rpmpath')

        ts = rpm.TransactionSet()
        fdno = os.open(rpmpath, os.O_RDONLY)
        hdr = ts.hdrFromFdno(fdno)
        os.close(fdno)

        for filename in hdr[rpm.RPMTAG_FILENAMES]:
            if not self._compare_fhs(filename):
                self.fail("File [%s] violates the FHS." % filename)