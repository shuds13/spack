##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install nlopt
#
# You can edit this file again by typing:
#
#     spack edit nlopt
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Nlopt(CMakePackage):
#class Nlopt(AutotoolsPackage):    
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://nlopt.readthedocs.io"
    url      = "https://github.com/stevengj/nlopt/releases/download/nlopt-2.4.2/nlopt-2.4.2.tar.gz"

    version('develop', git='https://github.com/stevengj/nlopt.git', branch='master')
    version('2.4.2', 'd0b8f139a4acf29b76dbae69ade8ac54')
    
    variant('shared', default=True, description='Enables the build of shared libraries')
    variant('python', default=True, description='Build python wrappers')
    variant('guile',  default=False, description='Enable Guile support')
    variant('octave', default=False, description='Enable GNU Octave support')
    variant('cxx',    default=False,  description='Build the C++ routines')
    
    #Note: matlab is licenced - spack does not download automatically
    variant("matlab", default=False, description="Build the Matlab bindings.")
    
    # FIXME: Add dependencies if required.
    depends_on('cmake@3.0:', type='build',when='@develop')
    depends_on('python', when='+python')
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    depends_on('swig', when='+python')
    depends_on('guile', when='+guile')
    depends_on('octave', when='+octave')
    depends_on('matlab', when='+matlab')
    
    #Tarballs 2.4.2 and prev just use autotools - need to change class inheritance
    #def configure_args(self):
        ## FIXME: Add arguments other than --prefix
        ## FIXME: If not needed delete the function
        #spec = self.spec
        #args = []
        
        #if '+python' in self.spec:
            #args.extend([
                #'PYTHON={0}'.format(spec['python'].command.path)
                #])
        
        #if '+shared' in self.spec:
            #args.extend(['--enable-shared'])
            
        #return args    
 
    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        spec = self.spec
        args = []

        #Can just specify on command line to alter defaults - 
        #eg: spack install nlopt@develop +guile -octave +cxx
        
        #Some do not need cmake options when using spack - spack will locate
        
        #Spack should locate python by default - but for consistent cmake options
        if '+python' in spec:
            args.append("-DPYTHON_EXECUTABLE=%s" % spec['python'].command.path)
        
        #On is default
        if '-shared' in spec:
            args.append('-DBUILD_SHARED_LIBS:Bool=OFF')
            
        if '+cxx' in spec:
            args.append('-DNLOPT_CXX:BOOL=ON')
            
        if '+matlab' in spec:
            args.append("-DMatlab_ROOT_DIR=%s" % spec['matlab'].command.path)
            
        return args
    
