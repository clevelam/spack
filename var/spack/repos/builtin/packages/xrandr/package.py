# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xrandr(AutotoolsPackage):
    """xrandr - primitive command line interface to X11 Resize, Rotate, and
    Reflect (RandR) extension."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xrandr"
    url      = "https://www.x.org/archive/individual/app/xrandr-1.5.0.tar.gz"

    version('1.5.0', sha256='ddfe8e7866149c24ccce8e6aaa0623218ae19130c2859cadcaa4228d8bb4a46d')

    depends_on('libxrandr@1.5:')
    depends_on('libxrender')
    depends_on('libx11')
    depends_on('randrproto')

    depends_on('xproto@7.0.17:', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
