# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cairo(AutotoolsPackage):
    """Cairo is a 2D graphics library with support for multiple output
    devices."""

    homepage = "https://www.cairographics.org/"
    url      = "https://www.cairographics.org/releases/cairo-1.16.0.tar.xz"

    version('1.16.0', sha256='5e7b29b3f113ef870d1e3ecf8adf21f923396401604bda16d44be45e66052331')
    version('1.14.12', sha256='8c90f00c500b2299c0a323dd9beead2a00353752b2092ead558139bd67f7bf16')
    version('1.14.8', sha256='d1f2d98ae9a4111564f6de4e013d639cf77155baf2556582295a0f00a9bc5e20')
    version('1.14.0', sha256='2cf5f81432e77ea4359af9dcd0f4faf37d015934501391c311bfd2d19a0134b7')

    variant('X', default=False, description="Build with X11 support")
    variant('pdf', default=False, description="Enable cairo's PDF surface backend feature")
    variant('gobject', default=False, description="Enable cairo's gobject functions feature")
    variant('ft', default=False, description="Enable cairo's FreeType font backend feature")
    variant('fc', default=False, description="Enable cairo's Fontconfig font backend feature")
    variant('png', default=False, description="Enable cairo's PNG functions feature")
    variant('svg', default=False, description="Enable cairo's SVN functions feature")

    depends_on('libx11', when='+X')
    depends_on('libxext', when='+X')
    depends_on('libxrender', when='+X')
    depends_on('libxcb', when='+X')
    depends_on('python', when='+X', type='build')
    depends_on('libpng', when='+png')
    depends_on('librsvg', when='+svg')
    depends_on('glib')
    depends_on('pixman')
    depends_on('freetype', when='+ft')
    depends_on('pkgconfig', type='build')
    depends_on('fontconfig@2.10.91:', when='+fc')  # Require newer version of fontconfig.

    conflicts('+png', when='platform=darwin')
    conflicts('+svg', when='platform=darwin')

    def configure_args(self):
        args = [
            '--disable-trace',  # can cause problems with libiberty
            '--enable-tee'
        ]

        if '+X' in self.spec:
            args.extend(['--enable-xlib', '--enable-xcb'])
        else:
            args.extend(['--disable-xlib', '--disable-xcb'])

        args.extend(self.enable_or_disable('pdf'))
        args.extend(self.enable_or_disable('gobject'))
        args.extend(self.enable_or_disable('ft'))
        args.extend(self.enable_or_disable('fc'))

        return args
